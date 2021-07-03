#網路連線
import urllib.request as re
scr = "https://www.ntu.edu.tw/"
with re.urlopen(scr) as target:#可得到網站的原始碼(html)
    data = target.read().decode("utf-8")
print(data)