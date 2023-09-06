# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yaticker.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="yaticker.proto",
    package="",
    syntax="proto3",
    serialized_pb=_b(
        '\n\x0eyaticker.proto"\xcb\x08\n\x08yaticker\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x02\x12\x0c\n\x04time\x18\x03 \x01(\x12\x12\x10\n\x08\x63urrency\x18\x04 \x01(\t\x12\x10\n\x08\x65xchange\x18\x05 \x01(\t\x12&\n\tquoteType\x18\x06 \x01(\x0e\x32\x13.yaticker.QuoteType\x12.\n\x0bmarketHours\x18\x07 \x01(\x0e\x32\x19.yaticker.MarketHoursType\x12\x15\n\rchangePercent\x18\x08 \x01(\x02\x12\x11\n\tdayVolume\x18\t \x01(\x12\x12\x0f\n\x07\x64\x61yHigh\x18\n \x01(\x02\x12\x0e\n\x06\x64\x61yLow\x18\x0b \x01(\x02\x12\x0e\n\x06\x63hange\x18\x0c \x01(\x02\x12\x11\n\tshortName\x18\r \x01(\t\x12\x12\n\nexpireDate\x18\x0e \x01(\x12\x12\x11\n\topenPrice\x18\x0f \x01(\x02\x12\x15\n\rpreviousClose\x18\x10 \x01(\x02\x12\x13\n\x0bstrikePrice\x18\x11 \x01(\x02\x12\x18\n\x10underlyingSymbol\x18\x12 \x01(\t\x12\x14\n\x0copenInterest\x18\x13 \x01(\x12\x12)\n\x0boptionsType\x18\x14 \x01(\x0e\x32\x14.yaticker.OptionType\x12\x12\n\nminiOption\x18\x15 \x01(\x12\x12\x10\n\x08lastSize\x18\x16 \x01(\x12\x12\x0b\n\x03\x62id\x18\x17 \x01(\x02\x12\x0f\n\x07\x62idSize\x18\x18 \x01(\x12\x12\x0b\n\x03\x61sk\x18\x19 \x01(\x02\x12\x0f\n\x07\x61skSize\x18\x1a \x01(\x12\x12\x11\n\tpriceHint\x18\x1b \x01(\x12\x12\x10\n\x08vol_24hr\x18\x1c \x01(\x12\x12\x18\n\x10volAllCurrencies\x18\x1d \x01(\x12\x12\x14\n\x0c\x66romcurrency\x18\x1e \x01(\t\x12\x12\n\nlastMarket\x18\x1f \x01(\t\x12\x19\n\x11\x63irculatingSupply\x18  \x01(\x01\x12\x11\n\tmarketcap\x18! \x01(\x01"\x80\x02\n\tQuoteType\x12\x08\n\x04NONE\x10\x00\x12\r\n\tALTSYMBOL\x10\x05\x12\r\n\tHEARTBEAT\x10\x07\x12\n\n\x06\x45QUITY\x10\x08\x12\t\n\x05INDEX\x10\t\x12\x0e\n\nMUTUALFUND\x10\x0b\x12\x0f\n\x0bMONEYMARKET\x10\x0c\x12\n\n\x06OPTION\x10\r\x12\x0c\n\x08\x43URRENCY\x10\x0e\x12\x0b\n\x07WARRANT\x10\x0f\x12\x08\n\x04\x42OND\x10\x11\x12\n\n\x06\x46UTURE\x10\x12\x12\x07\n\x03\x45TF\x10\x14\x12\r\n\tCOMMODITY\x10\x17\x12\x0c\n\x08\x45\x43NQUOTE\x10\x1c\x12\x12\n\x0e\x43RYPTOCURRENCY\x10)\x12\r\n\tINDICATOR\x10*\x12\r\n\x08INDUSTRY\x10\xe8\x07"\x1f\n\nOptionType\x12\x08\n\x04\x43\x41LL\x10\x00\x12\x07\n\x03PUT\x10\x01"a\n\x0fMarketHoursType\x12\x0e\n\nPRE_MARKET\x10\x00\x12\x12\n\x0eREGULAR_MARKET\x10\x01\x12\x0f\n\x0bPOST_MARKET\x10\x02\x12\x19\n\x15\x45XTENDED_HOURS_MARKET\x10\x03\x62\x06proto3'
    ),
)


_YATICKER_QUOTETYPE = _descriptor.EnumDescriptor(
    name="QuoteType",
    full_name="yaticker.QuoteType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="NONE", index=0, number=0, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ALTSYMBOL", index=1, number=5, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="HEARTBEAT", index=2, number=7, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="EQUITY", index=3, number=8, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INDEX", index=4, number=9, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MUTUALFUND", index=5, number=11, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MONEYMARKET", index=6, number=12, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="OPTION", index=7, number=13, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CURRENCY", index=8, number=14, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="WARRANT", index=9, number=15, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BOND", index=10, number=17, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="FUTURE", index=11, number=18, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ETF", index=12, number=20, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="COMMODITY", index=13, number=23, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ECNQUOTE", index=14, number=28, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CRYPTOCURRENCY", index=15, number=41, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INDICATOR", index=16, number=42, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INDUSTRY", index=17, number=1000, options=None, type=None
        ),
    ],
    containing_type=None,
    options=None,
    serialized_start=730,
    serialized_end=986,
)
_sym_db.RegisterEnumDescriptor(_YATICKER_QUOTETYPE)

_YATICKER_OPTIONTYPE = _descriptor.EnumDescriptor(
    name="OptionType",
    full_name="yaticker.OptionType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CALL", index=0, number=0, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PUT", index=1, number=1, options=None, type=None
        ),
    ],
    containing_type=None,
    options=None,
    serialized_start=988,
    serialized_end=1019,
)
_sym_db.RegisterEnumDescriptor(_YATICKER_OPTIONTYPE)

_YATICKER_MARKETHOURSTYPE = _descriptor.EnumDescriptor(
    name="MarketHoursType",
    full_name="yaticker.MarketHoursType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PRE_MARKET", index=0, number=0, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="REGULAR_MARKET", index=1, number=1, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="POST_MARKET", index=2, number=2, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="EXTENDED_HOURS_MARKET", index=3, number=3, options=None, type=None
        ),
    ],
    containing_type=None,
    options=None,
    serialized_start=1021,
    serialized_end=1118,
)
_sym_db.RegisterEnumDescriptor(_YATICKER_MARKETHOURSTYPE)


_YATICKER = _descriptor.Descriptor(
    name="yaticker",
    full_name="yaticker",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="yaticker.id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="price",
            full_name="yaticker.price",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="time",
            full_name="yaticker.time",
            index=2,
            number=3,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="currency",
            full_name="yaticker.currency",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="exchange",
            full_name="yaticker.exchange",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="quoteType",
            full_name="yaticker.quoteType",
            index=5,
            number=6,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="marketHours",
            full_name="yaticker.marketHours",
            index=6,
            number=7,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="changePercent",
            full_name="yaticker.changePercent",
            index=7,
            number=8,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dayVolume",
            full_name="yaticker.dayVolume",
            index=8,
            number=9,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dayHigh",
            full_name="yaticker.dayHigh",
            index=9,
            number=10,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dayLow",
            full_name="yaticker.dayLow",
            index=10,
            number=11,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="change",
            full_name="yaticker.change",
            index=11,
            number=12,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="shortName",
            full_name="yaticker.shortName",
            index=12,
            number=13,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="expireDate",
            full_name="yaticker.expireDate",
            index=13,
            number=14,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="openPrice",
            full_name="yaticker.openPrice",
            index=14,
            number=15,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="previousClose",
            full_name="yaticker.previousClose",
            index=15,
            number=16,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="strikePrice",
            full_name="yaticker.strikePrice",
            index=16,
            number=17,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="underlyingSymbol",
            full_name="yaticker.underlyingSymbol",
            index=17,
            number=18,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="openInterest",
            full_name="yaticker.openInterest",
            index=18,
            number=19,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="optionsType",
            full_name="yaticker.optionsType",
            index=19,
            number=20,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="miniOption",
            full_name="yaticker.miniOption",
            index=20,
            number=21,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="lastSize",
            full_name="yaticker.lastSize",
            index=21,
            number=22,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bid",
            full_name="yaticker.bid",
            index=22,
            number=23,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bidSize",
            full_name="yaticker.bidSize",
            index=23,
            number=24,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="ask",
            full_name="yaticker.ask",
            index=24,
            number=25,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="askSize",
            full_name="yaticker.askSize",
            index=25,
            number=26,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="priceHint",
            full_name="yaticker.priceHint",
            index=26,
            number=27,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="vol_24hr",
            full_name="yaticker.vol_24hr",
            index=27,
            number=28,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="volAllCurrencies",
            full_name="yaticker.volAllCurrencies",
            index=28,
            number=29,
            type=18,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="fromcurrency",
            full_name="yaticker.fromcurrency",
            index=29,
            number=30,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="lastMarket",
            full_name="yaticker.lastMarket",
            index=30,
            number=31,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="circulatingSupply",
            full_name="yaticker.circulatingSupply",
            index=31,
            number=32,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="marketcap",
            full_name="yaticker.marketcap",
            index=32,
            number=33,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _YATICKER_QUOTETYPE,
        _YATICKER_OPTIONTYPE,
        _YATICKER_MARKETHOURSTYPE,
    ],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=19,
    serialized_end=1118,
)

_YATICKER.fields_by_name["quoteType"].enum_type = _YATICKER_QUOTETYPE
_YATICKER.fields_by_name["marketHours"].enum_type = _YATICKER_MARKETHOURSTYPE
_YATICKER.fields_by_name["optionsType"].enum_type = _YATICKER_OPTIONTYPE
_YATICKER_QUOTETYPE.containing_type = _YATICKER
_YATICKER_OPTIONTYPE.containing_type = _YATICKER
_YATICKER_MARKETHOURSTYPE.containing_type = _YATICKER
DESCRIPTOR.message_types_by_name["yaticker"] = _YATICKER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

yaticker = _reflection.GeneratedProtocolMessageType(
    "yaticker",
    (_message.Message,),
    dict(
        DESCRIPTOR=_YATICKER,
        __module__="yaticker_pb2"
        # @@protoc_insertion_point(class_scope:yaticker)
    ),
)
_sym_db.RegisterMessage(yaticker)


# @@protoc_insertion_point(module_scope)
