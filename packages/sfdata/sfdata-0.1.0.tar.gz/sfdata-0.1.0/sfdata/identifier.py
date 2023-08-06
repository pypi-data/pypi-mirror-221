from uuid import uuid4
from xsdata.models.enums import DataType

from sfdata.schema.models import PrimaryKey, Schema
from sfdata.stream_parser.events import EndNode, StartNode, Value

from sfdata.util import context_to_path


def identify_fields(stream, schema: Schema):
    """set field type and field name"""
    record = None
    entry_id = None
    for event in stream:
        path = context_to_path(event.context)

        if isinstance(event, StartNode):
            if new_record := schema.get_record_by_path(path):
                record = new_record
                entry_id = PrimaryKey(path=path)
                event = event.from_event(event, entry_id=entry_id)
        elif isinstance(event, EndNode):
            if schema.get_record_by_name(event.tag) == record:
                # end of record
                record = None
                event = event.from_event(event, entry_id=entry_id)
        if record:
            event = event.from_event(event, record_name=record.name)
        yield event

        if isinstance(event, StartNode) and record is not None and entry_id is not None:
            f = record.get_field_by_path(path)
            if field := record.get_field_by_path(path):
                value_event = next(stream)
                if isinstance(value_event, Value):
                    if custom_datatype := schema.get_datatype_by_name(field.type):
                        field_type = custom_datatype
                    else:
                        field_type = DataType.from_code(field.type.lower())

                    value_event = value_event.from_event(
                        value_event,
                        type=field_type,
                        field_name=field.name,
                        record_name=record.name,
                        entry_id=entry_id,
                    )
                yield value_event
