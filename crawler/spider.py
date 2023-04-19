import sys, signal

from config import DEPTH_LIMIT
from .downloader import downloader
from .parser import parse_html
from .storage import storage_content, storage_urls

class Spider:
    def __init__(self, start_urls):
        self.urls = start_urls
        self.visited_urls = set()

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
            self.data.append(data)

            self.urls += new_urls
        
        self.run(depth+1)

    def end(self, signal, frame):
        storage_content(self.data)
        storage_urls(self.visited_urls)
        sys.exit(0)