from typing import List, Protocol

from medl.common import SongData

__all__ = ["BaseMetadataFetcher"]


class BaseMetadataFetcher(Protocol):
    def search(self, query: str, limit: int) -> List[SongData]:
        ...

    def fetch(self, query: str) -> List[SongData]:
        ...
