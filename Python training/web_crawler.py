# str="Hello World"替換字串的方法
# str=str.replace("Hello ", "")
# print(str)
import urllib.request as req
for i in range(1, 50):#選擇頁數
    pa=str(i)
    url = "https://www.ptt.cc/bbs/movie/index"+pa+".html"
    #建立request物件,附加headers的資訊
    request = req.Request(url, headers={ #取得使用權 F12 >>Network >>重新整理  >>headers >> user-agent >>取得Mozil....
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    import bs4
    with open("data", mode="a", encoding="utf-8") as file:#mode="a"才能寫入所有
        root = bs4.BeautifulSoup(data, "html.parser")
        titles = root.find_all("div", class_="title") #尋找所有class=title 的div標籤
        for title in titles:
            if title.a != None :  #如果標題包含a標籤(代表沒刪除) 輸出
                con=title.a.string
                file.write(con+"\n")
