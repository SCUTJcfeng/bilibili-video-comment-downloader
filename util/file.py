
import os
import json


class FileUtil:

    @classmethod
    def write_json(cls, file_path, file_name, json_data):
        file_ = os.path.join(file_path, file_name)
        with open(file_, mode='w', encoding='utf8') as f:
            f.write(json.dumps(json_data, indent=4, ensure_ascii=False))
