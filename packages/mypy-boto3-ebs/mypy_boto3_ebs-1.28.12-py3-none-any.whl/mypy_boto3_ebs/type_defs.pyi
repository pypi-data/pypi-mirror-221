"""
Type annotations for ebs service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/type_defs/)

Usage::

    ```python
    from mypy_boto3_ebs.type_defs import BlockTypeDef

    data: BlockTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody

from .literals import StatusType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BlockTypeDef",
    "ChangedBlockTypeDef",
    "CompleteSnapshotRequestRequestTypeDef",
    "CompleteSnapshotResponseTypeDef",
    "GetSnapshotBlockRequestRequestTypeDef",
    "GetSnapshotBlockResponseTypeDef",
    "ListChangedBlocksRequestRequestTypeDef",
    "ListSnapshotBlocksRequestRequestTypeDef",
    "PutSnapshotBlockRequestRequestTypeDef",
    "PutSnapshotBlockResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
    "TagOutputTypeDef",
    "ListSnapshotBlocksResponseTypeDef",
    "ListChangedBlocksResponseTypeDef",
    "StartSnapshotRequestRequestTypeDef",
    "StartSnapshotResponseTypeDef",
)

BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "BlockIndex": int,
        "BlockToken": str,
    },
    total=False,
)

ChangedBlockTypeDef = TypedDict(
    "ChangedBlockTypeDef",
    {
        "BlockIndex": int,
        "FirstBlockToken": str,
        "SecondBlockToken": str,
    },
    total=False,
)

_RequiredCompleteSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCompleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "ChangedBlocksCount": int,
    },
)
_OptionalCompleteSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCompleteSnapshotRequestRequestTypeDef",
    {
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "ChecksumAggregationMethod": Literal["LINEAR"],
    },
    total=False,
)

class CompleteSnapshotRequestRequestTypeDef(
    _RequiredCompleteSnapshotRequestRequestTypeDef, _OptionalCompleteSnapshotRequestRequestTypeDef
):
    pass

CompleteSnapshotResponseTypeDef = TypedDict(
    "CompleteSnapshotResponseTypeDef",
    {
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnapshotBlockRequestRequestTypeDef = TypedDict(
    "GetSnapshotBlockRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "BlockIndex": int,
        "BlockToken": str,
    },
)

GetSnapshotBlockResponseTypeDef = TypedDict(
    "GetSnapshotBlockResponseTypeDef",
    {
        "DataLength": int,
        "BlockData": StreamingBody,
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChangedBlocksRequestRequestTypeDef = TypedDict(
    "_RequiredListChangedBlocksRequestRequestTypeDef",
    {
        "SecondSnapshotId": str,
    },
)
_OptionalListChangedBlocksRequestRequestTypeDef = TypedDict(
    "_OptionalListChangedBlocksRequestRequestTypeDef",
    {
        "FirstSnapshotId": str,
        "NextToken": str,
        "MaxResults": int,
        "StartingBlockIndex": int,
    },
    total=False,
)

class ListChangedBlocksRequestRequestTypeDef(
    _RequiredListChangedBlocksRequestRequestTypeDef, _OptionalListChangedBlocksRequestRequestTypeDef
):
    pass

_RequiredListSnapshotBlocksRequestRequestTypeDef = TypedDict(
    "_RequiredListSnapshotBlocksRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
_OptionalListSnapshotBlocksRequestRequestTypeDef = TypedDict(
    "_OptionalListSnapshotBlocksRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StartingBlockIndex": int,
    },
    total=False,
)

class ListSnapshotBlocksRequestRequestTypeDef(
    _RequiredListSnapshotBlocksRequestRequestTypeDef,
    _OptionalListSnapshotBlocksRequestRequestTypeDef,
):
    pass

_RequiredPutSnapshotBlockRequestRequestTypeDef = TypedDict(
    "_RequiredPutSnapshotBlockRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "BlockIndex": int,
        "BlockData": Union[str, bytes, IO[Any], StreamingBody],
        "DataLength": int,
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
    },
)
_OptionalPutSnapshotBlockRequestRequestTypeDef = TypedDict(
    "_OptionalPutSnapshotBlockRequestRequestTypeDef",
    {
        "Progress": int,
    },
    total=False,
)

class PutSnapshotBlockRequestRequestTypeDef(
    _RequiredPutSnapshotBlockRequestRequestTypeDef, _OptionalPutSnapshotBlockRequestRequestTypeDef
):
    pass

PutSnapshotBlockResponseTypeDef = TypedDict(
    "PutSnapshotBlockResponseTypeDef",
    {
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

ListSnapshotBlocksResponseTypeDef = TypedDict(
    "ListSnapshotBlocksResponseTypeDef",
    {
        "Blocks": List[BlockTypeDef],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChangedBlocksResponseTypeDef = TypedDict(
    "ListChangedBlocksResponseTypeDef",
    {
        "ChangedBlocks": List[ChangedBlockTypeDef],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredStartSnapshotRequestRequestTypeDef",
    {
        "VolumeSize": int,
    },
)
_OptionalStartSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalStartSnapshotRequestRequestTypeDef",
    {
        "ParentSnapshotId": str,
        "Tags": Sequence[TagTypeDef],
        "Description": str,
        "ClientToken": str,
        "Encrypted": bool,
        "KmsKeyArn": str,
        "Timeout": int,
    },
    total=False,
)

class StartSnapshotRequestRequestTypeDef(
    _RequiredStartSnapshotRequestRequestTypeDef, _OptionalStartSnapshotRequestRequestTypeDef
):
    pass

StartSnapshotResponseTypeDef = TypedDict(
    "StartSnapshotResponseTypeDef",
    {
        "Description": str,
        "SnapshotId": str,
        "OwnerId": str,
        "Status": StatusType,
        "StartTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "Tags": List[TagOutputTypeDef],
        "ParentSnapshotId": str,
        "KmsKeyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
