# -*- coding: utf-8 -*-

from . import dispatchers  # noqa F401
from .decorators import immutable, mutable, serializer
from .fields import (
    BooleanField,
    ChildField,
    DateField,
    DateTimeField,
    DecimalField,
    FloatField,
    IntegerField,
    MappingField,
    RegexField,
    SequenceField,
    SetField,
    StringField,
    TimeField,
    URLField,
    UUIDField,
)
from .functions import (
    from_json,
    from_yaml,
    is_model,
    to_dict,
    to_json,
    to_model,
    to_yaml,
)
from .types import ImmutableDict, TypedMapping, TypedSequence, TypedSet

__all__ = [
    # decorators.py
    "mutable",
    "immutable",
    "serializer",
    # types.py
    "ImmutableDict",
    "TypedSequence",
    "TypedMapping",
    "TypedSet",
    # fields.py
    "BooleanField",
    "ChildField",
    "DateField",
    "DateTimeField",
    "TimeField",
    "FloatField",
    "IntegerField",
    "MappingField",
    "RegexField",
    "SetField",
    "StringField",
    "SequenceField",
    "URLField",
    "UUIDField",
    "DecimalField",
    # functions.py
    "from_json",
    "from_yaml",
    "is_model",
    "to_dict",
    "to_json",
    "to_model",
    "to_yaml",
]


__version__ = "1.1.0"
__title__ = "related-mltoolbox"

__author__ = """Ian Maurer, Maximilian Otten, Christian Hoppe"""

__uri__ = "https://git.openlogisticsfoundation.org/silicon-economy/base/ml-toolbox/related-mltoolbox"
__copyright__ = (
    "Copyright (c) Open Logistics Foundation, Copyright (c) 2017 genomoncology.com, "
)
__description__ = (
    "(Fork of related) Related: Straightforward nested object models in Python"
)
__doc__ = __description__ + " <" + __uri__ + ">"
__license__ = "MIT"
