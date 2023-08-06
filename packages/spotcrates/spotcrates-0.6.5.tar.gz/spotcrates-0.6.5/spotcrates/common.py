import logging
from abc import ABC, abstractmethod
from itertools import islice
from typing import Iterable, Dict, Any

from pygtrie import CharTrie

from spotipy import Spotify


class NotFoundException(Exception):
    pass


def batched(iterable: Iterable, n: int):
    """Batch data into lists of length n. The last batch may be shorter."""
    # batched('ABCDEFG', 3) --> ABC DEF G
    it = iter(iterable)
    while True:
        batch = list(islice(it, n))
        if not batch:
            return
        yield batch


def get_all_items(spotify: Spotify, first_page: Dict[str, Any]):
    """Collects the 'items' contents from every page in the given result set."""
    all_items = []

    all_items.extend(first_page["items"])

    try:
        next_page = spotify.next(first_page)
        while next_page:
            all_items.extend(next_page["items"])
            next_page = spotify.next(next_page)
    except Exception:
        logging.warning("Problems paging given Spotify items list", exc_info=True)

    return [item for item in all_items if item is not None]


def truncate_long_value(full_value: str, length: int, trim_tail: bool = True) -> str:
    """Returns the given value truncated from the start of the value so that it is at most the given length.

    :param full_value: The value to trim.
    :param length: The maximum length of the returned value.
    :param trim_tail: Whether to trim from the head or tail of the string.
    :return: The value trimmed from the start of the string to be at most the given length.
    """
    if not full_value:
        return full_value

    if len(full_value) > length:
        if trim_tail:
            return full_value[:length]
        else:
            return full_value[-length:]
    return full_value


class BaseLookup(ABC):
    def __init__(self):
        """Uses a trie to find the longest matching prefix for the given lookup value"""
        self.logger = logging.getLogger(__name__)
        self.lookup = self._init_lookup()

    def find(self, lookup_val):
        if not lookup_val:
            raise NotFoundException(f"Blank/null lookup value {lookup_val}")

        found_command = self.lookup.longest_prefix(lookup_val)

        if found_command:
            self.logger.debug(
                "Got %s (%s) for %s", found_command.value, found_command.key, lookup_val
            )
            return found_command.value
        else:
            raise NotFoundException(f"No value for {lookup_val}")

    @abstractmethod
    def _init_lookup(self) -> CharTrie:
        pass
