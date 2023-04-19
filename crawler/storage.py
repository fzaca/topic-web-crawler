import json
import logging, logging_config

def storage_content(data):
    try:
        with open('data/data.json', 'w') as f:
            json.dump(data, f)
        logging.info('Data file saved successfully.')
    except:
        logging.error('Not saving data file')

def storage_urls(urls):
    try:
        with open('data/urls.txt', 'w') as f:
            for url in urls:
                f.write(url + '\n')
        logging.info('URLs file saved successfully.')
    except:
        logging.error('Not saving URLs file')