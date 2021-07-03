import pandas as pd
# x=[]
# for i in range(3):
#     x += [int(input())]
# data = pd.Series([8,9,7])
# #print(data)
# print("Max=", data.max())
# print("Median=", data.median())
# print("Min=", data.min())
# data = data * 5 #直接對列表中所有值做運算
# print(data)
# data = data == 35#對列表中的值尋找是否有35的有True反之False
#print(data)
data = pd.DataFrame({
    "Name": ["Sam", "Gina", "John"],
    "Salary":[10000000,300000,6]
})
print(data)
print(data["Name"])  #指定欄位
print("---------")
print(data.iloc[0])  #指定列數

