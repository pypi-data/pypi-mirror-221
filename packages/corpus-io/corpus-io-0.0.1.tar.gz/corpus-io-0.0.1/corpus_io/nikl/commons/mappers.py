from typing import Iterable
from kiwipiepy import Kiwi

from corpus_io.morphemes import Morpheme

_kiwi = Kiwi()


def extract_sentence_as_stream(json_data: dict):
    paragraphs = [news["paragraph"] for news in json_data["document"]]
    for paragraph in paragraphs:
        for sentence in paragraph:
            yield sentence["form"]


def extract_sentences_as_stream_from(jsons: Iterable[dict]):
    for json_data in jsons:
        for sentence in extract_sentence_as_stream(json_data):
            yield sentence


def tokenize_to_morphemes(sentences: Iterable[str]):
    for sentence in sentences:
        tokens = _kiwi.tokenize(sentence)
        morphemes = [Morpheme.create_from_token(token) for token in tokens]
        yield sentence, morphemes
