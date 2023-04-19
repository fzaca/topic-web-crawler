import sys
from crawler import Spider

if __name__ == '__main__':
    urls = sys.argv[1:]
    spider = Spider(start_urls=urls)
    spider.run()