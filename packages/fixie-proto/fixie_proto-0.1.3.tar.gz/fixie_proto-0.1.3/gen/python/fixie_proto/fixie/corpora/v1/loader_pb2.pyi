from fixie.corpora.v1 import common_pb2 as _common_pb2
from google.api import annotations_pb2 as _annotations_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoadRequest(_message.Message):
    __slots__ = ["corpus_id", "partition", "page_token"]
    CORPUS_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    corpus_id: str
    partition: str
    page_token: bytes
    def __init__(self, corpus_id: _Optional[str] = ..., partition: _Optional[str] = ..., page_token: _Optional[bytes] = ...) -> None: ...

class LoadResponse(_message.Message):
    __slots__ = ["page", "new_partitions"]
    class Page(_message.Message):
        __slots__ = ["documents", "next_page_token"]
        DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
        NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        documents: _containers.RepeatedCompositeFieldContainer[_common_pb2.Document]
        next_page_token: bytes
        def __init__(self, documents: _Optional[_Iterable[_Union[_common_pb2.Document, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...
    class Partition(_message.Message):
        __slots__ = ["name", "first_page_token"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        FIRST_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        name: str
        first_page_token: bytes
        def __init__(self, name: _Optional[str] = ..., first_page_token: _Optional[bytes] = ...) -> None: ...
    PAGE_FIELD_NUMBER: _ClassVar[int]
    NEW_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    page: LoadResponse.Page
    new_partitions: _containers.RepeatedCompositeFieldContainer[LoadResponse.Partition]
    def __init__(self, page: _Optional[_Union[LoadResponse.Page, _Mapping]] = ..., new_partitions: _Optional[_Iterable[_Union[LoadResponse.Partition, _Mapping]]] = ...) -> None: ...
