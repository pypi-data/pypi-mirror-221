from tqdm import tqdm

from corpus_io.morphemes import Morpheme
from corpus_io.nikl.abc import TOKENIZED_SENT_GEN_TYPE

SENT_MORPHEME_SEP = "__SEN|||MOR__"
MORPHEME_SEP = "__ML|||MR__"


def convert_morpheme_stream_to_writable_format(morpheme_stream):
    for sentence, morphemes in morpheme_stream:
        morpheme_str = MORPHEME_SEP.join([morpheme.to_writable_format() for morpheme in morphemes])
        yield f"{sentence}{SENT_MORPHEME_SEP}{morpheme_str}\n"


def convert_line_into_morphemes(line):
    [sent, morphemes_str] = line.split(SENT_MORPHEME_SEP)
    morpheme_strs = morphemes_str.split(MORPHEME_SEP)
    morphemes = [Morpheme.create_from_formatted_str(morpheme_str) for morpheme_str in morpheme_strs]
    return sent, morphemes


class MorphemeIOService(object):
    @staticmethod
    def write_stream(output_file_path, morpheme_stream: TOKENIZED_SENT_GEN_TYPE):
        str_stream = convert_morpheme_stream_to_writable_format(morpheme_stream)
        with open(output_file_path, 'w') as f:
            for line in tqdm(str_stream):
                f.write(line)

    @staticmethod
    def read_as_stream(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                line = line[:-1]
                if len(line) == 0:
                    break
                yield convert_line_into_morphemes(line)
