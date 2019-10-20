import urllib.parse
import urllib.request

url = 'https://httpbin.org/headers'
# values = {'argument1': 'value1', 'argument2': 'value2'}
headers = {'User-Agent': 'python urllib'}
# data = urllib.parse.urlencode(values)
# byte_data = data.encode('ASCII')
req = urllib.request.Request(url)

# return http.client.HTTPResponse object
response = urllib.request.urlopen(req)
print(response)

# functions http.client.HTTPResponse object
print(response.geturl())
print(response.info())
print(response.getcode())
