import json

from pysidra.api.controllers.util import get_response


class Authentication:
    def __init__(
        self, base_url, scope, client_id, client_secret, grant_type="client_credentials"
    ):
        self.base_url = base_url
        self.scope = scope
        self.client_id = client_id
        self.client_secret = client_secret
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self.payload = {'grant_type': grant_type, 'scope': scope,  'client_id': client_id,  'client_secret': client_secret }

    def get_token(self):
        return json.loads(
            get_response(
                method="POST",
                url=self.base_url,
                headers=self.headers,
                data=self.payload,
            ).text
        )["access_token"]
