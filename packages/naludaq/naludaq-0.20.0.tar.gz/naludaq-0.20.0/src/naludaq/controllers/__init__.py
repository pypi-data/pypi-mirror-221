"""Controllers change one aspects of the board.

The different controllers change how the board operates.
They are divided based on function.

Controllers are one abstraction step over communication. By manipulating
different registers through the communication layer the controllers
change the desired behaviour.

The controller can't import other controllers, a controller controls an aspect of the board
But doesn't create larger behaviors

DESCRIPTIONS:
=============
Controller:
-----------
Base class for controllers, it accepts one init parameter: board
The board is a property and can be get/set for all controllers.

BoardController:
----------------
Control the overarching state of the board.

"""
from naludaq.controllers.trigger import get_trigger_controller

from .biasing_mode import get_biasing_mode_controller
from .board import BoardController, UpacBoardController, get_board_controller
from .connection import get_connection_controller
from .external_dac import get_dac_controller
from .gainstages import get_gainstage_controller
from .peripherals import get_peripherals_controller
from .readout import get_readout_controller
from .si5341_controller import Si5341Controller
from .tia import get_tia_controller
