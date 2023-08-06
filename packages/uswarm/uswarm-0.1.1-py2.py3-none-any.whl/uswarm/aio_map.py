import asyncio
from collections import deque
from typing import Any, Callable, Collection, AsyncIterator, Iterator, Union


async def _next(gg):
    # repackaging non-asyncio next() as async-like anext()
    try:
        return next(gg)
    except StopIteration:
        raise StopAsyncIteration


async def _aionext(gg):
    # there is no anext() :(
    return await gg.__anext__()


async def map_unordered(
    fn: Callable,
    args: Union[Iterator, Collection, AsyncIterator],
    maxsize=None,
    grace=0.001,
    as_task=False,
):
    """
    Async generator yielding return values of resolved invocations
    of `fn` against arg in args list

    Arguments are consumed and fed to callable in the order they are presented in args.
    Results are yielded NOT in order of args. Earliest done is yielded.

    If `size` is specified, worker tasks pool is constrained to that size.

    This is asyncio equivalent of Gevent's `imap_unordered(fn, args_iterable, pool_size)`
    http://www.gevent.org/api/gevent.pool.html#gevent.pool.Group.imap_unordered

    Note that args can be both, an async generator and a non-async iterator/generator.
    You can chain `map_unordered` as `args` param for another `map_unordered`

    Because this is an async generator, cannot consume it as regular iterable.
    Must use `async for`.

    Usage example:

            # note NO await in this assignment
            gen = map_unordered(fn, arguments_iter, maxsize=3)
            async for returned_value in gen:
                yield returned_value

    """
    if maxsize == 0:
        raise ValueError(
            "Argument `maxsize` cannot be set to zero. "
            "Use `None` to indicate no limit."
        )

    # Make args list consumable like a generator
    # so repeated islice(args, size) calls against `args` move slice down the list.

    if hasattr(args, "__anext__"):
        n = _aionext
    elif hasattr(args, "__next__"):
        n = _next
    else:
        args = iter(args)
        n = _next

    have_args = True  # assumed. Don't len(args).
    pending_tasks = deque()

    while have_args or len(pending_tasks):
        try:
            while len(pending_tasks) < maxsize:
                arg = await n(args)
                task = asyncio.Task(fn(arg))
                task.arg = arg
                pending_tasks.append(task)
                asyncio.sleep(grace)
        except StopAsyncIteration:
            have_args = False

        if not len(pending_tasks):
            return

        done, pending_tasks = await asyncio.wait(
            pending_tasks, return_when=asyncio.FIRST_COMPLETED
        )
        pending_tasks = deque(pending_tasks)

        for task in done:
            if as_task:
                yield task
            else:
                yield await task  # await converts task object into its return value

        asyncio.sleep(grace)


async def _filter_wrapper(fn, arg):
    return (await fn(arg)), arg


async def _filter_none(arg):
    return not (arg is None)


async def filter_unordered(
    fn: Union[Callable, None],
    args: Union[Iterator, Collection, AsyncIterator],
    maxsize=None,
):
    """
    Async filter generator yielding values of `args` collection that match filter condition.
    Like python's native `filter([Callable|None], iterable)` but:
    - allows iterable to be async iterator
    - allows callable to be async callable
    - returns results OUT OF ORDER - whichever passes filter test first.

    Arguments are consumed and fed to callable in the order they are presented in args.
    Results are yielded NOT in order of args. Earliest done and passing the filter condition is yielded.

    If `maxsize` is specified, worker tasks pool is constrained to that size.

    This is inspired by Gevent's `imap_unordered(fn, args_iterable, pool_size)`
    http://www.gevent.org/api/gevent.pool.html#gevent.pool.Group.imap_unordered

    Because this is an async generator, cannot consume it as regular iterable.
    Must use `async for`.

    Usage example:

            # note NO await in this assignment
            gen = filter_unordered(fn, arguments_iter, maxsize=3)
            async for returned_value in gen:
                yield returned_value

    """
    if maxsize == 0:
        raise ValueError(
            "Argument `maxsize` cannot be set to zero. "
            "Use `None` to indicate no limit."
        )

    if hasattr(args, "__anext__"):
        n = _aionext
    elif hasattr(args, "__next__"):
        n = _next
    else:
        args = iter(args)
        n = _next

    if fn is None:
        fn = _filter_none

    have_args = True  # assumed. Don't len(args).
    pending_tasks = deque()

    while have_args or len(pending_tasks):
        try:
            while len(pending_tasks) != maxsize:
                arg = await n(args)
                pending_tasks.append(asyncio.Task(_filter_wrapper(fn, arg)))
        except StopAsyncIteration:
            have_args = False

        if not len(pending_tasks):
            return

        done, pending_tasks = await asyncio.wait(
            pending_tasks, return_when=asyncio.FIRST_COMPLETED
        )
        pending_tasks = deque(pending_tasks)

        for task in done:
            filter_match, arg = await task
            if filter_match:
                yield arg
