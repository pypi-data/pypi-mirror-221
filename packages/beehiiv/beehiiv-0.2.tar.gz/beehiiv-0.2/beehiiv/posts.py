from beehiiv.endpoint import Endpoint


class Posts(Endpoint):

    def __init__(self, api_key, publicationId):
        '''init

        :param str api_key: BeeHiiv API KEY
        :param str publicationId: The prefixed ID of the publication object
        '''
        super().__init__(api_key)
        self.endpoint = "/publications/{}/posts"
        self.publicationId = publicationId

    def index(self, audience=None, content_tags=[], expand=[], limit=None,
              page=None, platform=None, status=None):
        '''index
        Retrieve all posts belonging to a specific publication

        https://developers.beehiiv.com/docs/v2/84b282584290d-index

        :param str audience: Optionally filter the results by audience
                             Allowed values: [free, premium, all]
                             Default: all
        :param list content_tags: Optionally filter posts by content_tags. Adding a content tag will return any post with that content tag associated to it.
        :param list expand: Optional list of expandable objects.
                            Allowed values: [stats, free_web_content, free_email_content, free_rss_content, premium_web_content, premium_email_content]
                            stats - Returns statistics about the post(s)
                            free_web_content - Returns the web HTML rendered to a free reader
                            free_email_content - Returns the email HTML rendered to a free reader
                            free_rss_content - Returns the RSS feed HTML
                            premium_web_content - Returns the web HTML rendered to a premium reader
                            premium_email_content - Returns the email HTML rendered to a premium reader
        :param int limit: A limit on the number of objects to be returned. The limit can range between 1 and 100, and the default is 10.
                          Default: 10
        :param int page: Pagination returns the results in pages. Each page contains the number of results specified by the limit (default: 10).
                         Default: 1

        :param str platform: Optionally filter the results by platform.
                             Allowed values: [web, email, both, all]
                             web - Posts only published to web.
                             email - Posts only published to email.
                             both - Posts published to email and web.
                             all - Does not restrict results by platform.
                             Default: all
        :param str status: Optionally filter the results by the status of the post.
                           Allowed values: [draft, confirmed, archived, all]
                           draft - not been scheduled.
                           confirmed - The post will be active after the scheduled_at.
                           archived - The post is no longer active.
                           all - Does not restrict results by status.
                           Default: all
        '''  # noqa E501
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
        '''show
        Retreive a single Post belonging to a specific publication

        https://developers.beehiiv.com/docs/v2/ab0d2f8ee91c2-show

        :param str postId: The prefixed ID of the post object
        :param list expand: Optional list of expandable objects.
                            Allowed values: [stats, free_web_content, free_email_content, free_rss_content, premium_web_content, premium_email_content]
                            stats - Returns statistics about the post(s)
                            free_web_content - Returns the web HTML rendered to a free reader
                            free_email_content - Returns the email HTML rendered to a free reader
                            free_rss_content - Returns the RSS feed HTML
                            premium_web_content - Returns the web HTML rendered to a premium reader
                            premium_email_content - Returns the email HTML rendered to a premium reader
        '''  # noqa E501
        return self._make_call(
            [self.publicationId, postId],
            endpoint=self.endpoint + "/{}",
            params={
                "expand[]": expand,
            },
        ).json()

    def destory(self, postId):
        '''delete
        Delete or Archive a post. Any post that has been confirmed will have
        it's status changed to archived. Posts in the draft status will be
        permenantly deleted.

        https://developers.beehiiv.com/docs/v2/d82c22d939938-destroy

        :param str postId: The prefixed ID of the post object
        '''  # noqa E501
        return self._make_call(
            [self.publicationId, postId],
            endpoint=self.endpoint + "/{}",
            method="DELETE",
        ).json()
