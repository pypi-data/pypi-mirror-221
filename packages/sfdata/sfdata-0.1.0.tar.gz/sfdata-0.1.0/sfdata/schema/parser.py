from pathlib import Path
import jstyleson
from sfdata.schema.models import CustomDataType, Schema, Record, Field
import yaml


def parse_schema(schema) -> Schema:
    if isinstance(schema, dict):
        return _parse(schema)
    elif hasattr(schema, "read"):
        return _parse_string(schema.read())
    else:
        return _parse_file(schema)


def _parse_file(path):
    path = Path(path)
    with path.open("rt") as f:
        return _parse_string(f.read())


def _parse_string(content):
    if content.startswith("{"):
        content = jstyleson.loads(content)
    else:
        content = yaml.safe_load(content)
    return _parse(content)


def _parse(content: dict):
    content = content.copy()
    records = content.pop("records", {})

    _datatypes = content.pop("datatypes", {})
    schema_id = content.pop("id")
    version = content.pop("version")
    _records = []
    datatypes = [
        CustomDataType(name=name, **datatype) for name, datatype in _datatypes.items()
    ]
    for name, record in records.items():
        fields = record.pop("fields", {})
        record_path = record.get("path", None) or name
        _fields = [
            Field(name=field_name, parent_path=record_path, **field)
            for field_name, field in fields.items()
        ]
        _records.append(Record(fields=_fields, **record, name=name))

    schema = Schema(
        records=_records, version=version, id=schema_id, datatypes=datatypes
    )
    # schema = _set_foreign_keys_path(schema)
    return schema
