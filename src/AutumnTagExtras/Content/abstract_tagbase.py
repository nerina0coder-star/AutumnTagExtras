from abc import ABC
from typing import Any

from Autumn import current_base
from Autumn.Tag.abstract_tag import AbstractTag


@current_base.ctrl
class AbstractTagBase(AbstractTag, ABC):
    """
    The base class for all content tags.
    """

    def build(self, cache_if_possible: bool = True, **kwargs: Any) -> str:
        return super().build(cache_if_possible, **kwargs)