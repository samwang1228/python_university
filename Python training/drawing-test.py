import numpy as np 
from matplotlib import pyplot as plt 
#pip list 可檢查安裝的模組 
x = np.arange(0,11) #設定x軸範圍 不包括11
y =  2  * x +  5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") #x軸標題
plt.ylabel("y axis caption") #y軸標題
plt.plot(x, y,"oy") #o代表以圓圈顯示 b代表blue
plt.show()