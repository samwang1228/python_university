import pandas as pd
#數字
data = pd.Series([4, 800, 900])
condition = data >= 800
print(condition)
print(data[condition])  #篩選大於800的資料
#字串
data = pd.Series(["hollo", "python", "pandas"])
condition = data.str.contains("p")
print(data[condition])
#dataframe
data = pd.DataFrame({
    "name": ["sam", "gina", "john"],
    "salary": [90000000, 8999999, 7878787]
})
sa=data["salary"]
condition = data["salary"]>sa[2]
print(data[condition])
condition = data["name"] == "sam"
print(data[condition])