from beehiiv.endpoint import Endpoint


class Publications(Endpoint):

    def __init__(self, api_key):
        '''init

        :param str api_key: BeeHiiv API KEY
        '''
        super().__init__(api_key)
        self.endpoint = "/publications"

    def index(self, expand=[], limit=None, page=None):
        '''index
        Retrieve all publications associated with your API key.

        https://developers.beehiiv.com/docs/v2/f2cc85aaf19cd-index

        :param list expand: Optional list of expandable objects.
                            Allowed value: [stats]
                            stats - Returns statistics about the publication(s)
        :param int limit: A limit on the number of objects to be returned. The limit can range between 1 and 100, and the default is 10.
                          Default: 10
        :param int page: Pagination returns the results in pages. Each page contains the number of results specified by the limit (default: 10).
                         Default: 1
        '''  # noqa E501
        return self._make_call(
            None,
            params={
                "expand[]": expand,
                "limit": limit,
                "page": page,
            },
        ).json()

    def show(self, publicationId, expand=[]):
        '''show
        Retrieve a single publication

        https://developers.beehiiv.com/docs/v2/d664af2e46883-show

        :param str publicationId: The prefixed ID of the publication object
        :param list expand: Optional list of expandable objects.
                            Allowed value: [stats]
                            stats - Returns statistics about the publication(s)
        '''
        return self._make_call(
            [publicationId],
            endpoint=self.endpoint + "/{}",
            params={
                "expand[]": expand,
            },
        ).json()
