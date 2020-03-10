import requests
r = requests.get('https://www.onemarketing.dk/')
print(r)
print(r.text)

# all available methods for requests
print(dir(r))
print(r.apparent_encoding)
print(r.close)
print(r.connection)
print(r.content)
print(r.cookies)
print(r.elapsed)
print(r.encoding)
print(r.headers)
print(r.history)
print(r.is_permanent_redirect)
print(r.is_redirect)
print(r.iter_content)
print(r.iter_lines)
print(r.json)
print(r.links)
print(r.next)
print(r.ok)
print(r.raise_for_status)
print(r.raw)
print(r.reason)
print(r.request)
print(r.status_code)
print(r.text)
print(r.url)

# detailed help with information about all methods
print(help(r))

# downloading binary files
r = requests.get('https://assets.amuniversal.com/2e79f5503b150138eb72005056a9545d')
print(r.status_code)
print(r.ok)
print(r.headers)
with open('downloaded-image.gif', 'wb') as f:
    f.write(r.content)

# get requests
payload = {'page': 1, 'count': 2}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)

# post requests
payload = {'username': 'marek', 'password': '12345'}
r = requests.post('https://httpbin.org/post', data=payload)

response_dictionary = r.json()
print(response_dictionary['form'])

# authentication
username = response_dictionary['form']['username']
password = response_dictionary['form']['password']
r = requests.get(f'https://httpbin.org/basic-auth/{username}/{password}')
print(r.status_code) # 401

r = requests.get(f'https://httpbin.org/basic-auth/{username}/{password}', auth=('marek','12345'))
print(r.status_code) # 200

r = requests.get('https://httpbin.org/delay/2', timeout=3)
print(r.status_code)
try:
    r = requests.get('https://httpbin.org/delay/2', timeout=1)
except requests.exceptions.ReadTimeout as e:
    print('Request timed out. Details:', e)
else:
    print(r.status_code)
