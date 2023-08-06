from typing import Dict, Optional
from retrying import retry

from config.frozen import Frozen
from config.exception import OrderPendingException, \
    retry_if_order_not_sent_exception, retry_if_order_not_accepted_exception
from config.constants import Type, CMD, Cmd, STATUS, Status
from config.logger import logger
from xtb import Xtb
from models.transaction import Transaction


class Trade(Frozen):
    def __init__(self, trade_raw: Dict):
        trade_raw['order'] = trade_raw.get('order', 0)
        trade_raw['offset'] = trade_raw.get('offset', 0)
        trade_raw['sl'] = trade_raw.get('sl', 0)
        trade_raw['tp'] = trade_raw.get('tp', 0)
        trade_raw['profit'] = trade_raw.get('profit', 0)
        trade_raw['expiration'] = trade_raw.get('expiration', 0)
        trade_raw['storage'] = trade_raw.get('storage', 0)
        self.__order: Optional[int] = trade_raw['order']
        self.__cmd: int = trade_raw['cmd']
        self.__comment: str = trade_raw['comment']
        self.__offset: Optional[float] = trade_raw['offset']
        self.__sl: Optional[float] = trade_raw['sl']
        self.__tp: Optional[float] = trade_raw['tp']
        self.__symbol: str = trade_raw['symbol']
        self.__volume: float = trade_raw['volume']
        self.__profit: Optional[float] = trade_raw['profit']
        self.__storage: Optional[float] = trade_raw['storage']
        self.__raw: Dict = trade_raw
        self.__transaction: Optional[Transaction] = None

        self.__digits: int = trade_raw['digits']
        self.__commission: float = trade_raw['commission']
        self.__close_price: float = trade_raw['close_price']
        self.__open_price: float = trade_raw['open_price']
        self.__open_time: int = trade_raw['open_time']
        self.__close_time: int = trade_raw['close_time']
        self.__timestamp: int = trade_raw['timestamp']
        self.__closed: bool = trade_raw['closed'] == 'true'

    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, value: int) -> None:
        self.__order = value

    @property
    def cmd(self) -> int:
        return self.__cmd

    @property
    def comment(self) -> str:
        return self.__comment

    @property
    def offset(self) -> float:
        return self.__offset

    @property
    def sl(self) -> float:
        return self.__sl

    @property
    def tp(self) -> float:
        return self.__tp

    @property
    def symbol(self) -> str:
        return self.__symbol

    @property
    def volume(self) -> float:
        return self.__volume

    @property
    def raw(self) -> Dict:
        return self.__raw

    @property
    def profit(self) -> float:
        return self.__profit

    @property
    def storage(self) -> float:
        return self.__storage

    @property
    def transaction(self) -> Transaction:
        return self.__transaction

    @property
    def accepted(self) -> bool:
        try:
            return self.transaction.accepted
        except:
            return False

    @property
    def digits(self) -> int:
        return self.__digits

    @property
    def commission(self) -> float:
        return self.__commission

    @property
    def close_price(self) -> float:
        return self.__close_price

    @property
    def open_price(self) -> float:
        return self.__open_price

    @property
    def open_time(self) -> int:
        return self.__open_time

    @property
    def close_time(self) -> int:
        return self.__close_time

    @property
    def timestamp(self) -> int:
        return self.__timestamp

    @property
    def closed(self) -> bool:
        return self.__closed

    def transact(self, xtb: Xtb, _type: int) -> None:
        symbol = xtb.get_client().get_symbol(symbol=self.__symbol)
        if _type == Type.OPEN:
            if self.cmd == Cmd.BUY:
                self.raw['open_price'] = symbol['ask']
            elif self.cmd == Cmd.SELL:
                self.raw['open_price'] = symbol['bid']
        self.send_transaction(xtb=xtb, _type=_type)
        self.check_order_sent(xtb=xtb)

    @retry(retry_on_exception=retry_if_order_not_sent_exception,
           stop_max_attempt_number=5, wait_exponential_multiplier=1000, wait_exponential_max=10000)
    def send_transaction(self, xtb: Xtb, _type: int) -> None:
        # TODO: check lotMin del symbol antes de mandar transaction y devolver una exception
        self.transaction = Transaction(order=xtb.get_client().trade_transaction(trade=self.raw, _type=_type))

    @retry(retry_on_exception=retry_if_order_not_accepted_exception,
           stop_max_attempt_number=5, wait_exponential_multiplier=1000, wait_exponential_max=10000)
    def check_order_sent(self, xtb: Xtb):
        try:
            transaction = xtb.get_client().trade_transaction_status(transacting_order=self.transaction.order)
            self.transaction.status = STATUS[transaction['requestStatus']]
            self.transaction.message = transaction['message']
            self.transaction.custom_comment = transaction['customComment']
            self.transaction.ask = transaction['ask']
            self.transaction.bid = transaction['bid']
            if self.transaction.status == Status.ACCEPTED:
                logger.debug(f"Trade order '{self.order} - {self.symbol} - {CMD[self.cmd]}' is CLOSED. "
                             f"Transaction order is {self.transaction.order}")
            elif self.transaction.status == Status.PENDING:
                logger.warning(f"Trade order '{self.order} - {self.symbol} - {CMD[self.cmd]}' is PENDING. "
                               f"Transaction order is {self.transaction}")
                raise OrderPendingException(f"Trade order '{self.order} is PENDING. "
                                            f"Closing order is {self.transaction}")
            elif self.transaction.status == Status.ERROR:
                logger.error(f"Trade order '{self.order} - {self.symbol} - {CMD[self.cmd]}' has FAILED. "
                             f"Transaction: {self.transaction}")
            elif self.transaction.status == Status.REJECTED:
                logger.error(f"Trade order '{self.order} - {self.symbol} - {CMD[self.cmd]}' has been REJECTED. "
                             f"Transaction order is {self.transaction}")
        except OrderPendingException:
            self.transaction.status = Status.PENDING
        except Exception as e:
            logger.error(e)
