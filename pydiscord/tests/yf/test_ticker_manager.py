from typing import List

import pytest

from pydiscord.yf.ticker_manager import TickerManager


@pytest.fixture
def file_handler_mock(mocker):
    mock_file_handler = mocker.patch(
        'pydiscord.util.file_handler.FileHandler',
        autospec=True)

    return mock_file_handler.return_value


@pytest.fixture
def ticker_manager(file_handler_mock):
    return TickerManager(file_handler_mock)


def _add_linebreak(test_tickers: List[str]) -> str:
    return '\n'.join(test_tickers) + '\n'


def test_add_non_existing_ticker(ticker_manager, file_handler_mock):
    file_handler_mock.read_text.return_value = ''
    ticker_manager.add_ticker('AAPL')

    file_handler_mock.append_text.assert_called_once_with('AAPL\n')


def test_add_existing_ticker(ticker_manager, file_handler_mock):
    file_handler_mock.read_text.return_value = 'AAPL\n'
    ticker_manager.add_ticker('AAPL')

    file_handler_mock.append_text.assert_not_called()


def test_remove_ticker(ticker_manager, file_handler_mock):
    test_tickers: List[str] = ['AAPL', 'GOOGL']

    file_handler_mock.read_text.return_value = _add_linebreak(test_tickers)
    ticker_manager.remove_ticker('AAPL')

    file_handler_mock.write_text.assert_called_once_with('GOOGL\n')


def test_remove_non_existing_ticker(ticker_manager, file_handler_mock):
    test_tickers: List[str] = ['AAPL', 'GOOGL']

    file_handler_mock.read_text.return_value = _add_linebreak(test_tickers)
    ticker_manager.remove_ticker('MSFT')

    file_handler_mock.write_text.assert_not_called()


def test_get_all_tickers(ticker_manager, file_handler_mock):
    test_tickers: List[str] = ['AAPL', 'GOOGL', 'MSFT']

    file_handler_mock.read_text.return_value = _add_linebreak(test_tickers)
    tickers = ticker_manager.get_all_tickers()

    assert tickers == test_tickers
