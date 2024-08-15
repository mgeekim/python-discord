import pytest

from pydiscord.yf.yf import YF


@pytest.fixture
def yf() -> YF:
    return YF()


@pytest.fixture
def mock_yf_ticker(mocker):
    mock = mocker.MagicMock()
    mocker.patch('yfinance.Ticker', return_value=mock)

    return mock
