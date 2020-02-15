
from util import Request, current_timestamp, HttpMethod


class BilibiliApi:

    BASE_API_URL = 'https://api.bilibili.com'

    @classmethod
    def build_comment_api_request(cls, oid, pn=1, type_=1, sort=2):
        url = cls.BASE_API_URL + '/x/v2/reply'
        params = {
            '_': current_timestamp(),
            'oid': oid,
            'pn': pn,
            'type': type_,
            'sort': sort,
        }
        return Request(url=url, method=HttpMethod.GET, params=params)
