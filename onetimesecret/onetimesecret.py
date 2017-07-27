#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth

url = "https://onetimesecret.com/api/v1/share"


class OneTimeSecret:

    def __init__(self, email, api_key):
        self.email = email
        self.api_key = api_key

    def share(self, secret, passphrase=None, ttl=None, recipient=None):

        # Default ttl to 1 day
        if ttl is None:
            ttl = 3600 * 24

        data = {"secret": secret.encode("utf-8"),
                "ttl": ttl}

        if passphrase:
            data.update({"passphrase": passphrase.encode("utf-8")})
        if recipient:
            data.update({"recipient": recipient.encode("utf-8")})

        r = requests.post(url, data=data, auth=HTTPBasicAuth(self.email, self.api_key))

        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            return None
