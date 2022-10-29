import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(len(res.text))
print(res.text[:50])

# print(res.raise_for_status())
# res2 = requests.get('https://automatetheboringstuff.com/files/ab.txt')
# print(res2.status_code)
# print(res2.raise_for_status())

# =======================================================================

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    print(playFile.write(chunk))
playFile.close()
