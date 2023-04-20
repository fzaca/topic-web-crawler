import logging, logging_config

from urllib.request import urlopen
from urllib.error import URLError

def downloader(url):
    try:
        logging.info('Downloading: %s', url[:50] + '...' if len(url) > 50 else url)
        with urlopen(url) as session:
            html = session.read()
            return html
    except URLError as e:
        logging.error('Downloading: %s', url)
        return None