import time

import requests


class MinimApi:
    def __init__(self, endpoint, app_id, secret):
        self.api_secret = secret
        self.api_app_id = app_id
        self.api_endpoint = endpoint

        self.url_prefix = 'api/v1'
        self.token_expires_at = 0

    async def fetch_all_ids(self, url, opts=None):
        if opts is None:
            opts = {}
        aggregate_data = []
        offset = 0
        finished = False

        while not finished:
            opts.update({"offset": offset})
            res = await self.get(url, opts)
            ids = [item["app_id"] for item in res["data"]]

            aggregate_data += ids

            if len(aggregate_data) >= int(res.headers['x-total-count']):
                finished = True
            else:
                offset = len(aggregate_data)

        return aggregate_data

    async def multi_get(self, url, opts=None):
        if opts is None:
            opts = {"maxMultiGetLimit": 10, "callback": None, "ids": None, "params": {}}
        ids = opts.get("ids") or await self.fetch_all_ids(url)
        max_multi_get_limit = opts.get("max_multi_get_limit") or 10

        ids_in_chunks = []
        aggregate_data = []

        for i in range(0, len(ids), max_multi_get_limit):
            ids_in_chunks.append(ids[i:i + max_multi_get_limit])

        for chunk in ids_in_chunks:
            params = {**(opts.get("params") or {}), "app_id": ",".join(chunk)}

            res = await self.get(url, params)

            if opts.get("callback"):
                aggregate_data = res()

            aggregate_data += res["data"]

        return aggregate_data

    def get(self, url, opts=None):
        return self.request("get", url, opts)

    def post(self, url, data=None):
        return self.request("post", url, None, data)

    def put(self, url, data=None):
        return self.request("put", url, None, data)

    def patch(self, url, data=None):
        return self.request("patch", url, None, data)

    def delete(self, url, opts=None):
        return self.request("delete", url, opts)

    async def request(self, method, url, opts=None, data=None):
        timestamp = int(time.time())

        if timestamp > self.token_expires_at - 15:
            await self._get_access_token()

        opts = opts or {}

        params = {**opts, "access_token": self.access_token}

        response = requests.request(method, self.api_endpoint + "/" + self.url_prefix + url, params=params, data=data)

        return response.json()

    async def _get_access_token(self):
        data = {
            "client_id": self.api_app_id,
            "client_secret": self.api_secret,
            "grant_type": "client_credentials",
        }

        for tries in range(3):
            try:
                response = requests.post(self.api_endpoint + "/api/oauth/token", data=data)
                token_data = response.json()

                self.access_token = token_data["access_token"]
                self.token_expires_at = (token_data["created_at"] + token_data["expires_in"]) * 1000

                break
            except Exception as error:
                print(f"unable to get token: {error}")
