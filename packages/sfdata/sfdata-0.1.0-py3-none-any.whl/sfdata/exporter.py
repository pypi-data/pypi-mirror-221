from collections import defaultdict

import tablib
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime
from xsdata.models.enums import DataType

from sfdata.schema.models import Schema
from sfdata.stream_parser.events import Value


def export_value(event: Value):
    """
    export value to standard python format
    (opinionated maybe, might not be the best approach)
    """
    if isinstance(event.value, XmlTime):
        return event.value.to_time()
    if isinstance(event.value, XmlDate):
        return event.value.to_date()
    if isinstance(event.value, XmlDateTime):
        return event.value.to_datetime()
    if isinstance(event.value, XmlPeriod):
        if event.type == DataType.G_YEAR:
            return event.value.year
        if event.type == DataType.G_MONTH:
            return event.value.month
        if event.type == DataType.G_DAY:
            return event.value.day
        # for month-day and year-month export as string
        return str(event.value)
    return event.value


def populate_databook(stream,primary_keys, schema: Schema) -> tablib.Databook:
    """export data to tablib databook"""
    book = tablib.Databook()

    entries = {record.name: defaultdict(list) for record in schema.records}

    for event in stream:
        entries[event.record_name][event.entry_id.uid].append(event)
    primary_keys = primary_keys.value
    for record in schema.records:
        headers = [f.name for f in record.fields]
        sheet = tablib.Dataset(title=record.name, headers=headers)
        book.add_sheet(sheet)
        for entry in entries[record.name].values():
            row = []
            for field in record.fields:
                found_field = False
                for event in entry:
                    event_field_name = getattr(event, "field_name", None)
                    if field.name == event_field_name:
                        value = export_value(event)
                        row.append(value)
                        found_field = True
                if not found_field:
                    if field.foreign_key is not None:
                        value = primary_keys.get(field.foreign_key)
                    else:
                        value = None
                    row.append(value)
            sheet.append(row)
    return book
