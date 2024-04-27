"""Support for interacting with Spotify Connect."""

from __future__ import annotations

from homeassistant.core import HomeAssistant, ServiceCall

from .const import DOMAIN
from .ha_spotify_data import HomeAssistantSpotifyData


class SpotifyServices:
    """Class that holes services for Spotify and should be published to hass."""

    def __init__(
        self,
        hass: HomeAssistant,
    ) -> None:
        """Initialise with HASS Object."""
        self._hass = hass

    def async_register(self) -> None:
        """Register all our services."""

        def handle_play(call: ServiceCall):
            """Handle calls to the Play service."""
            data: HomeAssistantSpotifyData = self._hass.data[DOMAIN][
                "dfb3056334a97cec4500e26c1e5c23fd"
            ]
            client = data.ensure_spotify_client()
            client.volume(10, "bd77d6e99a44cdb{1ad8c5af102a4f8c4291fe82e")
            client.start_playback(
                "bd77d6e99a44cdb1ad8c5af102a4f8c4291fe82e",
                "spotify:playlist:37i9dQZF1DZ06evO1EfAgb",
            )
            return True

        self._hass.services.async_register(DOMAIN, "play", handle_play)
