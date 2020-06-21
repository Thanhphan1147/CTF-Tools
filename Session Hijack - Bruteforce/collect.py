import requests
import re
import urllib.parse
import time

url = "http://192.168.238.142/WebGoat/attack"
login = ('root','owaspbwa')
session = requests.Session()
data = {'start': 'Start WebGoat'}
find = "Hijack a Session"

r1 = session.get(url, auth=login)
# print(r1.text)

r2 = session.post(url, data, auth=login)

# print(r2.text)

m = re.search("attack\?Screen=(\d+).*%s"%find, r2.text)
if not m is None:
    scr= m.group(1)

params = {'Screen': scr, 'menu': '1800'}
q = urllib.parse.urlencode(params)
    
nurl = f'{url}?{q}'
# print(url)

# print(time.time())
r3 = session.get(nurl)
# print(r3.text)
t = time.time()
# print(t)

# print(r3.cookies.get_dict())

for c in r3.cookies:
    a = str(c.value)
    print(a)

# print(int(la[1]))
# print(int(la[1]) - int(lt))
# print()
# r3.connection.close()
