import pandas as pd 
data = pd.DataFrame({
    "Name": ["Sam", "Gina", "John"],
    "salary":[1000000,500000,40000]
})
# print(data)
# print("資料數量", data.size)
# print("資料狀態(列,行)", data.shape)
# print("資料索引", data.index)
# print("取得第二列",data.iloc[1],sep="\n")
# names = data["Name"] #要先取得一維數據
# print("將Name轉大寫", names.str.upper(), sep="\n")
# salarys = data["salary"]
# print("薪水平均值", salarys.mean())
data["revenue"] = [2000000, 1000000, 50000]  #新增欄位
data["rank"] = pd.Series([1, 2, 3])  #較正式寫法
data["cp"] = data["revenue"]/data["salary"]  #將欄位新增且做運算
print(data)