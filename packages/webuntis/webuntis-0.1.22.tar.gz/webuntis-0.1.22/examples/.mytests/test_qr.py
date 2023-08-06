from urllib.parse import parse_qs, urlparse
import webuntis

sampleQR="untis://setschool?url=urania.webuntis.com&school=htl3r&user=HOR&key=ZXZJLM5J3YBONH5V&schoolNumber=7088200"
u = urlparse(sampleQR)
p = parse_qs(u.query)

credentials = {
    'username': p['user'][0],
    'password': p['key'][0],
    'server': p['url'][0],
    'useragent': 'time',
    'school': p['school'][0]
}

print(f"{credentials} = ")
print("------ Login")
with webuntis.Session(**credentials).login() as s:
    print("logged in", s)
