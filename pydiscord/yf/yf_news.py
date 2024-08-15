from dataclasses import dataclass, field


@dataclass
class YFNews:
    uuid: str
    title: str
    publisher: str
    link: str
    relatedTickers: list = field(default_factory=list)
