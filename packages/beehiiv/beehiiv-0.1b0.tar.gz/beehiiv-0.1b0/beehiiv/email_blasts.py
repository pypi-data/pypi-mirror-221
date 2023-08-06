from beehiiv.endpoint import Endpoint


class EmailBlasts(Endpoint):

    def __init__(self, api_key, publicationId):
        super().__init__(api_key)
        self.endpoint = "/publications/{}/email_blasts"
        self.publicationId = publicationId

    def index(self, expand=[], limit=None, page=None):
        '''index'''
        return self._make_call(
            [self.publicationId],
            params={
                "expand[]": expand,
                "limit": limit,
                "page": page,
            },
        ).json()

    def show(self, emailBlastId, expand=[]):
        '''show'''
        return self._make_call(
            [self.publicationId, emailBlastId],
            endpoint=self.endpoint + "/{}",
            params={
                "expand[]": expand,
            },
        ).json()

    def update(self, subscriptionId, unsubscribe=None, custom_fields=[]):
        '''update'''
        return self._make_call(
            [self.publicationId, subscriptionId],
            endpoint=self.endpoint + "/{}",
            data={
                "unsubscribe": unsubscribe,
                "custom_fields": custom_fields,
            },
            method="PUT",
        ).json()

    def delete(self, subscriptionId):
        '''delete'''
        return self._make_call(
            [self.publicationId, subscriptionId],
            endpoint=self.endpoint + "/{}",
            method="DELETE",
        ).json()
