from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MediaInfo:
    """Object information for a media on RÚV."""

    name: str
    identifier: str
    image: str | None = None
    # needs media_type audio video ?


@dataclass
class Media:
    """Media on RÚV."""

    # name: str
    identifier: str
    url: str
    media_type: str
