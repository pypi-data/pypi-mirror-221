from dataclasses import dataclass
from typing import Dict, List, Optional

from corpus_io.file_io.morphemes_io import MorphemeIOService
from corpus_io.nikl.abc import NIKLTokenizeIOService


@dataclass(frozen=True)
class CorpusMergeOption:
    dir_path: str
    max_file_num: Optional[int] = None


def merge_streams(streams):
    for stream in streams:
        for item in stream:
            yield item


class CorpusTokenizeMergeUseCase(object):
    @staticmethod
    def execute(output_file_path, read_options: Dict[str, List[CorpusMergeOption]], seed=0):
        merged_stream = CorpusTokenizeMergeUseCase.create_corpus_read_stream(read_options, seed)
        MorphemeIOService.write_stream(output_file_path, merged_stream)

    @staticmethod
    def create_corpus_read_stream(read_options: Dict[str, List[CorpusMergeOption]], seed=0):
        streams = CorpusTokenizeMergeUseCase._convert_options_into_streams(read_options, seed)
        return merge_streams(streams)

    @staticmethod
    def _convert_options_into_streams(read_options, seed):
        streams = []
        for code, options in read_options.items():
            io_service_cls = NIKLTokenizeIOService.get_io_service_using_code(code)
            for option in options:
                stream = io_service_cls.get_tokenized_sentence_generator(option.dir_path,
                                                                         max_file_num=option.max_file_num, seed=seed)
                streams.append(stream)
        return streams
