from __future__ import annotations

import json
import aiohttp

from .const import LIVE_CHANNELS, LOGGER

CHANNEL_BASE_URL = "https://geo.spilari.ruv.is/channel/"


async def get_channels() -> list[dict]:
    results = []
    for channel in LIVE_CHANNELS:
        results.append({**channel, "identifier": f'channel.{channel["slug"]}'})
    return results


async def get_channel_media(session: aiohttp.client.ClientSession, slug: str) -> dict:
    url = CHANNEL_BASE_URL + slug
    response = await session.request("GET", url, headers={"Accept": "application/json"})
    if response.status == 200:
        data = json.loads(await response.text())
        # If the channel has a switcher for different resolution/bitrates, use that instead of the url
        # if 'switcher' in data:
        #     url = data['switcher']
        # else:
        url = data["url"]
        return {"url": url, "identifier": f"channel.{slug}"}

    else:
        LOGGER.error(
            f"Error getting channel {slug}: {response.status} {await response.text()}"
        )

    return {}
