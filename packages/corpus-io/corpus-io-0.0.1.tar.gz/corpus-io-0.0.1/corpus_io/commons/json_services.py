import os
import json
import random
from typing import List


class JsonLoadService(object):
    @staticmethod
    def load_file(filepath) -> dict:
        with open(filepath) as f:
            loaded_json = json.load(f)
        return loaded_json

    @staticmethod
    def load_files(dir_path, *args, **kwargs) -> List[dict]:
        return [data for data in JsonLoadService.load_files_as_stream(dir_path, *args, **kwargs)]

    @staticmethod
    def load_files_as_stream(dir_path, max_file_num=None, seed=0):
        json_filenames = sorted([filename for filename in os.listdir(dir_path) if filename.endswith('.json')])

        if max_file_num and max_file_num < len(json_filenames):
            random.seed(seed)
            json_filenames = random.sample(json_filenames, max_file_num)

        for json_filename in json_filenames:
            filepath = os.path.join(dir_path, json_filename)
            yield JsonLoadService.load_file(filepath)
