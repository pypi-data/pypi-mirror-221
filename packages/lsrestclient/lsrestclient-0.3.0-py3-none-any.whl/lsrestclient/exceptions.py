class ConnectionError(Exception):

    def __init__(self, *args: object, url: str | None = None) -> None:
        self.url = url
        super().__init__(f"Connection could not be established to '{url}'", *args)
