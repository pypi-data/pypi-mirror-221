from lxml import etree

from sfdata_stream_old.events import (
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


def dom_parse(source, **kwargs) -> list[ParseEvent]:
    """
    Equivalent of the xml parse included in the sfdata.stream_parser package, but uses the ET DOM
    and allows direct DOM manipulation.
    """
    parser = etree.iterparse(source, events=("start", "end", "comment", "pi"), **kwargs)

    yield StartTree(url=source)
    path = []
    for action, elem in parser:
        if action == "start":
            path.append(elem.tag)

            yield StartNode(
                tag=elem.tag, attrib=elem.attrib, node=elem, path=format_path(path)
            )
            if elem.text and elem.text.strip():
                yield Value(value=elem.text, path=format_path(path))
        elif action == "end":
            path.pop(-1)
            yield EndNode(tag=elem.tag, node=elem)
            if elem.tail and elem.tail.strip():
                yield Value(value=elem.tail, path=format_path(path))
        elif action == "comment":
            yield CommentNode(text=elem.text, node=elem)
        elif action == "pi":
            yield ProcessingInstructionNode(name=elem.target, text=elem.text, node=elem)
        else:
            yield ValueError(f"Unknown event: {action}")
    yield EndTree(url=source)
