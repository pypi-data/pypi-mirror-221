import logging
from typing import Literal
from uuid import uuid4

from sfdata.converter import convert_types
from sfdata.exporter import populate_databook
from sfdata.identifier import identify_fields
from sfdata.settings import setup_logger
from sfdata.util import context_to_path
from sfdata.schema.models import Schema, Field, Record
from sfdata.stream_parser.events import Value, StartNode
from sfdata.stream_parser.filters.context import add_context, generator_with_value
from sfdata.stream_parser.parser.xml import dom_parse
from xsdata.models.enums import DataType

setup_logger()
logger = logging.getLogger(__name__)


def filter_values(stream):
    """yield just Value events that where recognized by the schema"""
    for event in stream:
        if isinstance(event, Value) and getattr(event, "entry_id", None):
            yield event


@generator_with_value
def set_primary_keys(stream, pk_fields: tuple[tuple[Field, Record]]):
    found_field = False
    primary_keys = {}
    for event in stream:
        if not isinstance(event, StartNode):
            yield event
            continue
        path = context_to_path(event.context)
        for field, record in pk_fields:
            if path == field.path:
                # primary_key exists already
                value_event = next(stream)
                primary_keys[f"{record.name}.{field.name}"] = value_event.value
                yield value_event
                break

            parent_path = "/".join(field.path.split("/")[:-1])
            if path == parent_path:
                found_field = True
                yield event
                if field.generator is None:
                    continue
                if field.generator == "uuid":
                    value = str(uuid4())
                    primary_keys[f"{record.name}.{field.name}"] = value
                    yield Value(
                        type=DataType.from_code("str"),
                        field_id=field.pk,
                        field_name=field.name,
                        record_name=record.name,
                        entry_id=event.entry_id,
                        value=value,
                    )
                    break
                else:
                    raise Exception("Currently only accepting 'uuid' generators")
        if not found_field:
            yield event
    return primary_keys


def demo_stuff(stream):
    for event in stream:
        context = getattr(event, "context", ())
        if context and context[-1] == "ReferralSource":
            print(event)
        yield event


def standardise(schema: Schema, file, output: Literal["dataframes", "databook"]):
    logger.info(f"starting standardisation for file {file} and schema {schema}")

    stream = dom_parse(file)
    stream = add_context(stream)
    stream = identify_fields(stream, schema)
    stream = convert_types(stream)
    primary_keys, stream = set_primary_keys(stream, pk_fields=schema.primary_keys)
    # print(primary_keys)
    # stream = set_foreign_keys(stream, pk_fields=schema.foreign_keys)
    # stream = demo_stuff(stream)
    stream = filter_values(stream)
    book = populate_databook(stream, primary_keys, schema)
    logger.info(f"finished standardisation for file {file} and schema {schema}")

    if output == "dataframes":
        return {sheet.title: sheet.export("df") for sheet in book.sheets()}
    elif output == "databook":
        return book
    return
