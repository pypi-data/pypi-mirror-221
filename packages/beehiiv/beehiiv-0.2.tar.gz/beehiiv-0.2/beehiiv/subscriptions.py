from beehiiv.endpoint import Endpoint


class Subscriptions(Endpoint):

    def __init__(self, api_key, publicationId):
        '''init

        :param str api_key: BeeHiiv API KEY
        :param str publicationId: The prefixed ID of the publication object
        '''
        super().__init__(api_key)
        self.endpoint = "/publications/{}/subscriptions"
        self.publicationId = publicationId

    def create(self, email, reactivate_existing=None, send_welcome_email=None,
               utm_source=None, utm_medium=None, utm_campaign=None,
               referring_site=None, referral_code=None, custom_fields=[]):
        '''create
        Create new subscriptions for a publication.

        https://developers.beehiiv.com/docs/v2/1f82a0eaf9b68-create

        :param str email: The email address of the subscription.
        :param bool reactivate_existing: Whether or not to reactivate the subscription if they have already unsubscribed. This option should be used only if the subscriber is knowingly resubscribing.
                                         Default: false
        :param bool send_welcome_email: Default: false
        :param str utm_source: The source of the subscription.
        :param str utm_medium: The medium of the subscription
        :param str utm_campaign: The acquisition campaign of the subscription
        :param str referring_site: The website that the subscriber was referred from
        :param str referral_code: This should be a subscribers referral_code. This gives referral credit for the new subscription.
        :param list custom_fields: The custom fields must already exist for the publication. Any new custom fields here will be discarded.
        '''  # noqa E501
        return self._make_call(
            [self.publicationId],
            data={
                "email": email,
                "reactivate_existing": reactivate_existing,
                "send_welcome_email": send_welcome_email,
                "utm_source": utm_source,
                "utm_medium": utm_medium,
                "utm_campaign": utm_campaign,
                "referring_site": referring_site,
                "referral_code": referral_code,
                "custom_fields": custom_fields,
            },
            method="POST",
        ).json()

    def index(self, email=None, expand=[], limit=None, page=None, status=None,
              tier=None):
        '''index
        Retrieve all subscriptions belonging to a specific publication

        https://developers.beehiiv.com/docs/v2/ac72589d509bc-index

        :param str email: Optional email address to find a subscription.
                          This param must be an exact match and is case insensitive.
        :param list expand: Optional list of expandable objects.
                            Allowed values: [stats, custom_fields, referrals]
                            stats - Returns statistics about the subscription(s).
                            custom_fields - Returns an array of custom field values that have been set on the subscription.
                            referrals - Returns an array of subscriptions with limited data - id, email, and status. These are the subscriptions that were referred by this subscription.
        :param int limit: A limit on the number of objects to be returned. The limit can range between 1 and 100, and the default is 10.
                          Default: 10
        :param int page: Pagination returns the results in pages. Each page contains the number of results specified by the limit (default: 10).
                         Default: 1
        :param str status: Optionally filter the results by a status
                           Allowed values: [validating, invalid, pending, active, inactive, all]
                           Default: all
        :param str tier: Optionally filter the results by a their tier
                         Allowed values: [free, premium, all]
                         Default: all
        '''  # noqa E501
        return self._make_call(
            [self.publicationId],
            params={
                "email": email,
                "expand[]": expand,
                "limit": limit,
                "page": page,
                "status": status,
                "tier": tier,
            },
        ).json()

    def show(self, subscriptionId, expand=[]):
        '''show
        Retrieve a single subscription belonging to a specific publication

        https://developers.beehiiv.com/docs/v2/21a42d55e6aff-show

        :param str subscriptionId: The prefixed ID of the subscription object
        :param list expand: Optional list of expandable objects.
                            Allowed values: [stats, custom_fields, referrals]
                            stats - Returns statistics about the subscription(s).
                            custom_fields - Returns an array of custom field values that have been set on the subscription.
                            referrals - Returns an array of subscriptions with limited data - id, email, and status. These are the subscriptions that were referred by this subscription.
        ''' # noqa E501
        return self._make_call(
            [self.publicationId, subscriptionId],
            endpoint=self.endpoint + "/{}",
            params={
                "expand[]": expand,
            },
        ).json()

    def update(self, subscriptionId, unsubscribe=None, custom_fields=[]):
        '''update
        Update a subscriber

        https://developers.beehiiv.com/docs/v2/6bb99290622e5-update

        :param str subscriptionId: The prefixed ID of the subscription object
        :param bool unsubscribe: Optional parameter to unsubscribe the subscriber. If they are a premium subscription, this will also end their billing.
                                 Default: false
        :param list custom_fields: The custom fields must already exist for the publication. Any new custom fields here will be discarded.
                                   {
                                        name: str [The name of the existing custom field],
                                        value: str [The value to stored for the subscription. Will be ignored if delete: true is included.],
                                        delete: bool [Optionally delete any value stored. If true, any passed in value attribute will be ignored.],
                                   }
        '''  # noqa E501
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
        '''delete
        Delete a subscription.
        This cannot be undone All data associated with the subscription
        will also be deleted. We recommend unsubscribing when possible
        instead of deleting.

        If a premium subscription is deleted they will no longer be billed.

        https://developers.beehiiv.com/docs/v2/5fa5aa2351d71-delete

        :param str subscriptionId: The prefixed ID of the subscription object
        '''
        return self._make_call(
            [self.publicationId, subscriptionId],
            endpoint=self.endpoint + "/{}",
            method="DELETE",
        ).json()
