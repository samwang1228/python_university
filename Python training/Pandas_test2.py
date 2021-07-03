import pandas as pd
#數字處理
# data = pd.Series([6, 8, -8, 689, 9])
# #print(data.sum(), data.prod())#相加總合 相乘總和
# #print(data.mean(), data.std())  #平均 標準差
# print(data.nlargest(3))  #前三大數 
# print(data.nsmallest(2))  #前兩小數
#字串處理
data =pd.Series(["你好", "Python", "Pandas"],index=["a","b","c"]) #可自行更改索引
print(data.str.lower()) #轉小寫
print(data.str.upper()) #轉大寫
print(data.str.len())  #每個字串長度
print(data.str.cat(sep="-"))  #以-合併字串
print(data.str.contains("P"))  #判斷是否有P
print(data.str.replace("你好", "Hello"))  #將你好取代成Hollo
data=data.str.replace("你好","Hollo")
print("資料型態", data.dtype)
print("資料數量", data.size)
print("資料索引", data.index)
print(data[0],data["a"])


