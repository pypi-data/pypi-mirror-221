from typing import Dict, Optional
from datetime import datetime

from config.frozen import Frozen
from config.constants import WEEKDAY
from models.timetable import Timetable
from models.shift import Shift

from xtb import Xtb


class Symbol(Frozen):
    def __init__(self, xtb: Xtb, symbol: str):
        symbol_dict: Dict = xtb.get_client().get_symbol(symbol=symbol)
        self.__symbol: str = symbol_dict['symbol']
        self.__currency: str = symbol_dict['currency']
        self.__currency_profit: str = symbol_dict['currencyProfit']
        self.__contract_size: str = symbol_dict['contractSize']
        self.__precision: str = symbol_dict['precision']
        self.__bid: str = symbol_dict['bid']
        self.__ask: str = symbol_dict['ask']
        self.__swap_long: str = symbol_dict['swapLong']
        self.__swap_short: str = symbol_dict['swapShort']
        self.__spread: float = symbol_dict['spreadRaw']

        self.__time: int = symbol_dict['time']
        self.__pips_precision: int = symbol_dict['pipsPrecision']
        self.__tick_size: float = symbol_dict['tickSize']
        self.__leverage: float = symbol_dict['leverage']

        self.__timetable: Timetable = xtb.get_symbol_timetable(symbol=symbol)

    @property
    def symbol(self) -> str:
        return self.__symbol

    @property
    def currency(self) -> str:
        return self.__currency

    @property
    def currency_profit(self) -> str:
        return self.__currency_profit

    @property
    def contract_size(self) -> str:
        return self.__contract_size

    @property
    def precision(self) -> str:
        return self.__precision

    @property
    def bid(self) -> str:
        return self.__bid

    @property
    def ask(self) -> str:
        return self.__ask

    @property
    def swap_long(self) -> str:
        return self.__swap_long

    @property
    def swap_short(self) -> str:
        return self.__swap_short

    @property
    def timetable(self) -> Timetable:
        return self.__timetable

    @property
    def spread(self) -> float:
        return self.__spread

    @property
    def time(self) -> int:
        return self.__time

    @property
    def pips_precision(self) -> int:
        return self.__pips_precision

    @property
    def tick_size(self) -> float:
        return self.__tick_size

    @property
    def leverage(self) -> float:
        return self.__leverage

    def get_active_shift(self) -> Optional[Shift]:
        for shift in getattr(self.timetable, WEEKDAY[datetime.today().isoweekday()]):
            if shift.from_ts < datetime.now() < shift.to_ts:
                return shift
