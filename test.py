from newspaper import Article as ArticleParser

article = ArticleParser('https://www.24sata.hr/news/kaos-u-hong-kongu-policajci-pravim-mecima-na-prosvjednika-651379', MIN_WORD_COUNT=20)
article.download(proxy='http://127.0.0.1:8118', js=True, headless=False, sleep=10)
print(article.html)

article = ArticleParser('https://www.24sata.hr/news/kaos-u-hong-kongu-policajci-pravim-mecima-na-prosvjednika-651379test', MIN_WORD_COUNT=20)
article.download(proxy='http://127.0.0.1:8118', js=True, headless=False, sleep=10)
print(article.html)