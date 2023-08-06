import inspect
import requests

class Endpoint:
    api_uri = "https://api.beehiiv.com/v2"
    endpoint = None

    def __init__(self, api_key):
        '''init'''
        self.api_key = api_key

    def _craft_url(self, endpoint, params):
        '''make api url'''
        return "{}{}".format(
            self.api_uri,
            endpoint.format(*params) if params else endpoint,
        )

    def _create_call_headers(self):
        '''create headers'''
        return {
            "Authorization": "Bearer {}".format(self.api_key),
        }

    def _make_call(self, endpoint_params, params=None, endpoint=None, data=None,
                   method="GET"):
        '''make call api'''
        return requests.request(
            method,
            headers=self._create_call_headers(),
            url=self._craft_url(
                self.endpoint if not endpoint else endpoint,
                endpoint_params
            ),
            data=data,
            params=params,
        )

