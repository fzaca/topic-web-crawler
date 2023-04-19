import json

def storage_content(data):
    try:
        with open('data/data.json', 'w') as f:
            json.dump(data, f)
    except:
        print("Error saving data file")

def storage_urls(urls):
    try:
        with open('data/urls.txt', 'w') as f:
            for url in urls:
                f.write(url + '\n')
    except:
        print("Error saving txt file")