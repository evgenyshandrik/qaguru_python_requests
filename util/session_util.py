"""
Session util
"""
import os

from requests import Session


class BaseSession(Session):
    """
    Base session class
    """

    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        return super().request(method, url=f'{self.base_url}{url}', **kwargs)


def req_session() -> BaseSession:
    """
    Create session for reqres API
    """
    return BaseSession(base_url=os.getenv('reqres_api'))
