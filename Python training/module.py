import sys as s#可自訂函式後再import
print(s.platform)#印出作業系統
print(s.maxsize)  #印出int最大值
#print(s.path)  #模組路徑
#s.path.append("modules")  #新增搜尋路徑
import modules.geometry as g #封包概念有了這個就不用新增路徑
#result = modules.geometry.slope(2, 6, 7, 8)
result = g.distence(2,8,9,5)
print(result)