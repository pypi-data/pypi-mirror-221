from beehiiv.endpoint import Endpoint


class EmailBlasts(Endpoint):

    def __init__(self, api_key, publicationId):
        '''init

        :param str api_key: BeeHiiv API KEY
        :param str publicationId: The prefixed ID of the publication object
        '''
        super().__init__(api_key)
        self.endpoint = "/publications/{}/email_blasts"
        self.publicationId = publicationId

    def index(self, expand=[], limit=None, page=None):
        '''index
        Retrieve all Email Blasts

        https://developers.beehiiv.com/docs/v2/63287a49cf161-index

        :param list expand: Optional list of expandable objects.
                            Allowed values: [stats, free_email_content, premium_email_content]
                            stats - Returns statistics about the email blast(s)
                            free_email_content - Returns the email HTML rendered to a free reader
                            premium_email_content - Returns the email HTML rendered to a premium reader
        :param int limit: A limit on the number of objects to be returned. The limit can range between 1 and 100, and the default is 10.
                          Default: 10
        :param int page: Pagination returns the results in pages. Each page contains the number of results specified by the limit (default: 10).
                         Default: 1
        '''  # noqa E501
        return self._make_call(
            [self.publicationId],
            params={
                "expand[]": expand,
                "limit": limit,
                "page": page,
            },
        ).json()

    def show(self, emailBlastId, expand=[]):
        '''show
        Retrieve an Email Blast

        https://developers.beehiiv.com/docs/v2/6fd5be33e6726-show

        :param str emailBlastId: The prefixed ID of the email blast object
        :param list expand: Optional list of expandable objects.
                            Allowed values: [stats, free_email_content, premium_email_content]
                            stats - Returns statistics about the email blast(s)
                            free_email_content - Returns the email HTML rendered to a free reader
                            premium_email_content - Returns the email HTML rendered to a premium reader
        '''  # noqa E501
        return self._make_call(
            [self.publicationId, emailBlastId],
            endpoint=self.endpoint + "/{}",
            params={
                "expand[]": expand,
            },
        ).json()
