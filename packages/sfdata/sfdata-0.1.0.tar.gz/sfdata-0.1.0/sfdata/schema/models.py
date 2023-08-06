import warnings
from typing import Optional
from uuid import uuid4
from functools import cached_property

from pydantic import BaseModel
from xsdata.exceptions import ConverterWarning
from xsdata.formats.converter import converter
from xsdata.models.enums import DataType


class PrimaryKey(BaseModel):
    path: str
    uid: str

    def __init__(self, **data):
        if not data.get("uid", None):
            data["uid"] = str(uuid4())
        super().__init__(**data)

    def __eq__(self, other: object) -> bool:
        return self.uid == getattr(other, "uid", None)

    @property
    def key(self):
        return f"{self.path} - {self.uid}"


class Base(BaseModel):
    pk: str
    name: str
    path: str

    def __init__(self, **data):
        if not data.get("path", None):
            parent_path = data.get("parent_path", "")
            data["path"] = parent_path + "/" + data["name"]
        if not data.get("pk", None):
            data["pk"] = str(uuid4())
        super().__init__(**data)


class Field(Base):
    type: str
    primary_key: bool = False
    foreign_key: Optional[str] = None
    generator: Optional[str] = None


class Record(Base):
    fields: list[Field]

    def get_field_by_pk(self, pk: str):
        fields = [f for f in self.fields if f.pk == pk]
        return next(iter(fields), None)

    def get_field_by_name(self, name):
        fields = [f for f in self.fields if f.name == name]
        return next(iter(fields), None)

    def get_field_by_path(self, path: str):
        fields = [f for f in self.fields if f.path == path]
        return next(iter(fields), None)

    @property
    def primary_key(self):
        fields = [f for f in self.fields if f.primary_key]
        return next(iter(fields), None)

    @property
    def foreign_keys(self):
        return [f for f in self.fields if f.foreign_key is not None]


class CustomDataType(BaseModel):
    """TODO - expand this custom types. currently only working for enums"""

    name: str
    base: str
    enumeration: list | dict

    def deserialize(self, value):
        datatype = DataType.from_code(self.base)

        def _raise_warning():
            warnings.warn(
                f"Failed to convert value `{value}` to one of {self.enumeration}",
                ConverterWarning,
            )

        if isinstance(self.enumeration, dict):
            if all(isinstance(key, int) for key in self.enumeration.keys()):
                # keys are integers
                try:
                    value_as_key = int(value)
                except ValueError:
                    # key is not an integer - check if in values
                    if value not in self.enumeration.values():
                        _raise_warning()
                else:
                    if value_as_key not in self.enumeration.keys():
                        _raise_warning()
                    else:
                        # get value given the enum key
                        value = self.enumeration[value_as_key]
            else:
                try:
                    value = self.enumeration[value]
                except KeyError:
                    _raise_warning()

            value = converter.deserialize(value, [datatype.type])
        else:
            if value not in self.enumeration:
                _raise_warning()
            value = converter.deserialize(value, [datatype.type])
        return value


class Schema(BaseModel):
    id: str
    version: str
    records: list[Record]
    datatypes: list[CustomDataType] = []

    def get_record_by_name(self, name) -> Optional[Record]:
        records = [r for r in self.records if r.name == name]
        return next(iter(records), None)

    def get_record_by_path(self, path) -> Optional[Record]:
        records = [r for r in self.records if r.path == path]
        return next(iter(records), None)

    def get_datatype_by_name(self, name) -> Optional[CustomDataType]:
        datatypes = [dt for dt in self.datatypes if dt.name == name]
        return next(iter(datatypes), None)

    @property
    def primary_keys(self) -> list[tuple[Field, Record]]:
        return tuple(
            (field, record)
            for record in self.records
            for field in record.fields
            if field.primary_key
        )

    @property
    def foreign_keys(self) -> list[tuple[Field, Record]]:
        foreign_key_fields = []
        for record in self.records:
            for field in record.fields:
                if field.foreign_key is not None:
                    record_name, field_name = field.foreign_key.split(".")
                    record = self.get_record_by_name(record_name)
                    field = record.get_field_by_name(field_name)
                    foreign_key_fields.append((field, record))
        return foreign_key_fields

    @property
    def primary_keys_with_generator(self) -> list[tuple[Field, Record]]:
        return tuple(
            entry for entry in self.primary_keys if entry[0].generator is not None
        )

    def get_field_record(self, field: Field) -> Optional[Record]:
        for record in self.records:
            if field in record.fields:
                return record
        return None
