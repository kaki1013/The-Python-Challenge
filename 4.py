"""
페이지 소스의 힌트: urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough.
풀이: 가운데 사진 누르면 아래 링크로 연결되고 그 아래 문구가 나옴
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
and the next nothing is 44827
이를 반복하여 아래의 링크로 이동하고 이를 반복
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827
아마 400번 반복이면 충분
"""
import urllib.request


def next_number(link):
    response = urllib.request.urlopen(link)
    html = response.read()
    nxt = str(html).split()[-1][:-1]
    return nxt


url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"

for i in range(400):
    go = url + nothing
    nothing = next_number(go)
#     print(i, nothing)
# i = 85: 16044 (Yes. Divide by two and keep going.: 반 나누고 똑같이 진행)
# i = 233: 66831
# i = 381: 66831

# ans = peak.html
# http://www.pythonchallenge.com/pc/def/peak.html
