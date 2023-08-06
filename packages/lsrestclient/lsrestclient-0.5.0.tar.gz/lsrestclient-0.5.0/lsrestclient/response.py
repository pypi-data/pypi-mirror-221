from dataclasses import dataclass
from typing import Optional

import lsjsonclasses
from requests import Response
from requests.structures import CaseInsensitiveDict


@dataclass
class LsRestClientResponse:
    """
    Represents a response from the LsRestClient.
    """

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
        """
        Create an instance of LsRestClientResponse from a requests Response object.

        :param response: The requests Response object.
        :type response: Response
        :return: An instance of LsRestClientResponse representing the response.
        :rtype: LsRestClientResponse
        """
        return cls(
            status_code=response.status_code,
            content=response.content.decode("utf8"),
            headers=response.headers,
        )
