from feedparser import parse

RSS_SOURCES = [
    {
        "id": "1",
        "name": "CNN",
        "url": "http://rss.cnn.com/rss/cnn_topstories.rss"
    }
]


class RSS:
    def __init__(self, id, name, url):
        self.id = id
        self.name = name
        self.url = url
        self.feed = parse(url)

