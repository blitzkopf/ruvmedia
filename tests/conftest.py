import pytest
import aiohttp


@pytest.fixture
async def gql_client():
    from ruvmedia.gql_client import RuvGQLClient

    gql = RuvGQLClient()
    yield gql
    await gql.close()


@pytest.fixture
async def session():
    sess = aiohttp.ClientSession()
    yield sess
    await sess.close()
