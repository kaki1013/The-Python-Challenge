s = "http://www.pythonchallenge.com/pc/def/0.html"
idx = s.index('0')
s = s[:idx] + str(2**38) + s[idx+1:]
print(s)
# http://www.pythonchallenge.com/pc/def/274877906944.html