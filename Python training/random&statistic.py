# import random
# data = random.choice([3, 5, 7, 8, 9])#隨機選取數
# data2 = random.sample([56, 7, 8, 99, 55, 789], 3)  #隨機選取n數
# print(data)
# print(data2)
# data3 = [6, 7, 8, 9, 56]
# random.shuffle(data3)#隨機對調
# print(data3)
# data4 = random.random()  #隨機得到0-1的亂數
# data5 = random.uniform(60, 700)  #隨機得到自訂範圍的亂數 
# print(data4, '\n', data5)
# data6 = random.normalvariate(100, 10)  #得到平均為100 標準差為10的亂數
# print(data6)
import statistics as s
num_list = [99,678,777]
# for i in range(3):由使用者輸入的方法
#     num_list += [int(input())]
average = s.mean(num_list)#得到平均數
print(average)
med = s.median(num_list)  #取得中位數
print(med)
stand = s.stdev(num_list) #取得標準差
print(stand)