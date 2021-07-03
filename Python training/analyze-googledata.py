import pandas as pd
data = pd.read_csv("googleplaystore.csv")#讀取csv檔
#分析
print("資料數量",data.shape)
print("資料欄位", data.columns)
print("=================")
print(data.describe())#列出所有統紀數據
# print(data["Rating"].corr())#相關係數()可放你想比較的
#print(data["Category"])
# for i in range(100):#9前100個app名稱
#     print(data["App"][i])
#print(data["Size"].mean())
#篩選 最大容量
# data["Size"] = data["Size"].str.replace("M", "000").replace("Varies with device", "")#將M取代至000而亂碼將他換置成空
# data["Size"] = data["Size"].str.replace("[k,+]", "")
# data["Size"]=pd.to_numeric(data["Size"],downcast="integer")#轉成數字 且為整數
# condition = data["Size"] == 100000.0 
# print(data[condition])
#print(data["Size"].max(), "kB")
#篩選評分
# lowdata=data
# condition = data["Rating"] == 1.0 #過濾錯誤評分(大於5)
# lowdata = data[condition]  #取代
# print(lowdata["App"])  #搜尋評分最低的app
# condition = data["Rating"] <= 5.0  #過濾錯誤評分(大於5)
# rate_5_data=data
# rate_5_data = rate_5_data[condition]  #取代
# print(rate_5_data["Rating"].mean())  #平均星星
# print(rate_5_data["Rating"].median()) #中位數
# print(rate_5_data["Rating"].max())
# print(rate_5_data["Rating"].min())
# #篩選下載率
# #print(data["Installs"])
# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[+,]", "").replace("Free",""))
# print("平均下載率",data["Installs"].mean())
# print("最小下載率", data["Installs"].min())
# print("最小下載率App資訊", data.iloc[data["Installs"].argmin()], sep="\n")
# condition = data["Installs"] >= 100000
# install_data=data
# install_data =install_data[condition]
# print("安裝數大於一萬的程式有", install_data["Installs"].shape[0], "個")
#搜尋你想要的app
# keyboard = input("請輸入關鍵字:")
# condition = data["App"].str.contains(keyboard,case=False)#代表忽略大小寫
# print(data[condition]["App"])


