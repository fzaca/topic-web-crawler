from config import DEPTH_LIMIT
from .downloader import downloader
from .parser import parse_html
from .storage import storage

class Spider:
    def __init__(self, start_urls):
        self.urls = start_urls
        self.visited_urls = set()

    def run(self, depth=0):
        if depth > DEPTH_LIMIT:
            return

        for url in self.urls:
            if url in self.visited_urls:
                continue
            self.visited_urls.add(url)
            # Download
            html = downloader(url)
            # Parse
            new_urls, data = parse_html(html)
            print(data['word_freq'])
            # Storage

            self.urls += new_urls
        
        self.run(depth+1)