# orders.py

import datetime as dt
from typing import (
    Dict, Optional, Iterable, Union, List, Callable
)

import pandas as pd

from cryptofeed.types import Ticker
from cryptofeed.defines import TICKER

from crypto_screening.symbols import adjust_symbol
from crypto_screening.dataset import (
    BIDS, ASKS, ORDERS_COLUMNS, create_dataset
)
from crypto_screening.market.screeners.base import BaseScreener
from crypto_screening.market.screeners.callbacks import (
    BaseCallback, callback_data
)
from crypto_screening.market.screeners.recorder import (
    MarketScreener, MarketRecorder, MarketHandler
)
__all__ = [
    "OrdersMarketScreener",
    "OrdersMarketRecorder",
    "OrdersScreener",
    "orders_market_screener",
    "create_orders_market_dataset",
    "record_orders",
    "create_orders_screeners"
]

def create_orders_market_dataset() -> pd.DataFrame:
    """
    Creates a dataframe for the order book data.

    :return: The dataframe.
    """

    return create_dataset(
        columns=OrdersMarketRecorder.COLUMNS
    )
# end create_orderbook_market_dataset

class OrdersScreener(BaseScreener):
    """
    A class to represent an asset price screener.

    Using this class, you can create a screener object to
    screen the market ask and bid data for a specific asset in
    a specific exchange at real time.

    Parameters:

    - symbol:
        The symbol of an asset to screen.

    - exchange:
        The key of the exchange platform to screen data from.

    - location:
        The saving location for the saved data of the screener.

    - cancel:
        The time to cancel screening process after no new data is fetched.

    - delay:
        The delay to wait between each data fetching.

    - market:
        The dataset of the market data as orders.
    """

    NAME = "ORDERS"

    COLUMNS = ORDERS_COLUMNS

    @property
    def orders_market(self) -> pd.DataFrame:
        """
        Returns the market to hold the recorder data.

        :return: The market object.
        """

        return self.market
    # end orders_market
# end OrdersScreener

async def record_orders(
        screeners: Iterable[OrdersScreener],
        data: Ticker,
        timestamp: float,
        callbacks: Optional[Iterable[BaseCallback]] = None
) -> bool:
    """
    Records the data from the crypto feed into the dataset.

    :param screeners: The screeners.
    :param data: The data from the exchange.
    :param timestamp: The time of the request.
    :param callbacks: The callbacks for the service.

    :return: The validation value.
    """

    exchange = data.exchange.lower()
    symbol = adjust_symbol(symbol=data.symbol)

    try:
        index = dt.datetime.fromtimestamp(timestamp)

        data = {
            BIDS: float(data.bid),
            ASKS: float(data.ask)
        }

        valid = False

        for screener in screeners:
            if index in screener.market.index:
                continue
            # end if

            valid = True

            screener.market.loc[index] = data
        # end for

        if valid:
            for callback in callbacks or []:
                payload = callback_data(
                    data=[(timestamp, data)],
                    exchange=exchange, symbol=symbol
                )

                await callback.record(
                    payload, timestamp, key=OrdersScreener.NAME
                )
            # end if
        # end if

        return True

    except IndexError:
        return False
    # end try
# end record_orders

RecorderParameters = Dict[str, Union[Iterable[str], Dict[str, Callable]]]

class OrdersMarketRecorder(MarketRecorder):
    """
    A class to represent a crypto data feed recorder.
    This object passes the record method to the handler object to record
    the data fetched by the handler.

    Parameters:

    - screeners:
        The screeners to record data into their market datasets.

    - callbacks:
        The callbacks to run when collecting new data.

    >>> from crypto_screening.market.screeners import OrdersMarketRecorder
    >>>
    >>> recorder = OrdersMarketRecorder(...)
    """

    COLUMNS = OrdersScreener.COLUMNS

    @property
    def orders_screeners(self) -> List[OrdersScreener]:
        """
        Returns a list of all the order-book screeners.

        :return: The order-book screeners.
        """

        return self.find_screeners(base=OrdersScreener)
    # end orders_screeners

    def parameters(self) -> RecorderParameters:
        """
        Returns the order book parameters.

        :return: The order book parameters.
        """

        return dict(
            channels=[TICKER],
            callbacks={TICKER: self.record},
            max_depth=1
        )
    # end parameters

    async def process(self, data: Ticker, timestamp: float) -> bool:
        """
        Records the data from the crypto feed into the dataset.

        :param data: The data from the exchange.
        :param timestamp: The time of the request.
        """

        exchange = data.exchange.lower()
        symbol = adjust_symbol(symbol=data.symbol)

        return await record_orders(
            screeners=self.find_screeners(
                base=OrdersScreener, exchange=exchange, symbol=symbol
            ), data=data, timestamp=timestamp, callbacks=self.callbacks
        )
    # end process
# end MarketOrdersRecorder

class OrdersMarketScreener(MarketScreener):
    """
    A class to represent an asset price screener.

    Using this class, you can create a screener object to
    screen the market ask and bid data for a specific asset in
    a specific exchange at real time.

    Parameters:

    - location:
        The saving location for the saved data of the screener.

    - cancel:
        The time to cancel screening process after no new data is fetched.

    - delay:
        The delay to wait between each data fetching.

    - handler:
        The handler object to handle the data feed.

    - recorder:
        The recorder object to record the data of the market from the feed.

    - screeners:
        The screener object to control and fill with data.

    - refresh:
        The duration of time between each refresh. 0 means no refresh.

    - amount:
        The amount of symbols for each symbols group for an exchange.

    - limited:
        The value to limit the running screeners to active exchanges.

    >>> from crypto_screening.market.screeners import orders_market_screener
    >>>
    >>> structure = {'binance': ['BTC/USDT'], 'bittrex': ['ETH/USDT']}
    >>>
    >>> screener = orders_market_screener(data=structure)
    >>> screener.run()
    """

    screeners: List[OrdersScreener]
    recorder: OrdersMarketRecorder

    COLUMNS = OrdersMarketRecorder.COLUMNS

    def __init__(
            self,
            recorder: OrdersMarketRecorder,
            screeners: Optional[Iterable[OrdersScreener]] = None,
            location: Optional[str] = None,
            cancel: Optional[Union[float, dt.timedelta]] = None,
            delay: Optional[Union[float, dt.timedelta]] = None,
            refresh: Optional[Union[float, dt.timedelta, bool]] = None,
            limited: Optional[bool] = None,
            handler: Optional[MarketHandler] = None,
            amount: Optional[int] = None
    ) -> None:
        """
        Creates the class attributes.

        :param location: The saving location for the data.
        :param delay: The delay for the process.
        :param cancel: The cancel time for the loops.
        :param limited: The value to limit the screeners to active only.
        :param refresh: The refresh time for rerunning.
        :param handler: The handler object for the market data.
        :param amount: The maximum amount of symbols for each feed.
        :param recorder: The recorder object for recording the data.
        """

        super().__init__(
            location=location, cancel=cancel,
            delay=delay, recorder=recorder,
            screeners=screeners, handler=handler, limited=limited,
            amount=amount, refresh=refresh
        )
    # end __init__

    @property
    def orders_screeners(self) -> List[OrdersScreener]:
        """
        Returns a list of all the order-book screeners.

        :return: The order-book screeners.
        """

        return self.find_screeners(base=OrdersScreener)
    # end orders_screeners
# end MarketOrderbookScreener

def create_orders_screeners(
        data: Dict[str, Iterable[str]],
        location: Optional[str] = None,
        cancel: Optional[Union[float, dt.timedelta]] = None,
        delay: Optional[Union[float, dt.timedelta]] = None,
) -> List[OrdersScreener]:
    """
    Defines the class attributes.

    :param data: The data for the screeners.
    :param location: The saving location for the data.
    :param cancel: The time to cancel the waiting.
    :param delay: The delay for the process.
    """

    screeners = []

    for exchange, symbols in data.items():
        for symbol in symbols:
            screeners.append(
                OrdersScreener(
                    symbol=symbol, exchange=exchange, delay=delay,
                    location=location, cancel=cancel
                )
            )
        # end for
    # end for

    return screeners
# end create_orders_screeners

def orders_market_screener(
        data: Dict[str, Iterable[str]],
        location: Optional[str] = None,
        cancel: Optional[Union[float, dt.timedelta]] = None,
        delay: Optional[Union[float, dt.timedelta]] = None,
        limited: Optional[bool] = None,
        handler: Optional[MarketHandler] = None,
        amount: Optional[int] = None,
        callbacks: Optional[Iterable[BaseCallback]] = None,
        refresh: Optional[Union[float, dt.timedelta, bool]] = None,
        recorder: Optional[OrdersMarketRecorder] = None
) -> OrdersMarketScreener:
    """
    Creates the market screener object for the data.

    :param data: The market data.
    :param handler: The handler object for the market data.
    :param limited: The value to limit the screeners to active only.
    :param refresh: The refresh time for rerunning.
    :param amount: The maximum amount of symbols for each feed.
    :param recorder: The recorder object for recording the data.
    :param location: The saving location for the data.
    :param delay: The delay for the process.
    :param cancel: The cancel time for the loops.
    :param callbacks: The callbacks for the service.

    :return: The market screener object.
    """

    screeners = create_orders_screeners(
        data=data, location=location,
        cancel=cancel, delay=delay
    )

    return OrdersMarketScreener(
        recorder=recorder or OrdersMarketRecorder(
            screeners=screeners, callbacks=callbacks
        ), screeners=screeners,
        handler=handler, location=location, amount=amount,
        cancel=cancel, delay=delay, limited=limited, refresh=refresh
    )
# end orders_market_screener