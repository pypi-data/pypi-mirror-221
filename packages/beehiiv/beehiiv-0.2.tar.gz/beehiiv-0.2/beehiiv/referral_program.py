from beehiiv.endpoint import Endpoint


class ReferralProgram(Endpoint):

    def __init__(self, api_key, publicationId):
        '''init

        :param str api_key: BeeHiiv API KEY
        :param str publicationId: The prefixed ID of the publication object
        '''
        super().__init__(api_key)
        self.endpoint = "/publications/{}/referral_program"
        self.publicationId = publicationId

    def show(self, limit=None, page=None):
        '''show
        Retrieve details about the publication's referral program,
        including milestones and rewards.

        https://developers.beehiiv.com/docs/v2/f580beba61c93-show

        :param int limit: A limit on the number of objects to be returned. The limit can range between 1 and 100, and the default is 10.
                          Default: 10
        :param int page: Pagination returns the results in pages. Each page contains the number of results specified by the limit (default: 10).
                         Default: 1
        '''  # noqa E501
        return self._make_call(
            [self.publicationId],
            params={
                "limit": limit,
                "page": page,
            },
        ).json()
