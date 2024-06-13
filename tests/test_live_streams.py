from ruvmedia.live_streams import get_channels

async def test_get_channels(session,event_loop):
    channels  = await get_channels(session)
    assert channels is not None
    assert len(channels) > 0
    assert "url" in channels[0]
    assert "name" in channels[0]
    assert "slug" in channels[0]
    assert channels[0]["url"] is not None
    assert channels[0]["name"] is not None
    assert channels[0]["slug"] is not None
    assert channels[0]["url"].startswith("http")
    #assert channels is None