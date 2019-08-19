import time

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
# attempt attempt realise Best practice with retries with requests
url = 'http://httpbin.org/'
HTTPMethods = 'get'


def get(url, HTTPMethods):
    try:
        responce = requests.get(url + HTTPMethods).text
        print(f"Try: {responce}")
        return requests.get((url + HTTPMethods))
    except Exception:
        # sleep for a bit in case that helps
        time.sleep(1)
        # try again
        print(f"Except: {responce}")
        return get(url)


if __name__ == '__main__':
    get(url, HTTPMethods)
