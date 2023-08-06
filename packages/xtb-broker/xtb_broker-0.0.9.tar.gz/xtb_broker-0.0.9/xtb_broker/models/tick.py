from typing import Dict, Optional
from datetime import datetime

from config.frozen import Frozen
from config.constants import WEEKDAY
from models.timetable import Timetable
from models.shift import Shift

from xtb import Xtb


class Tick(Frozen):
    def __init__(self, xtb: Xtb, symbol: str, timestamp: int   = None):
        tick_dict: Dict = xtb.get_client().get_symbol(symbol=symbol)
        self.__symbol: str = tick_dict['symbol']
        self.__ask: float = tick_dict['ask']
        self.__bid: float = tick_dict['bid']
        self.__high: float = tick_dict['high']
        self.__low: float = tick_dict['low']
        self.__timestamp: int = timestamp or tick_dict['timestamp']
        self.__spread: float = tick_dict['spreadRaw']

    @property
    def symbol(self) -> str:
        return self.__symbol

    @property
    def ask(self) -> float:
        return self.__ask

    @property
    def bid(self) -> float:
        return self.__bid

    @property
    def high(self) -> float:
        return self.__high

    @property
    def low(self) -> float:
        return self.__low

    @property
    def timestamp(self) -> int:
        return self.__timestamp

    @property
    def spread(self) -> float:
        return self.__spread
