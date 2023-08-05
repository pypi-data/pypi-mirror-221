"""Initializer for the HDSoCv1 board

This initializer will run the init sequence for the HDSoCv1 board.
It contains the HDSoCv1 specific startup sequence.
"""
import logging
import time

from naludaq.board.initializers import Initializers
from naludaq.controllers import Si5341Controller, get_dac_controller
from naludaq.helpers.decorators import log_function

logger = logging.getLogger("naludaq.init_hdsocv1")

VALID_BOARDS = [
    "hdsocv1",
    "hdsocv1_evalr1",
    "hdsocv1_evalr2",
]


class InitHDSoCv1(Initializers):
    def __init__(self, board):
        """Initializer for HDSoCv1.

        Args:
            board (Board): the board to initialize.
        """
        super().__init__(board, VALID_BOARDS)
        self.power_sequence = [
            "2v5_en",
            "1v2_en",
            "3v3_i2c_en",
            "clk2v5_en",
            "clk1v8_en",
            "clk_i2c_sel",
        ]

    def run(self) -> bool:
        """Runs the initialization sequence.

        Returns:
            True, always.
        """
        # Initialize FPGA registers
        self._fpga_init()

        # Power on FMC board
        self._power_toggle(False)
        self._power_toggle(True)
        time.sleep(0.25)

        self._program_clock()

        # Chip-side register startup
        self._analog_startup()
        self._digital_startup()

        # Set DACs
        self._init_dacs()

        return True

    @log_function(logger)
    def _fpga_init(self):
        """Write all FPGA registers to their default values."""
        self.control_registers.write_all()
        self.i2c_registers.write("i2c_en", True)

    @log_function(logger)
    def _power_toggle(self, state):
        """Toggles the power rails defined in `power_sequence` attribute."""
        for register in self.power_sequence:
            self.control_write(register, state)

    @log_function(logger)
    def _program_clock(self):
        """Program the clock chip, uses the clockfile in the paramters if it exits."""
        Si5341Controller(self.board).program(filename=self.board.params["clock_file"])
        self.control_write("clk_oeb", False)
        self.control_write("sysrst", True)
        self.control_write("sysrst", False)
        self.control_write("iomode0", True)
        self.control_write("iomode1", False)
        self.control_write("regclr", True)
        self.control_write("regclr", False)

    @log_function(logger)
    def _reset_sys(self):
        """Reset the ASIC and clear the analog and digital registers"""
        self.control_write("sysrst", True)
        self.control_write("regclr", True)

        self.control_write("sysrst", False)
        self.control_write("regclr", False)

    @log_function(logger)
    def _digital_startup(self):
        """Startup the digital side of the chip by programming all registers."""
        self.digital_registers.write_all()

    @log_function(logger)
    def _analog_startup(self):
        """Start the analog side of the chip by programming all registers."""
        self.analog_registers.write_all()
        self._dll_startup()

    @log_function(logger)
    def _dll_startup(self):
        """Starting the delay line on the analog side.

        Sets and unsets vanbuff to get the dll going and
        changes the vadjp values to ensure proper SST duty cycle once locked.
        """
        self.analog_write("qbias_left", 0)
        self.analog_write("qbias_right", 0)
        self.analog_write("vanbuf_left", 2816)
        self.analog_write("vanbuf_right", 2816)
        time.sleep(1)
        self.analog_write("qbias_left", 2048)
        self.analog_write("qbias_right", 2048)
        self.analog_write("vanbuf_left", 0)
        self.analog_write("vanbuf_right", 0)

        self.analog_write("vadjp_right", 0x8DA)
        self.analog_write("vadjp_left", 0x8DA)

    @log_function(logger)
    def _init_dacs(self):
        """Program the left and right side DACs"""
        dacvalues = self._get_dac_values()

        for channel, value in dacvalues.items():
            get_dac_controller(self.board).set_single_dac(channel, value)

    def _get_dac_values(self) -> dict:
        """Return a dict with all the {channels: dac_values}"""
        return self.board.params.get("ext_dac", {}).get("channels", {})
