from beehiiv.endpoint import Endpoint


class Posts(Endpoint):

    def __init__(self, api_key, publicationId):
        super().__init__(api_key)
        self.endpoint = "/publications/{}/posts"
        self.publicationId = publicationId

    def index(self, audience=None, content_tags=[], expand=[], limit=None,
              page=None, platform=None, status=None):
        '''index'''
        return self._make_call(
            [self.publicationId],
            params={
                "audience": audience,
                "content_tags[]": content_tags,
                "expand[]": expand,
                "limit": limit,
                "page": page,
                "platform": platform,
                "status": status,
            },
        ).json()

    def show(self, postId, expand=[]):
        '''show'''
        return self._make_call(
            [self.publicationId, postId],
            endpoint=self.endpoint + "/{}",
            params={
                "expand[]": expand,
            },
        ).json()

    def destory(self, subscriptionId, postId):
        '''delete'''
        return self._make_call(
            [self.publicationId, subscriptionId],
            endpoint=self.endpoint + "/{}",
            method="DELETE",
        ).json()
