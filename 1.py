# +2
s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
ans = []
for char in s:
    if ord('y') == ord(char):
        ans.append('a')
    elif ord('z') == ord(char):
        ans.append('b')
    elif ord('a') <= ord(char) <= ord('x'):
        change = ord(char) + 2
        ans.append(chr(change))
    else:
        ans.append(char)
print(''.join(ans))
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

s = "http://www.pythonchallenge.com/pc/def/map.html"
ans = []
for char in s:
    if ord('y') == ord(char):
        ans.append('a')
    elif ord('z') == ord(char):
        ans.append('b')
    elif ord('a') <= ord(char) <= ord('x'):
        change = ord(char) + 2
        ans.append(chr(change))
    else:
        ans.append(char)
print(''.join(ans))
# jvvr://yyy.ravjqpejcnngpig.eqo/re/fgh/ocr.jvon
# http://www.pythonchallenge.com/pc/def/ocr.html