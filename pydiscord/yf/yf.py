from dataclasses import dataclass, field
from typing import List

import yfinance as yf


@dataclass
class YFNews:
    uuid: str
    title: str
    publisher: str
    link: str
    relatedTickers: list = field(default_factory=list)


class YF:
    def __init__(self):
        self._ticker = ''
        self._seen_news_uuid = set()

    def set_ticker(self, ticker: str):
        if self._ticker is not ticker:
            self._ticker = ticker
            self._seen_news_uuid.clear()
            self.monitor_news()

    def monitor_news(self) -> List[YFNews]:
        unseen_news = []
        for news in self._get_latest_news():
            yf_news = self._create_yf_news(news)
            if yf_news.uuid not in self._seen_news_uuid:
                unseen_news.append(yf_news)
                self._seen_news_uuid.add(yf_news.uuid)

        return unseen_news

    def _get_latest_news(self) -> list:
        if not self._ticker:
            return []
        company = yf.Ticker(self._ticker)
        return company.news

    def _create_yf_news(self, news: dict) -> YFNews:
        return YFNews(**{field: news[field] for field in YFNews.__dataclass_fields__ if field in news})
