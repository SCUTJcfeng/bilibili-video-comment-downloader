
from api import BilibiliApi
from util import ConfigLoader, RequestUtil, FileUtil

config = ConfigLoader.load_config()


class VideoComment:
    def __init__(self, video_oid):
        self.video_oid = video_oid
        self.page = 1
        self.total_comments = []

    def run(self):
        self.get_comments()
        self.save_comments()

    def get_comment_by_page(self, page):
        request = BilibiliApi.build_comment_api_request(self.video_oid, pn=page)
        response = RequestUtil.do_request(request)
        if response.code != 0 or response.status_code != 200:
            print(response.message)
            return
        self.decode_comment_list(response.data['replies'])

    def decode_comment_list(self, data_list):
        for data in data_list:
            message = data['content']['message']
            self.total_comments.append(message)

    def get_comments(self):
        while self.page <= config['MAX_PAGE']:
            self.get_comment_by_page(self.page)
            self.page += 1

    def save_comments(self):
        FileUtil.write_json(config['FILE_PATH'], f'comments_{self.video_oid}.json', self.total_comments)
        for comment in self.total_comments:
            print(comment)
            print('-' * 20)


if __name__ == "__main__":
    for oid in config['VIDEO_OID_LIST']:
        VideoComment(oid).run()
