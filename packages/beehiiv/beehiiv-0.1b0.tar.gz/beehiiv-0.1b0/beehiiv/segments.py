from beehiiv.endpoint import Endpoint


class Segments(Endpoint):

    def __init__(self, api_key, publicationId):
        super().__init__(api_key)
        self.endpoint = "/publications/{}/segments"
        self.publicationId = publicationId

    def index(self, limit=None, page=None, status=None, type=None):
        '''index'''
        return self._make_call(
            [self.publicationId],
            params={
                "limit": limit,
                "page": page,
                "status": status,
                "type": type,
            },
        ).json()

    def show(self, segmentId):
        '''show'''
        return self._make_call(
            [self.publicationId, segmentId],
            endpoint=self.endpoint + "/{}",
        ).json()

    def delete(self, segmentId):
        '''delete'''
        return self._make_call(
            [self.publicationId, segmentId],
            endpoint=self.endpoint + "/{}",
            method="DELETE",
        ).json()

    def expand_results(self, segmentId, limit=None, page=None):
        '''expand results'''
        return self._make_call(
            [self.publicationId, segmentId],
            endpoint=self.endpoint + "/{}/results",
            params={
                "limit": limit,
                "page": page,
            },
        ).json()
