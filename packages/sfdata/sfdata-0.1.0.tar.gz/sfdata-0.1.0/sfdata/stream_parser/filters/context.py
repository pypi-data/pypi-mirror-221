import logging
from typing import List

import functools
from sfdata.stream_parser import events
from sfdata.stream_parser.filters.generic import streamfilter

log = logging.getLogger(__name__)


@streamfilter(default_args=lambda: {"context": []})
def add_context(event, context: List[str]):
    """
    Adds 'context' to XML structures. For each :class:`sfdata.stream_parser.events.StartNode` the tag name is
    added to a 'context' tuple, and for each :class:`sfdata.stream_parser.events.EndNode` the context is popped.

    For all other events, the context tuple is set as-is.

    Provides: context
    """
    if isinstance(event, events.StartNode):
        context.append(event.tag)
        local_context = tuple(context)
    elif isinstance(event, events.EndNode):
        local_context = tuple(context)
        context.pop()
    else:
        local_context = tuple(context)

    return event.from_event(event, context=local_context)


class GeneratorReturnValueHolder:
    def __init__(self, stream):
        self.stream = stream
        self._value = None
        self._consumed = False

    def __iter__(self):
        self._value = yield from self.stream
        self._consumed = True

    def __next__(self):
        try:
            return next(self._value)
        except StopIteration as e:
            self._consumed = True
            self._value = e.value
            raise e

    @property
    def value(self):
        if not self._consumed:
            raise RuntimeError("Generator has not been consumed")
        return self._value


def generator_with_value(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return_value = GeneratorReturnValueHolder(func(*args, **kwargs))
        return return_value, iter(return_value)

    return wrapper
