import sys, signal

from config import DEPTH_LIMIT, KEYWORDS, MIN_KEYWORD_OCCURRENCES
from .downloader import downloader
from .parser import parse_html
from .storage import storage_content, storage_urls

class Spider:
    def __init__(self, start_urls):
        self.urls = start_urls
        self.visited_urls = set()
        self.storage_urls = []

        self.data = []

        # Señal de interrupcion (Ctrl+C)
        signal.signal(signal.SIGINT, self.end)

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
            # Storage
            if KEYWORDS:
                cant = sum(data['keyword_freq'].values())
                if cant >= MIN_KEYWORD_OCCURRENCES:
                    self.data.append(data)
                    self.storage_urls.append(url)
            else:
                self.data.append(data)
                self.storage_urls.append(url)

            self.urls += new_urls
        
        self.run(depth+1)

    def end(self, signal, frame):
        storage_content(self.data)
        storage_urls(self.storage_urls)
        sys.exit(0)