from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from functools import wraps
from typing import Any

from beni.bfunc import crcData, getWrapped, toAny
from beni.btype import AsyncFunc, AsyncFuncType


def cache(func: AsyncFuncType) -> AsyncFuncType:
    @wraps(func)
    async def wraper(*args: Any, **kwargs: Any):
        baseFunc = getWrapped(func)
        cacheData = _cacheFuncDict.get(baseFunc)
        if not cacheData:
            cacheData = _CacheFuncData()
            _cacheFuncDict[baseFunc] = cacheData
        key = (args, kwargs)
        while True:
            result = cacheData.get(key)
            if result is not None:
                return result
            async with cacheData.lock():
                result = await func(*args, **kwargs)
                cacheData.set(key, result)
                return result

    return toAny(wraper)


def clearCache(func: AsyncFunc):
    baseFunc = getWrapped(func)
    if baseFunc in _cacheFuncDict:
        del _cacheFuncDict[baseFunc]


_cacheFuncDict: dict[AsyncFunc, _CacheFuncData] = {}
_CacheKey = tuple[tuple[Any, ...], dict[str, Any]]


class _CacheFuncData:

    def __init__(self) -> None:
        self.event = asyncio.Event()
        self.running = False
        self._results: dict[str, Any] = {}

    def get(self, key: _CacheKey):
        return self._results.get(crcData(key))

    def set(self, key: _CacheKey, result: Any):
        self._results[crcData(key)] = result

    @asynccontextmanager
    async def lock(self):
        if self.running:
            await self.event.wait()
        self.running = True
        try:
            yield
        finally:
            self.running = False
            self.event.set()
            self.event.clear()
