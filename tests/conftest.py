import pytest
import aiohttp


@pytest.fixture
def gql_client():
    from ruvmedia.gql_client import RuvGQLClient
    return RuvGQLClient()


@pytest.fixture
async def session():
    sess = aiohttp.ClientSession()
    yield sess
    await sess.close()
