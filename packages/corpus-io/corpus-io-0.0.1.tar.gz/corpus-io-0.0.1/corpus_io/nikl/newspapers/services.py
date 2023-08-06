from corpus_io.nikl.abc import NIKLTokenizeIOService


class NewspaperIOService(NIKLTokenizeIOService):
    @classmethod
    def code(cls) -> str:
        return 'newspaper'
