import re
import logging, logging_config
import xml.etree.ElementTree as ET

from collections import Counter
from bs4 import BeautifulSoup, Comment
from config import KEYWORDS

def parse_html(html):
    if is_xml(html):
        logging.warning('Skipping XML')
        return None, None

    soup = BeautifulSoup(html, 'html.parser')

    # Limpieza de los datos
    regex = r"<(script|style|meta|noscript)[^>]*>[\s\S]*?</\1>"
    clean_html = re.sub(regex, "", str(soup))
    soup = BeautifulSoup(clean_html, 'html.parser')

    # Obtencion de urls
    urls = []
    for link in soup.find_all('a', href=True):
        url = link.get('href')
        if url.startswith('http'):
            urls.append(url)

    title = soup.title.string if soup.title else ''
    text = soup.get_text()
    meta = soup.find('meta', attrs={'name': 'description'})

    data = {}

    data['title'] = title
    data['text'] = text

    freq = Counter(text.lower().split())
    if KEYWORDS:
        data['keyword_freq'] = {}
        for keyword in KEYWORDS:
            data['keyword_freq'][keyword.lower()] = freq[keyword]

    return urls, data

def is_xml(content):
    try:
        ET.fromstring(content)
        return True
    except ET.ParseError:
        return False