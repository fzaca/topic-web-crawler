from urllib.request import urlopen
from urllib.error import URLError

def downloader(url):
    try:
        with urlopen(url) as session:
            html = session.read()
            return html
    except URLError as e:
        print(f"Error al descargar la página: {e}")
        return None