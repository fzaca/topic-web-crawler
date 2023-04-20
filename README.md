# Topic Web Crawler

Este es un proyecto de web crawler en Python que busca palabras clave en sitios web y devuelve los resultados.

## Requisitos

Este proyecto requiere Python 3.5 o superior.

## Instalación

1. Descarga o clona el repositorio.
```
$ git clone https://github.com/Xukay101/topic-web-crawler.git
```

2. Instala los requisitos del proyecto con el siguiente comando:
```
$ pip install -r requirements.txt
```
## Configuración

El archivo de configuración `config.py` contiene los siguientes parámetros:

- `DEPTH_LIMIT`: profundidad máxima a la que el web crawler debe explorar los enlaces del sitio web. El valor por defecto es `2`, lo que significa que solo se descargará el contenido del sitio web original.
- `WAIT_TIME`: tiempo de espera en segundos entre cada solicitud. El valor por defecto es `0`.
- `KEYWORDS`: lista de palabras clave a buscar en el contenido del sitio web. Si esta lista está vacía, el web crawler no buscará palabras clave. El valor por defecto es una lista vacía.
- `MIN_KEYWORD_OCCURRENCES`: número mínimo de veces que una palabra clave debe aparecer en el contenido de un sitio web para que se guarde en el archivo JSON. El valor por defecto es `1`.
- `MAX_DOWNLOAD_TIME`: tiempo máximo en segundos permitido para descargar el contenido de un sitio web. Si el tiempo de descarga supera este límite, el web crawler lo considerará como un fallo de descarga. El valor por defecto es `5`.

## Ejecución

Para ejecutar el web crawler, simplemente ejecute el archivo `main.py` seguido de uno o varios URLs. Por ejemplo:
