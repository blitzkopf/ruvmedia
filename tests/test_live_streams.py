from ruvmedia.live_streams import get_channels


async def test_get_channels(session):
    channels = await get_channels()
    assert channels is not None
    assert len(channels) > 0
    assert "image" in channels[0]
    assert "name" in channels[0]
    assert "slug" in channels[0]
    assert channels[0]["image"] is not None
    assert channels[0]["name"] is not None
    assert channels[0]["slug"] is not None
    assert channels[0]["image"].startswith("http")
    # assert channels is None
