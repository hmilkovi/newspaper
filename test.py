from newspaper import Article as ArticleParser
from tor_manager import TorHandler

article = ArticleParser('https://www.24sata.hr/news/kaos-u-hong-kongu-policajci-pravim-mecima-na-prosvjednika-651379', MIN_WORD_COUNT=20)
article.download(proxy='http://127.0.0.1:8118', js=True, headless=False, sleep=1)
print(article.html)

TorHandler().new_ip()

article = ArticleParser('https://www.24sata.hr/news/kaos-u-hong-kongu-policajci-pravim-mecima-na-prosvjednika-651379test', MIN_WORD_COUNT=20)
article.download(proxy='http://127.0.0.1:8118', js=True, headless=False, sleep=1)
print(article.html)