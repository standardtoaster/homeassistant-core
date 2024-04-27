"""Define constants for the Spotify integration."""

from dataclasses import dataclass
import logging
from typing import Any

from spotipy import Spotify

from homeassistant.components.media_player import MediaType
from homeassistant.helpers.config_entry_oauth2_flow import OAuth2Session
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

DOMAIN = "spotify"

LOGGER = logging.getLogger(__package__)

SPOTIFY_SCOPES = [
    # Needed to be able to control playback
    "user-modify-playback-state",
    # Needed in order to read available devices
    "user-read-playback-state",
    # Needed to determine if the user has Spotify Premium
    "user-read-private",
    # Needed for media browsing
    "playlist-read-private",
    "playlist-read-collaborative",
    "user-library-read",
    "user-top-read",
    "user-read-playback-position",
    "user-read-recently-played",
    "user-follow-read",
]

MEDIA_PLAYER_PREFIX = "spotify://"
MEDIA_TYPE_SHOW = "show"

PLAYABLE_MEDIA_TYPES = [
    MediaType.PLAYLIST,
    MediaType.ALBUM,
    MediaType.ARTIST,
    MediaType.EPISODE,
    MEDIA_TYPE_SHOW,
    MediaType.TRACK,
]