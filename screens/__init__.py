from .abstract import AbstractScreen
from .battle import BattleScreen
from .credits import CreditsScreen
from .moveChoosing import MoveChoosingScreen
from .teamChoosing import TeamChoosingScreen
from .title import TitleScreen
from .stage import StageScreen
from .continueScreen import ContinueScreen
from .gameOver import GameOverScreen

text_to_screen = {
    "AbstractScreen": AbstractScreen,
    "BattleScreen": BattleScreen,
    "CreditsScreen": CreditsScreen,
    "MoveChoosingScreen": MoveChoosingScreen,
    "TeamChoosingScreen": TeamChoosingScreen,
    "TitleScreen": TitleScreen,
    "StageScreen": StageScreen,
    "ContinueScreen": ContinueScreen,
    "GameOverScreen": GameOverScreen
}
