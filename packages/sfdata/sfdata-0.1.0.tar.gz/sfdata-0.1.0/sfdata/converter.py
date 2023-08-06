import logging

from xsdata.exceptions import ConverterWarning
from xsdata.formats.converter import converter
from xsdata.models.enums import DataType

from sfdata.schema.models import CustomDataType
from sfdata.stream_parser.events import Value

logger = logging.getLogger(__name__)


def convert_types(stream):
    """try and coerce the event type"""
    for event in stream:
        if isinstance(event, Value):
            value_type = getattr(event, "type", None)
            if isinstance(value_type, DataType):
                try:
                    value = converter.deserialize(event.value, [event.type.type])
                except ConverterWarning as e:
                    logger.warning(f"error:{e} | event:{event}")
                else:
                    event = event.from_event(event, value=value)
            elif isinstance(value_type, CustomDataType):
                try:
                    value = value_type.deserialize(event.value)
                except ConverterWarning as e:
                    logger.warning(f"error:{e} | event:{event}")
                else:
                    event = event.from_event(event, value=value)
        yield event
