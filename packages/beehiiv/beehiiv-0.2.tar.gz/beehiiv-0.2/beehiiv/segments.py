from beehiiv.endpoint import Endpoint


class Segments(Endpoint):

    def __init__(self, api_key, publicationId):
        '''init

        :param str api_key: BeeHiiv API KEY
        :param str publicationId: The prefixed ID of the publication object
        '''
        super().__init__(api_key)
        self.endpoint = "/publications/{}/segments"
        self.publicationId = publicationId

    def index(self, limit=None, page=None, status=None, type=None):
        '''index
        Retrieve information about all segments
        belonging to a specific publication

        https://developers.beehiiv.com/docs/v2/c64e02cfe1026-index

        :param int limit: A limit on the number of objects to be returned. The limit can range between 1 and 100, and the default is 10.
                          Default: 10
        :param int page: Pagination returns the results in pages. Each page contains the number of results specified by the limit (default: 10).
                         Default: 1
        :param str status: Optionally filter the results by the segment's status.
                           Allowed values: [pending, processing, completed, failed, all]
                           Default: all
        :param str type: Optionally filter the results by the segment's type.
                         Allowed values: [dynamic, static, manual, all]
                         Default: all
        '''  # noqa E501
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
        '''show
        Retrieve a single segment belonging to a specific publication

        https://developers.beehiiv.com/docs/v2/8a20afd6a7570-show

        :param str segmentId: The prefixed ID of the segment object
        '''
        return self._make_call(
            [self.publicationId, segmentId],
            endpoint=self.endpoint + "/{}",
        ).json()

    def delete(self, segmentId):
        '''delete
        Delete a segment. Deleting the segment does not effect
        the subscriptions in the segment.

        https://developers.beehiiv.com/docs/v2/620e1d108ef9a-delete

        :param str segmentId: The prefixed ID of the segment object
        '''
        return self._make_call(
            [self.publicationId, segmentId],
            endpoint=self.endpoint + "/{}",
            method="DELETE",
        ).json()

    def expand_results(self, segmentId, limit=None, page=None):
        '''expand results
        List the Subscriber Ids from the most recent calculation
        of a specific publication.

        https://developers.beehiiv.com/docs/v2/dbf5cd286f14b-expand-results

        :param str segmentId: The prefixed ID of the segment object
        :param int limit: A limit on the number of objects to be returned. The limit can range between 1 and 100, and the default is 10.
                          Default: 10
        :param int page: Pagination returns the results in pages. Each page contains the number of results specified by the limit (default: 10).
                         Default: 1
        '''  # noqa E501
        return self._make_call(
            [self.publicationId, segmentId],
            endpoint=self.endpoint + "/{}/results",
            params={
                "limit": limit,
                "page": page,
            },
        ).json()
