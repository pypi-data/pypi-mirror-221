from itertools import chain
from typing import List, Any, Iterable


def flatten(lst: Iterable[List[Any]]) -> List[Any]:
    return list(chain.from_iterable(lst))
