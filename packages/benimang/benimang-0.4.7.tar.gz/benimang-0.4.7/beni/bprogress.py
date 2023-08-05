import asyncio
from contextlib import asynccontextmanager
from typing import Any, Coroutine, Sequence, TypeVar

from tqdm import tqdm

from beni import block


@asynccontextmanager
async def show(total: int):
    # 示例
    # async with bprogress.show(100) as update:
    #     while True:
    #         await asyncio.sleep(1)
    #         update()
    print()
    with tqdm(total=total, ncols=70) as progress:
        yield progress.update
    print()

_ReturnType = TypeVar('_ReturnType')


async def run(
    taskList: Sequence[Coroutine[Any, Any, _ReturnType]],
    itemLimit: int = 999999,
) -> Sequence[_ReturnType]:
    # 示例
    # await bprogress.run(
    #     [myfun() for _ in range(100)],
    #     10,
    # )
    print()
    with tqdm(total=len(taskList), ncols=70) as progress:
        @block.useLimit(itemLimit)
        async def task(x: Coroutine[Any, Any, _ReturnType]):
            result = await x
            progress.update()
            return result
        resultList = await asyncio.gather(*[task(x) for x in taskList])
    print()
    return resultList
