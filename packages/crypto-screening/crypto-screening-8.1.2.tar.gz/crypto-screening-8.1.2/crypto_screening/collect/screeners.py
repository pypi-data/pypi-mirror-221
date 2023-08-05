# screeners.py

from typing import (
    Optional, Dict, Iterable,
    Set, Union, Tuple, List
)

import pandas as pd
from attrs import define

from crypto_screening.symbols import symbol_to_pair, symbol_to_parts
from crypto_screening.collect.symbols import (
    matching_symbol_pair, MarketSymbolSignature,
    exchanges_symbols
)
from crypto_screening.market.screeners.base import (
    BaseScreener, BaseMarketScreener
)

__all__ = [
    "matching_screener_signatures",
    "matching_screener_pair",
    "matching_screener_pairs",
    "MarketScreenerSignature",
    "find_screeners",
    "structure_screeners",
    "live_nonempty_screeners",
    "remove_empty_screeners",
    "screeners_exchanges_symbols",
    "structure_exchanges_symbols_screeners",
    "structure_exchanges_symbols_screener",
    "gather_screeners",
    "exchanges_symbols_screeners",
    "screeners_to_multiple_symbols_screeners",
    "screeners_to_assets_screeners",
    "screeners_to_symbols_screeners",
    "screeners_to_multiple_assets_screeners",
    "screeners_to_multiple_assets_datasets",
    "screeners_to_multiple_symbols_datasets",
    "nonempty_screeners"
]

AssetMatches = Iterable[Iterable[str]]

def matching_screener_pair(
        screener1: BaseScreener,
        screener2: BaseScreener, /, *,
        matches: Optional[AssetMatches] = None,
        separator: Optional[str] = None
) -> bool:
    """
    Checks if the symbols are valid with the matching currencies.

    :param screener1: The first ticker.
    :param screener2: The second ticker.
    :param matches: The currencies.
    :param separator: The separator of the assets.

    :return: The validation value for the symbols.
    """

    return (
        (screener1.exchange != screener2.exchange) and
        matching_symbol_pair(
            screener1.symbol, screener2.symbol,
            matches=matches, separator=separator
        )
    )
# end matching_screener_pair

ExchangesAssetMatches = Union[Dict[Iterable[str], AssetMatches], AssetMatches]

def matching_screener_pairs(
        screeners: Iterable[BaseScreener],
        matches: Optional[ExchangesAssetMatches] = None,
        separator: Optional[str] = None,
        empty: Optional[bool] = True
) -> Set[Tuple[BaseScreener, BaseScreener]]:
    """
    Checks if the screeners are valid with the matching currencies.

    :param screeners: The screeners.
    :param matches: The currencies.
    :param separator: The separator of the assets.
    :param empty: Allows empty screeners.

    :return: The validation value for the symbols.
    """

    pairs: List[Tuple[BaseScreener, BaseScreener]] = []

    if not empty:
        screeners = remove_empty_screeners(screeners=screeners)
    # end if

    for screener1 in screeners:
        for screener2 in screeners:
            exchanges_matches = (
                matches
                if not isinstance(matches, dict) else
                [
                    *matches.get(screener1.exchange, []),
                    *matches.get(screener2.exchange, [])
                ]
            )

            if matching_screener_pair(
                screener1, screener2,
                matches=exchanges_matches or None,
                separator=separator
            ):
                pairs.append((screener1, screener2))
            # end if
        # end for
    # end for

    return set(pairs)
# end matching_screener_pairs

@define(repr=False, unsafe_hash=True)
class MarketScreenerSignature(MarketSymbolSignature):
    """A class to represent the data for the execution of a trade."""

    screener: Optional[BaseScreener] = None
# end MarketScreenerSignature

def matching_screener_signatures(
        data: Optional[Set[Tuple[BaseScreener, BaseScreener]]] = None,
        screeners: Optional[Iterable[BaseScreener]] = None,
        matches: Optional[ExchangesAssetMatches] = None,
        separator: Optional[str] = None,
        empty: Optional[bool] = True
) -> Set[Tuple[MarketScreenerSignature, MarketScreenerSignature]]:
    """
    Checks if the screeners are valid with the matching currencies.

    :param data: The data for the pairs.
    :param screeners: The screeners.
    :param matches: The currencies.
    :param separator: The separator of the assets.
    :param empty: Allows empty screeners.

    :return: The validation value for the symbols.
    """

    if (data is None) and (screeners is None):
        raise ValueError(
            f"One of 'screeners' and 'data' parameters must be given, "
            f"when 'data' is superior to 'screeners'."
        )

    elif (not screeners) and (not data):
        return set()
    # end if

    pairs: List[Tuple[MarketScreenerSignature, MarketScreenerSignature]] = []

    data = data or matching_screener_pairs(
        screeners=screeners, matches=matches,
        separator=separator, empty=empty
    )

    for screener1, screener2 in data:
        currency1 = symbol_to_pair(screener1.symbol).quote
        currency2 = symbol_to_pair(screener2.symbol).quote

        pairs.append(
            (
                MarketScreenerSignature(
                    asset=currency1, currency=currency1,
                    exchange=screener1.exchange,
                    screener=screener1
                ),
                MarketScreenerSignature(
                    asset=currency2, currency=currency2,
                    exchange=screener2.exchange,
                    screener=screener2
                )
            )
        )
    # end for

    return set(pairs)
# end matching_screener_signatures

def nonempty_screeners(
        screeners: Iterable[Union[BaseScreener, BaseMarketScreener]]
) -> Set[Union[BaseScreener, BaseMarketScreener]]:
    """
    Returns a list of all the live create_screeners.

    :param screeners: The create_screeners to search from.

    :return: A list the live create_screeners.
    """

    return {
        screener for screener in screeners
        if (
            (
                isinstance(screener, BaseMarketScreener) and
                nonempty_screeners(screener.screeners)
            ) or
            (
                (len(screener.market) > 0) and
                isinstance(screener, BaseScreener)
            )
        )
    }
# end nonempty_screeners

def live_nonempty_screeners(
        screeners: Iterable[Union[BaseScreener, BaseMarketScreener]]
) -> Set[Union[BaseScreener, BaseMarketScreener]]:
    """
    Returns a list of all the live create_screeners.

    :param screeners: The create_screeners to search from.

    :return: A list the live create_screeners.
    """

    return {
        screener for screener in screeners
        if (
            (
                isinstance(screener, BaseMarketScreener) and
                live_nonempty_screeners(screener.screeners)
            ) or
            (
                screener.screening and
                (len(screener.market) > 0) and
                isinstance(screener, BaseScreener)
            )
        )
    }
# end live_nonempty_screeners

def structure_screeners(
        screeners: Iterable[BaseScreener]
) -> Dict[str, Dict[str, List[BaseScreener]]]:
    """
    Structures the screener objects by exchanges and symbols

    :param screeners: The screeners to structure.

    :return: The structure of the screeners.
    """

    structure: Dict[str, Dict[str, List[BaseScreener]]] = {}

    for screener in screeners:
        (
            structure.
            setdefault(screener.exchange, {}).
            setdefault(screener.symbol, [])
        ).append(screener)
    # end for

    return structure
# end structure_screeners

def find_screeners(
        screeners: Iterable[BaseScreener],
        exchange: Optional[str] = None,
        symbol: Optional[str] = None
) -> List[BaseScreener]:
    """
    Finds all the screeners with the matching exchange and symbol key.

    :param screeners: The screeners to process.
    :param exchange: The exchange key for the symbol.
    :param symbol: The pair symbol to search its screeners.

    :return: The matching screeners.
    """

    return [
        screener for screener in screeners
        if (
            ((symbol is None) or (screener.symbol.lower() == symbol.lower())) and
            ((exchange is None) or (exchange.lower() == screener.exchange.lower()))
        )
    ]
# end find_screeners

def remove_empty_screeners(screeners: Iterable[BaseScreener]) -> List[BaseScreener]:
    """
    Removes the empty screeners.

    :param screeners: The screeners of the assets and exchanges.
    """

    return [
        screener for screener in screeners
        if len(screener.market) > 0
    ]
# end remove_empty_screeners

def screeners_exchanges_symbols(screeners: Iterable[BaseScreener]) -> Dict[str, Set[str]]:
    """
    Collects the structure of the screeners exchanges and symbols.

    :param screeners: The screeners to process.

    :return: The collected structure of exchanges and symbols.
    """

    data: Dict[str, Set[str]] = {}

    for screener in screeners:
        data.setdefault(screener.exchange, set()).add(screener.symbol)
    # end for

    return {
        exchange: symbols
        for exchange, symbols in data.items()
        if symbols
    }
# end screeners_exchanges_symbols

def structure_exchanges_symbols_screeners(
        screeners: Iterable[BaseScreener]
) -> Dict[str, Dict[str, List[BaseScreener]]]:
    """
    Structures the screener objects by exchanges and symbols

    :param screeners: The screeners to structure.

    :return: The structure of the screeners.
    """

    structure: Dict[str, Dict[str, List[BaseScreener]]] = {}

    for screener in screeners:
        (
            structure.
            setdefault(screener.exchange, {}).
            setdefault(screener.symbol, [])
        ).append(screener)
    # end for

    return structure
# end structure_exchanges_symbols_screeners

def structure_exchanges_symbols_screener(
        screeners: Iterable[BaseScreener]
) -> Dict[str, Dict[str, BaseScreener]]:
    """
    Structures the screener objects by exchanges and symbols

    :param screeners: The screeners to structure.

    :return: The structure of the screeners.
    """

    structure: Dict[str, Dict[str, BaseScreener]] = {}

    for screener in screeners:
        (
            structure.
            setdefault(screener.exchange, {}).
            setdefault(screener.symbol, screener)
        )
    # end for

    return structure
# end structure_exchanges_symbols_screener

def gather_screeners(
        screeners: Iterable[Union[BaseScreener, BaseMarketScreener]]
) -> List[BaseScreener]:
    """
    Gathers the base screeners.

    :param screeners: The screeners to process.

    :return: The gathered base screeners.
    """

    checked_screeners: List[BaseScreener] = []

    for screener in screeners:
        if isinstance(screener, BaseScreener):
            checked_screeners.append(screener)

        elif isinstance(screener, BaseMarketScreener):
            checked_screeners.extend(screener.screeners)
        # end if
    # end for

    return checked_screeners
# end gather_screeners

def exchanges_symbols_screeners(
        screeners: Iterable[BaseScreener],
        exchanges: Optional[Iterable[str]] = None,
        adjust: Optional[bool] = True,
        separator: Optional[str] = None,
        bases: Optional[Union[Dict[str, Iterable[str]], Iterable[str]]] = None,
        quotes: Optional[Union[Dict[str, Iterable[str]], Iterable[str]]] = None,
        included: Optional[Union[Dict[str, Iterable[str]], Iterable[str]]] = None,
        excluded: Optional[Union[Dict[str, Iterable[str]], Iterable[str]]] = None
) -> List[BaseScreener]:
    """
    Collects the symbols from the exchanges.

    :param screeners: The screeners to collect.
    :param exchanges: The exchanges.
    :param quotes: The quotes of the asset pairs.
    :param excluded: The excluded symbols.
    :param adjust: The value to adjust the invalid exchanges.
    :param separator: The separator of the assets.
    :param included: The symbols to include.
    :param bases: The bases of the asset pairs.

    :return: The data of the exchanges.
    """

    if exchanges is None:
        exchanges = {screener.exchange for screener in screeners}
    # end if

    if (not screeners) or (not exchanges):
        return[]
    # end if

    found_exchanges_symbols = exchanges_symbols(
        exchanges=set(exchanges), adjust=adjust, separator=separator,
        bases=bases, quotes=quotes, included=included, excluded=excluded
    )

    return [
        screener for screener in screeners
        if (
            (screener.exchange in found_exchanges_symbols) and
            (screener.symbol in found_exchanges_symbols[screener.exchange])
        )
    ]
# end exchanges_symbols_screeners

def screeners_to_multiple_symbols_screeners(
        screeners: Iterable[BaseScreener]
) -> Dict[str, Dict[str, List[BaseScreener]]]:
    """
    Converts the datasets structure to the structure of the data rows.

    :param screeners: The screeners to process.

    :return: The new data.
    """

    results: Dict[str, Dict[str, List[BaseScreener]]] = {}

    for screener in screeners:
        (
            results.
            setdefault(screener.exchange, {}).
            setdefault(screener.symbol, []).
            append(screener)
        )
    # end for

    return results
# end symbols_datasets_to_symbols_data

def screeners_to_symbols_screeners(
        screeners: Iterable[BaseScreener]
) -> Dict[str, Dict[str, BaseScreener]]:
    """
    Converts the datasets structure to the structure of the data rows.

    :param screeners: The screeners to process.

    :return: The new data.
    """

    results: Dict[str, Dict[str, BaseScreener]] = {}

    for screener in screeners:
        (
            results.
            setdefault(screener.exchange, {}).
            setdefault(screener.symbol, screener)
        )
    # end for

    return results
# end symbols_datasets_to_symbols_data

def screeners_to_multiple_assets_screeners(
        screeners: Iterable[BaseScreener],
        separator: Optional[str] = None
) -> Dict[str, Dict[str, Dict[str, List[BaseScreener]]]]:
    """
    Converts the datasets structure to the structure of the data rows.

    :param screeners: The screeners to process.
    :param separator: The separator for the symbols.

    :return: The new data.
    """

    results: Dict[str, Dict[str, Dict[str, List[BaseScreener]]]] = {}

    for screener in screeners:
        base, quote = symbol_to_parts(screener.symbol, separator=separator)
        (
            results.
            setdefault(screener.exchange, {}).
            setdefault(base, {}).
            setdefault(quote, []).
            append(screener)
        )
    # end for

    return results
# end screeners_to_multiple_assets_screeners

def screeners_to_assets_screeners(
        screeners: Iterable[BaseScreener],
        separator: Optional[str] = None
) -> Dict[str, Dict[str, Dict[str, BaseScreener]]]:
    """
    Converts the datasets structure to the structure of the data rows.

    :param screeners: The screeners to process.
    :param separator: The separator for the symbols.

    :return: The new data.
    """

    results: Dict[str, Dict[str, Dict[str, BaseScreener]]] = {}

    for screener in screeners:
        base, quote = symbol_to_parts(screener.symbol, separator=separator)
        (
            results.
            setdefault(screener.exchange, {}).
            setdefault(base, {}).
            setdefault(quote, screener)
        )
    # end for

    return results
# end screeners_to_multiple_assets_screeners

def screeners_to_multiple_symbols_datasets(
        screeners: Iterable[BaseScreener]
) -> Dict[str, Dict[str, List[pd.DataFrame]]]:
    """
    Converts the datasets structure to the structure of the data rows.

    :param screeners: The screeners to process.

    :return: The new data.
    """

    results: Dict[str, Dict[str, List[pd.DataFrame]]] = {}

    for screener in screeners:
        (
            results.
            setdefault(screener.exchange, {}).
            setdefault(screener.symbol, []).
            append(screener.market)
        )
    # end for

    return results
# end screeners_to_multiple_symbols_datasets

def screeners_to_multiple_assets_datasets(
        screeners: Iterable[BaseScreener],
        separator: Optional[str] = None
) -> Dict[str, Dict[str, Dict[str, List[pd.DataFrame]]]]:
    """
    Converts the datasets structure to the structure of the data rows.

    :param screeners: The screeners to process.
    :param separator: The separator for the symbols.

    :return: The new data.
    """

    results: Dict[str, Dict[str, Dict[str, List[pd.DataFrame]]]] = {}

    for screener in screeners:
        base, quote = symbol_to_parts(screener.symbol, separator=separator)
        (
            results.
            setdefault(screener.exchange, {}).
            setdefault(base, {}).
            setdefault(quote, []).
            append(screener.market)
        )
    # end for

    return results
# end screeners_to_multiple_assets_datasets