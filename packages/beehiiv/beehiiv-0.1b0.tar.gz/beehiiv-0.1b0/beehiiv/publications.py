from beehiiv.endpoint import Endpoint


class Publications(Endpoint):

    def __init__(self, api_key):
        super().__init__(api_key)
        self.endpoint = "/publications"

    def index(self, expand=[], limit=None, page=None):
        '''index'''
        return self._make_call(
            None,
            params={
                "expand[]": expand,
                "limit": limit,
                "page": page,
            },
        ).json()

    def show(self, publicationId, expand=[]):
        '''show'''
        return self._make_call(
            [publicationId],
            endpoint=self.endpoint + "/{}",
            params={
                "expand[]": expand,
            },
        ).json()
