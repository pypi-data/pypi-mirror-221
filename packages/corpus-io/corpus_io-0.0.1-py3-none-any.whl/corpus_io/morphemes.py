from dataclasses import dataclass

FIELD_SEP = "__FL|||FR__"


@dataclass(frozen=True)
class Morpheme:
    form: str
    tag: str
    start: int
    end: int

    @classmethod
    def create_from_token(cls, token):
        return cls(form=token.form, tag=token.tag, start=token.start, end=token.end)

    @classmethod
    def create_from_formatted_str(cls, formatted_str):
        [form, tag, start, end] = formatted_str.split(FIELD_SEP)
        return cls(form=form, tag=tag, start=int(start), end=int(end))

    def to_writable_format(self):
        return FIELD_SEP.join([self.form, self.tag, str(self.start), str(self.end)])
