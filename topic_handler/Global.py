# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: xuach/proto/models.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


class Languages(betterproto.Enum):
    DEFAULT = 0
    es_CO = 1
    en_US = 2
    pt_BR = 3


@dataclass
class RequestFormat(betterproto.Message):
    topic: str = betterproto.string_field(1)
    token: str = betterproto.string_field(2)
    language: "Languages" = betterproto.enum_field(3)


@dataclass
class ResponseError(betterproto.Message):
    res: int = betterproto.int32_field(1)
    msg: str = betterproto.string_field(2)
    data: Dict[str, str] = betterproto.map_field(
        3, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
