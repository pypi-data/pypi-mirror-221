import abc
from inspect import isabstract
from typing import Iterator, Tuple, List

from corpus_io.commons.json_services import JsonLoadService
from corpus_io.morphemes import Morpheme
from corpus_io.nikl.commons.mappers import extract_sentences_as_stream_from, tokenize_to_morphemes

TOKENIZED_SENT_GEN_TYPE = Iterator[Tuple[str, List[Morpheme]]]


class NIKLTokenizeIOService(abc.ABC):
    registered_subclasses = {}

    def __init_subclass__(cls):
        super().__init_subclass__()
        if not isabstract(cls):
            cls.registered_subclasses[cls.code()] = cls

    @classmethod
    def get_tokenized_sentence_generator(cls, dir_path, max_file_num=None, seed=0) -> TOKENIZED_SENT_GEN_TYPE:
        file_stream = JsonLoadService.load_files_as_stream(dir_path, max_file_num, seed)
        sentence_stream = extract_sentences_as_stream_from(file_stream)
        morpheme_stream = tokenize_to_morphemes(sentence_stream)
        return morpheme_stream

    @classmethod
    @abc.abstractmethod
    def code(cls) -> str:
        raise NotImplementedError

    @staticmethod
    def get_io_service_using_code(code):
        return NIKLTokenizeIOService.registered_subclasses[code]
