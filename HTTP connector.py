import time

import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

# attempt attempt realise Best practice with retries with requests
url = 'http://httpbin.org/'
HTTPMethods = 'delete'


def requests_retry_session(
        retries=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
        session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


response = requests_retry_session().get(url + HTTPMethods)
print(response.text)

if __name__ == '__main__':
    # requests_retry_session()
    s = requests.Session()
    s.auth = ('user', 'pass')
    s.headers.update({'x-test': 'true'})

response = requests_retry_session(session=s).get(url + HTTPMethods)


