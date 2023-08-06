import re
from dataclasses import dataclass
from typing import Optional, Dict, Any

import lsjsonclasses
import requests
from requests import Session, Response
from requests.structures import CaseInsensitiveDict


@dataclass
class LsRestClientResponse:
    status_code: int
    content: str
    headers: CaseInsensitiveDict

    _json: Optional[dict] = None

    def json(self):
        if self._json is None:
            self._json = lsjsonclasses.LSoftJSONDecoder.loads(self.content)
        return self._json

    @classmethod
    def from_requests_response(cls, response: Response):
        return cls(
            status_code=response.status_code,
            content=response.content.decode("utf8"),
            headers=response.headers,
        )


class LsRestClient(Session):
    _clients = {}

    @classmethod
    def client(cls, name):
        try:
            return cls._clients[name]
        except KeyError as e:
            raise Exception(f"LsRestClient with name '{name}' not initialized.")

    def __init__(self, base_url: str = None, name: str = "default") -> None:
        self.base_url = base_url
        self.base_headers = {'content-type': 'application/json'}
        self.name = name
        super().__init__()
        self._clients[name] = self

    def full_url(self, url: str, params: dict | None = None) -> str:
        if params is None:
            params = {}

        full_url = f"{self.base_url}{url}"
        regex = re.compile("\{(.*?)\}")
        found = regex.findall(full_url)
        url_params = {p: params[p] for p in found}
        for p in found:
            del params[p]
        return full_url.format(**url_params)

    def request(
        self,
        method: str,
        url: str,
        *args,
        params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> LsRestClientResponse:  # pragma: no cover

        # apply base_headers
        headers = self.base_headers | kwargs.get("headers", {})
        kwargs |= dict(headers=headers)

        # params
        if params is None:
            params = {}
        if body is not None:
            kwargs['data'] = lsjsonclasses.LSoftJSONEncoder.dumps(body).encode("utf8")

        return LsRestClientResponse.from_requests_response(
            requests.request(
                method.upper(),
                self.full_url(url, params),
                *args,
                **kwargs
            )
        )

    def get(self, *args, **kwargs):
        return self.request('GET', *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.request('POST', *args, **kwargs)

    def put(self, *args, **kwargs):
        return self.request('PUT', *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.request('PATCH', *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.request('DELETE', *args, **kwargs)

    def options(self, *args, **kwargs):
        return self.request('OPTIONS', *args, **kwargs)

    def head(self, *args, **kwargs):
        return self.request('HEAD', *args, **kwargs)
