from typing import List

from pydiscord.yf.yf import YFNews

dummy_thumbnail_url = 'https://dummy'

dummy_news_1st: List[dict] = [{
    'uuid': '5772bc94-ace9-30a9-8df3-fa125e5947ee',
    'title': "Daniel Loeb's Strategic Embrace of Apple Inc in Q2 2024",
    'publisher': 'GuruFocus.com',
    'link': 'https://finance.yahoo.com/news/daniel-loebs-strategic-embrace-apple-035347543.html',
    'providerPublishTime': 1723694027,
    'type': 'STORY',
    'thumbnail': {
        'resolutions': [{
            'url': dummy_thumbnail_url, 'width': 1242, 'height': 902, 'tag': 'original'
        }, {
            'url': dummy_thumbnail_url, 'width': 140, 'height': 140, 'tag': '140x140'}]
    },
    'relatedTickers': ['AAPL']
}, {
    'uuid': '583c020e-dfc5-3cad-ae54-4aba890763eb',
    'title': 'Berkshire Might Be Finished Selling Apple Stock, With a Stake at Exactly 400 Million Shares',
    'publisher': 'Barrons.com',
    'link': 'https://finance.yahoo.com/m/583c020e-dfc5-3cad-ae54-4aba890763eb/berkshire-might-be-finished.html',
    'providerPublishTime': 1723690680,
    'type': 'STORY',
    'thumbnail': {
        'resolutions': [{
            'url': dummy_thumbnail_url, 'width': 140, 'height': 140, 'tag': '140x140'}]
    },
    'relatedTickers': ['AAPL']
}, {
    'uuid': '9313dd35-6487-334e-a749-78e714381b06',
    'title': 'Warren Buffett Bet On Ulta Beauty, Heico in Q2. See How His Portfolio Changed.',
    'publisher': 'Investopedia',
    'link': 'https://finance.yahoo.com/m/9313dd35-6487-334e-a749-78e714381b06/warren-buffett-bet-on-ulta.html',
    'providerPublishTime': 1723680364,
    'type': 'STORY',
    'thumbnail': {
        'resolutions': [{
            'url': dummy_thumbnail_url, 'width': 3000, 'height': 2000, 'tag': 'original'
        }, {
            'url': dummy_thumbnail_url, 'width': 140, 'height': 140, 'tag': '140x140'}]
    },
    'relatedTickers': ['AAPL', 'ULTA', 'HEI-A', 'CVX']
}]

dummy_news_2nd: List[dict] = [{
    'uuid': '4a48859c-d12a-303a-9d78-321987a6270e',
    'title': "Warren Buffett's Major Portfolio Reshuffle: A Deep Dive into Apple's 20.13% Reduction",
    'publisher': 'GuruFocus.com',
    'link': 'https://finance.yahoo.com/news/warren-buffetts-major-portfolio-reshuffle-220124017.html',
    'providerPublishTime': 1723672884,
    'type': 'STORY',
    'thumbnail': {
        'resolutions': [{
            'url': dummy_thumbnail_url, 'width': 1242, 'height': 902, 'tag': 'original'
        }, {
            'url': dummy_thumbnail_url, 'width': 140, 'height': 140, 'tag': '140x140'}]
    },
    'relatedTickers': ['AAPL', 'CVX']
}, {
    'uuid': 'b9e9154b-c9e5-3ab5-8fa3-f1af994ec2ca',
    'title': "Warren Buffett's Firm Chops Apple Position, Enters Holdings in Ulta Beauty and Heico",
    'publisher': 'GuruFocus.com',
    'link': 'https://finance.yahoo.com/news/warren-buffetts-firm-chops-apple-220124490.html',
    'providerPublishTime': 1723672884,
    'type': 'STORY',
    'thumbnail': {
        'resolutions': [{
            'url': dummy_thumbnail_url, 'width': 770, 'height': 433, 'tag': 'original'
        }, {
            'url': dummy_thumbnail_url, 'width': 140, 'height': 140, 'tag': '140x140'}]
    },
    'relatedTickers': ['ULTA', 'HEI-A', 'AAPL', 'CVX']
}]

result_1st = [
    YFNews(
        uuid='5772bc94-ace9-30a9-8df3-fa125e5947ee',
        title="Daniel Loeb's Strategic Embrace of Apple Inc in Q2 2024",
        publisher='GuruFocus.com',
        link='https://finance.yahoo.com/news/daniel-loebs-strategic-embrace-apple-035347543.html',
        relatedTickers=['AAPL'],
    ),
    YFNews(
        uuid='583c020e-dfc5-3cad-ae54-4aba890763eb',
        title='Berkshire Might Be Finished Selling Apple Stock, With a Stake '
              'at Exactly 400 Million Shares',
        publisher='Barrons.com',
        link='https://finance.yahoo.com/m/583c020e-dfc5-3cad-ae54-4aba890763eb/berkshire-might-be-finished.html',
        relatedTickers=['AAPL'],
    ),
    YFNews(
        uuid='9313dd35-6487-334e-a749-78e714381b06',
        title='Warren Buffett Bet On Ulta Beauty, Heico in Q2. See How His Portfolio Changed.',
        publisher='Investopedia',
        link='https://finance.yahoo.com/m/9313dd35-6487-334e-a749-78e714381b06/warren-buffett-bet-on-ulta.html',
        relatedTickers=['AAPL', 'ULTA', 'HEI-A', 'CVX'],
    )
]
result_2nd = [
    YFNews(
        uuid='4a48859c-d12a-303a-9d78-321987a6270e',
        title="Warren Buffett's Major Portfolio Reshuffle: A Deep Dive into Apple's 20.13% Reduction",
        publisher='GuruFocus.com',
        link='https://finance.yahoo.com/news/warren-buffetts-major-portfolio-reshuffle-220124017.html',
        relatedTickers=['AAPL', 'CVX'],
    ),
    YFNews(
        uuid='b9e9154b-c9e5-3ab5-8fa3-f1af994ec2ca',
        title="Warren Buffett's Firm Chops Apple Position, Enters Holdings in Ulta Beauty and Heico",
        publisher='GuruFocus.com',
        link='https://finance.yahoo.com/news/warren-buffetts-firm-chops-apple-220124490.html',
        relatedTickers=['ULTA', 'HEI-A', 'AAPL', 'CVX', ],
    ),
]

dummy_news_1st: List[dict] = dummy_news_1st
dummy_news_2nd: List[dict] = dummy_news_1st + dummy_news_2nd

result_yf_news_1st: List[YFNews] = result_1st
result_yf_news_2nd: List[YFNews] = result_1st + result_2nd
