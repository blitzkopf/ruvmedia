async def test_get_categories(gql_client):
    # This test will fail because the client is not connected
    # and the client is not connected because the connect method
    # is not called
    categories = await gql_client.get_categories()
    assert categories is not None
    assert len(categories) > 0
    assert "categories" in categories
    assert "title" in categories["categories"][0]
    assert "slug" in categories["categories"][0]
    assert "__typename" in categories["categories"][0]


async def test_get_category(gql_client):
    # This test will fail because the client is not connected
    # and the client is not connected because the connect method
    # is not called
    categories = await gql_client.get_category(category="kvikmyndir", station="tv")
    assert categories is not None
    assert len(categories) > 0
    assert "categories" in categories
    assert "title" in categories["categories"][0]
    assert "slug" in categories["categories"][0]
    assert "__typename" in categories["categories"][0]
