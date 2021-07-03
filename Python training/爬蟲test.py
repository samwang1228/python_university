import urllib.request as req
url="https://www.ptt.cc/bbs/Tech_Job/M.1583592401.A.5A6.html"
#建立request物件,附加headers的資訊
request = req.Request(url, headers={ #取得使用權 F12 >>Network >>重新整理  >>headers >> user-agent >>取得Mozil....
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
import bs4
with open("data", mode="a", encoding="utf-8") as file:#mode="a"才能寫入所有
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("span", class_="f3 push-content") #尋找所有class=title 的span標籤 這裡很重要 span與f3..需自己找
    for title in titles:
        #print(title.string)
        con=title.string
        file.write(con+"\n")
