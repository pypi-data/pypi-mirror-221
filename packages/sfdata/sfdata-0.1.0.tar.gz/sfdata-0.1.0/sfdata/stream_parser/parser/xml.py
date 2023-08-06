from typing import Generator

from lxml import etree

from sfdata.stream_parser.events import (
    CommentNode,
    EndNode,
    EndTree,
    ParseEvent,
    ProcessingInstructionNode,
    StartNode,
    StartTree,
    Value,
)


def format_path(path: list[str]):
    return "/".join(path)


def dom_parse(source, **kwargs) -> Generator[ParseEvent, None, None]:
    """
    Equivalent of the xml parse included in the sfdata.stream_parser package, but uses the ET DOM
    and allows direct DOM manipulation.
    """
    parser = etree.iterparse(source, events=("start", "end", "comment", "pi"), **kwargs)

    yield StartTree(url=source)
    for action, elem in parser:
        if action == "start":
            yield StartNode(tag=elem.tag, attrib=elem.attrib, node=elem)
            if elem.text and elem.text.strip():
                yield Value(value=elem.text)
        elif action == "end":
            yield EndNode(tag=elem.tag, node=elem)
            if elem.tail and elem.tail.strip():
                yield Value(value=elem.tail)
        elif action == "comment":
            yield CommentNode(text=elem.text, node=elem)
        elif action == "pi":
            yield ProcessingInstructionNode(name=elem.target, text=elem.text, node=elem)
        else:
            yield ValueError(f"Unknown event: {action}")
    yield EndTree(url=source)
