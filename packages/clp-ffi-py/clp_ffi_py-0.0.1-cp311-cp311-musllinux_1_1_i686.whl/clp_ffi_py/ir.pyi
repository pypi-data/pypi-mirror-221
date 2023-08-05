from datetime import tzinfo
from typing import Any, Dict, Optional

class Metadata:
    def __init__(self, ref_timestamp: int, timestamp_format: str, timezone_id: str): ...
    def is_using_four_byte_encoding(self) -> bool: ...
    def get_ref_timestamp(self) -> int: ...
    def get_timestamp_format(self) -> str: ...
    def get_timezone_id(self) -> str: ...
    def get_timezone(self) -> tzinfo: ...

class LogEvent:
    def __init__(
        self,
        log_message: str,
        timestamp: int,
        index: int = 0,
        metadata: Optional[Metadata] = None,
    ): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __getstate__(self) -> Dict[str, Any]: ...
    def __setstate__(self, state: Dict[str, Any]) -> None: ...
    def get_log_message(self) -> str: ...
    def get_timestamp(self) -> int: ...
    def get_index(self) -> int: ...
    def get_formatted_message(self, timezone: Optional[tzinfo] = None) -> str: ...

class FourByteEncoder:
    @staticmethod
    def encode_preamble(ref_timestamp: int, timestamp_format: str, timezone: str) -> bytearray: ...
    @staticmethod
    def encode_message_and_timestamp_delta(timestamp_delta: int, msg: bytes) -> bytearray: ...
    @staticmethod
    def encode_message(msg: bytes) -> bytearray: ...
    @staticmethod
    def encode_timestamp_delta(timestamp_delta: int) -> bytearray: ...
