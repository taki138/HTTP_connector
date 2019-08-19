import time
import requests

url = 'http://httpbin.org/'
HTTPMethods = 'get'


def get(url, HTTPMethods):
    try:
        print(requests.get(url + HTTPMethods))
        return requests.get((url + HTTPMethods))
    except Exception:
        # sleep for a bit in case that helps
        time.sleep(1)
        # try again
        print(requests.get(url))
        return get(url)


if __name__ == '__main__':
    get(url, HTTPMethods)
