from config import DEPTH_LIMIT

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
        
        self.run(depth+1)