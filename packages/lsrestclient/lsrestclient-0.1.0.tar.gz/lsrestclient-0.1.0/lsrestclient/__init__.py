import requests
from requests import Session, Response


class LsRestClient(Session):
	def __init__(self, base_url: str = None , name=default) -> None:
		self.base_url = base_url
		super().__init__()

	def full_url(self, url: str) -> str:
		full_url = f"{self.base_url}{url}"
		return full_url

	def request(
		self,
		method,
		url,
		*args,
		**kwargs
	) -> Response:  # pragma: no cover
		return requests.request(
			method.upper(),
			self.full_url(url),
			*args,
			**kwargs
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

