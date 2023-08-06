from beehiiv.endpoint import Endpoint


class ReferralProgram(Endpoint):

    def __init__(self, api_key, publicationId):
        super().__init__(api_key)
        self.endpoint = "/publications/{}/referral_program"
        self.publicationId = publicationId

    def show(self, emailBlastId, limit=None, page=None):
        '''show'''
        return self._make_call(
            [self.publicationId, emailBlastId],
            params={
                "limit": limit,
                "page": page,
            },
        ).json()
