from corpus_io.nikl.abc import NIKLTokenizeIOService


class WrittenIOService(NIKLTokenizeIOService):
    @classmethod
    def code(cls) -> str:
        return 'written'
