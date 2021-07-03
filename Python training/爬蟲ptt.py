import urllib.request as req
def getData(url):
    #建立request物件,附加headers的資訊
    request = req.Request(url, headers={ #取得使用權 F12 >>Network >>重新整理  >>headers >> user-agent >>取得Mozil....
        "cookie": "over18=1",  #如果18禁網站則需cookie 一樣在Network可找到
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title") #尋找所有class=title 的span標籤 這裡很重要 span與f3..需自己找
    test=False
    for title in titles:
        if title.a != None and "台灣" in title.a.string  :  # 如果標包含a標籤(沒有被刪除),印出來
           print(title.a.string)
           test = True
    #抓取上一頁的連結
    Next_Link = root.find("a", string="‹ 上頁")  #點選想要的並按檢查
    if test:
        print("https://www.ptt.cc"+Next_Link["href"])  
    return Next_Link["href"]  #字典得到網址
count = 0
PageUrl = "https://www.ptt.cc/bbs/Gossiping/index.html"
while count<30:#選擇頁數
    PageUrl = "https://www.ptt.cc" + getData(PageUrl)  #將上頁的網址覆蓋並再次呼叫函式
    count+=1 
