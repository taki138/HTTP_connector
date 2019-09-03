import sys
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

# Словарь в качестве аргумента через **arguments
# Так вы сможете передавать в функцию разное количество аргументов ключевых слов.
# В качестве аргументов ключевых слов можно также передавать и значения словаря:
# def myfunc(**arguments):
#  return arguments[‘key’]


# realise Best practice with retries with requests
url = 'http://httpbin.org/'
HTTPMethods = 'status/504'

stat_forcelist = (500, 502, 504)


def requests_retry_session(
        retries=6,
        backoff_factor=0.6,
        status_forcelist=stat_forcelist,
        session=None,
        raise_on_status=True

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
    print(session)
    return session


t0 = time.time()
try:
    response = requests_retry_session().get(
        url + HTTPMethods,
        timeout=5
    )

    print(f'\t Function requests_retry_session: started')
except Exception as x:
    print(f'\t Function requests_retry_session error occurred: \n \t {x}')
else:
    print('\t Function: requests_retry_session: \n \t response.status_code', response.status_code)
finally:
    t1 = time.time()
    print('\t Function requests_retry_session worked time:', t1 - t0, 'seconds')

# if __name__ == '__main__':
#     # requests_retry_session()
#     s = requests.Session()
#     s.auth = ('user', 'pass')
#     s.headers.update({'x-test': 'true'})

# response = requests_retry_session(session=s).get(url + HTTPMethods)
