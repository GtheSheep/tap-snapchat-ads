"""SnapchatAds Authentication."""


from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta


# The SingletonMeta metaclass makes your streams reuse the same authenticator instance.
# If this behaviour interferes with your use-case, you can remove the metaclass.
class SnapchatAdsAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator class for SnapchatAds."""

    @property
    def oauth_request_body(self) -> dict:
        """Define the OAuth request body for the SnapchatAds API."""
        return {
            'grant_type': 'refresh_token',
            'client_id': self.config["client_id"],
            'client_secret': self.config["client_secret"],
            'refresh_token': self.config["refresh_token"]
        }

    @classmethod
    def create_for_stream(cls, stream) -> "SnapchatAdsAuthenticator":
        return cls(
            stream=stream,
            auth_endpoint="https://accounts.snapchat.com/login/oauth2/access_token",
            oauth_scopes=','.join(['snapchat-marketing-api']),
        )
