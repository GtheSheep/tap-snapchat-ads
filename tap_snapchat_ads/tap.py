"""SnapchatAds tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_snapchat_ads.streams import (
    OrganizationsStream,
    AdAccountsStream,
    CampaignsStream,
)
STREAM_TYPES = [
    OrganizationsStream,
    AdAccountsStream,
    CampaignsStream,
]


class TapSnapchatAds(Tap):
    """SnapchatAds tap class."""
    name = "tap-snapchat-ads"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "refresh_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapSnapchatAds.cli()
