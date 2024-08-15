from pydiscord.tests.yf.tests_data import dummy_news_1st, dummy_news_2nd, result_2nd


def test_yf_without_ticker(mock_yf_ticker, yf):
    mock_yf_ticker.news = dummy_news_1st

    assert yf.monitor_news() == []


def test_yf_with_ticker(mock_yf_ticker, yf):
    mock_yf_ticker.news = dummy_news_1st
    yf.set_ticker('AAPL')
    mock_yf_ticker.news = dummy_news_2nd

    assert yf.monitor_news() == result_2nd
