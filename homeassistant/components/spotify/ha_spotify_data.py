"""Define constants for the Spotify integration."""

from dataclasses import dataclass
import logging
from typing import Any
from asyncio import run_coroutine_threadsafe

from spotipy import Spotify

from homeassistant.core import HomeAssistant
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator


@dataclass
class HomeAssistantSpotifyData:
    """Spotify data stored in the Home Assistant data object."""

    client: Spotify
    current_user: dict[str, Any]
    devices: DataUpdateCoordinator[list[dict[str, Any]]]
    session: OAuth2Session
    hass: HomeAssistant

    def ensure_spotify_client(self) -> Spotify:
        return run_coroutine_threadsafe(self.async_get_spotify_client, self.hass.loop).result

    async def async_ensure_spotify_client(self) -> Spotify:
        if not self.session.valid_token:
            await self.session.async_ensure_token_valid()
            await self.hass.async_add_executor_job(
                self.spotify.set_auth, self.session.token["access_token"]
            )
        return self.client
