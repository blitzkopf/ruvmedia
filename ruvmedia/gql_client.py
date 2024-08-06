from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


class RuvGQLClient:
    def __init__(self):
        self.transport = AIOHTTPTransport(url="https://spilari.nyr.ruv.is/gql/")
        self.client = Client(
            transport=self.transport, fetch_schema_from_transport=False
        )
        self.session = None
        # self.session = await self.client.connect_async(reconnecting=True)

    async def connect(self):
        if self.session is None:
            self.session = await self.client.connect_async(reconnecting=True)

    async def close(self):
        await self.client.close_async()

    async def get_categories(self, station="tv"):
        await self.connect()
        query = gql("""
            query getCategories($station: StationSearch!) {
                Category(station: $station) {
                    categories {
                        title
                        slug
                        __typename
                    }
                    __typename
                }
            }
        """)
        answer = await self.session.execute(query, variable_values={"station": station})
        return answer["Category"]

    async def get_category(self, category, station="tv"):
        await self.connect()
        query = gql("""
            query getCatgory($category: String!, $station: StationSearch!) {
                Category(station: $station, category: $category) {
                    categories {
                        title
                        slug
                        programs {
                            title
                            programID
                            slug
                            image
                            __typename
                        }
                        __typename
                    }
                    __typename
                }
            }
        """)
        answer = await self.session.execute(
            query, variable_values={"category": category, "station": station}
        )
        return answer["Category"]

    async def get_panels(self, station="tv"):
        await self.connect()
        query = gql("""
            query getPanel($station: Station!) {
                Featured(station: $station) {
                    id
                    panels {
                        title
                        type
                        slug
                        id

                        __typename
                    }
                    __typename
                }
            }
        """)
        answer = await self.session.execute(query, variable_values={"station": station})
        return answer["Featured"]

    async def get_panel(self, slug, station="tv"):
        await self.connect()
        query = gql("""
            query getPanel($slug: [String!], $station: Station!) {
                Featured(station: $station) {
                    panels(slug: { value: $slug }) {
                        title
                        display_style
                        slug
                        type
                        programs {
                            title
                            programID
                            slug
                            image
                            __typename
                        }
                        __typename
                    }
                    __typename
                }
            }
        """)
        answer = await self.session.execute(
            query, variable_values={"slug": slug, "station": station}
        )
        return answer["Featured"]

    async def get_program(self, id: int):
        await self.connect()
        query = gql("""
            query getProgram($id: Int!) {
                Program(id: $id) {
                    format
                    channel
                    title
                    image
                    categories(limit: 3) {
                        title
                        slug
                        __typename}
                    episodes(limit: 100) {
                        title
                        id
                        scope
                        image
                        rating
                        __typename
                    }
                    __typename
                }
            }
        """)

        answer = await self.session.execute(query, variable_values={"id": int(id)})
        return answer["Program"]

    async def get_episode(self, progam_id: int, episode_id: str):
        await self.connect()
        query = gql("""
            query getEpisode($programID: Int!, $episodeID: [String!] = [""])  {
    Program(id: $programID) {
      title
      episodes(limit: 1, id: { value: $episodeID }) {
        title
        id
        file
      }
    }
  }
        """)

        answer = await self.session.execute(
            query,
            variable_values={"programID": int(progam_id), "episodeID": [episode_id]},
        )
        return answer["Program"]
