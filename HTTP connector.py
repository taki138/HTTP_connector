import time
import requests

def get(url):
    try:
        return requests.get(url)
    except Exception:
        # sleep for a bit in case that helps
        time.sleep(1)
        # try again
        return get(url)
    xc