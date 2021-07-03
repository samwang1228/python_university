#儲存檔案 mode="w"
# file = open("data.txt", mode="w",encoding="utf-8")#開啟 檔名 模式 中文編碼
# file.write("hollo world\nsecond line\n中文測試")#寫入
# file.close()  #關閉
with open("data.txt", mode="w", encoding="utf-8") as file:  #開啟 檔名 模式 中文編碼 此方法會自動close
    #file.write("hollo world\nsecond line\n中文測試2")  #寫入
    file.write("3\n5")
#讀取檔案 mode="r"
sum=0
with open("data.txt", mode="r", encoding="utf-8") as file:
    #data = file.read()一次讀入所有
    for line in file:#一行一行讀取
        sum+=int(line)
print(sum)