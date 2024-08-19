from typing import List

from pydiscord.util.file_handler import FileHandler


class TickerManager:
    def __init__(self, file_handler: FileHandler):
        self.file_handler: FileHandler = file_handler

    def add_ticker(self, ticker: str):
        if ticker not in self.get_all_tickers():
            self.file_handler.append_text(ticker + "\n")

    def remove_ticker(self, ticker: str):
        tickers = self.get_all_tickers()
        if ticker in tickers:
            tickers.remove(ticker)
            self.file_handler.write_text("\n".join(tickers) + "\n")

    def get_all_tickers(self) -> List[str]:
        return self.file_handler.read_text().splitlines()
