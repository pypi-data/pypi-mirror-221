from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import *
from collections import deque
import itertools
import functools
from typing import Callable, Iterable

T = TypeVar('T')
R = TypeVar('R')
K = TypeVar('K')
V = TypeVar('V')

class Iter(Iterable[T], Generic[T]):
    """
    Iterable class, which can be used as an iterator.
    """
    _iter: Iterable[T] = None

    def __init__(self, iterator: Iterable[T]) -> None:
        self._iter = iterator
    
    def __iter__(self):
        return self._iter.__iter__()
    
    def __next__(self) -> T:
        return self.__iter__().__next__()

    def filter(self, predicate: Callable[[T], bool]) -> Iter[T]:
        return IterFilter(self, predicate)
    
    def map(self, func: Callable[[T], R]) -> Iter[R]:
        return IterMap(self, func)
    
    def first(self) -> Optional[T]:
        try:
            return next(self)
        except StopIteration:
            return None

    def flatten(self: Iter[Iter[R]]) -> Iter[R]:
        return Iter[R](itertools.chain.from_iterable(self))
    
    def reduce(self, f: Callable[[R, T], R], initial: Optional[R] = None) -> R:
        return functools.reduce(f, self, self.first() if initial is None else initial)
    
    def for_each(self, f: Callable[[T], None]) -> None:
        for item in self:
            f(item)
    
    def skip(self, n: int) -> Iter[T]:
        return IterSlice(self, n, None)
    
    def take(self, n: int) -> Iter[T]:
        return IterSlice(self, None, n)
    
    def slice(self, start: int, end: int) -> Iter[T]:
        return IterSlice(self, start, end)
    
    def nth(self, n: int) -> Optional[T]:
        return self.skip(n).first()
    
    def enumerate(self, start: int = 0) -> Iter[tuple[int, T]]:
        return Iter(enumerate(self, start))

    def groupby(self, key: Callable[[T], R]) -> Iter[tuple[R, Iter[T]]]:
        """
        Groupby on keys

        Note: Consumes entire iterator to create groups -> Holds dictionary of groups
        """
        return IterGroupby(self, key)
    
    def groupby_agg(self, key: Callable[[T], R]):
        """
        Groupby on consecutive keys

        Note: Does not consume iterator
        """
        return Iter(itertools.groupby(self, key)).map(lambda pair: (pair[0], Iter(pair[1])))

    def batch(self, n: int):
        return self.enumerate() \
            .groupby_agg(lambda x: x[0] // n) \
            .map(lambda x: x[1].map(lambda y: y[1]))
    
    def concat(self, other: Iterable[T]) -> Iter[T]:
        return Iter(itertools.chain(self, other))
    
    def count(self) -> int:
        return sum(1 for _ in self)
    
    def pairwise(self) -> Iter[tuple[T, T]]:
        return Iter(itertools.pairwise(self))

    def to_list(self) -> SList[T]:
        return SList(self)
    def to_dict(self, f: Callable[[T], tuple[K, V]]) -> SDict[K, V]:
        return SDict[K, V](self.map(f))
    def to_collection(self):
        return IterCollection(self.to_list())
    def collect(self, call: Callable[[Iterable], R]) -> R:
        return call(self)
    
    def thread_map(self, func: Callable[[T], R], threadpool_factory: Optional[Callable[[], ThreadPoolExecutor]] = None) -> Iter[R]:
        """
        WIP: map with automatic threading
        """
        return AsyncIter(self, func, threadpool_factory)

class IterCollection(Iter[T], Generic[T]):
    _collection = None

    def __init__(self, data: Collection[T]) -> None:
        if not isinstance(data, Collection):
            raise TypeError("iterator must be Collection!")
        self._collection = data
        super().__init__(self._collection)
    
    def __len__(self) -> int:
        return self._collection.__len__()
    
    def len(self) -> int:
        return self.__len__()
    
    def __getitem__(self, index: int) -> T:
        return self._collection.__getitem__(index)
    
    def __setitem__(self, index: int, value: T) -> None:
        return self._collection.__setitem__(index, value)
    
    def __reversed__(self) -> Iter[T]:
        return Iter(reversed(self._collection))
    
    def reversed(self) -> Iter[T]:
        return self.__reversed__()

class SQueue(deque[T], IterCollection[T]):
    def __init__(self, iterator: Optional[Iterable[T]] = None) -> None:
        super().__init__(iterator)

class IterMap(Iter[T], Generic[T, R]):

    def __init__(self, iterator: Iterable[T], f: Callable[[T], R]) -> None:
        super().__init__(iterator)
        self.func = f
    
    def __iter__(self):
        return map(self.func, self._iter)
    
class IterFilter(Iter[T], Generic[T]):
    def __init__(self, iterator: Iterable[T], predicate: Callable[[T], bool]) -> None:
        super().__init__(iterator)
        self.func = predicate
    
    def __iter__(self):
        return filter(self.func, self._iter)

class IterSlice(Iter[T], Generic[T]):
    def __init__(self, iterator: Iterable[T], start: int, end: int) -> None:
        super().__init__(iterator)
        self.start = start
        self.end = end
    
    def __iter__(self):
        return itertools.islice(self._iter, self.start, self.end)

def consuming_groupby(iterable: Iter[T], key: Callable[[T], R]) -> Iter[tuple[R, SQueue[T]]]:
    def append_or_create(r: SDict[R, SQueue[T]], k: R, item: T) -> SDict[R, SQueue[T]]:
        if k not in r:
            r[k] = SQueue([])
        r[k].append(item)
        return r
    
    return iterable \
        .reduce((lambda state, x: append_or_create(state, key(x), x)), SDict()) \
        .items() \
        .map(lambda kv: [kv[0], kv[1]])

class IterGroupby(Iter[T], Generic[T, R]):
    def __init__(self, iterator: Iterable[T], key: Callable[[T], R]) -> None:
        super().__init__(iterator)
        self.key = key
    
    def __iter__(self):
        return consuming_groupby(self._iter, self.key)

class SList(list[T], IterCollection[T], Generic[T]):
    """
    Smart list, which can be used as an iterator.
    """
    def iter(self) -> Iter[T]:
        return Iter(self)
    def append(self, item: T) -> SList[T]:
        super().append(item)
        return self
    
class SDict(dict[K, V], IterCollection[K], Generic[K, V]):
    """
    Smart dict, which can be used as an iterator.
    """
    def iter(self) -> Iter[T]:
        return Iter(iter(super().keys()))
    def keys(self) -> Iter[K]:
        return Iter(iter(super().keys()))
    def values(self) -> Iter[V]:
        return Iter(iter(super().values()))
    def items(self) -> Iter[tuple[K, V]]:
        return Iter(iter(super().items()))

class AsyncIter(Iter[T]):
    def __init__(self, iterator: Iterable[T], func:Callable[[T], R], threadpool_factory: Optional[Callable[[], ThreadPoolExecutor]] = None) -> None:
        super().__init__(iterator)
        self.func = func
        self.factory = lambda: ThreadPoolExecutor()
    
    def __iter__(self) -> AsyncIter[R]:
        with self.factory() as _pool:
            _r = Iter(_pool.map(self.func, self._iter))
        return Iter(_r)