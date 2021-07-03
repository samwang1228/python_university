#myclass.py
# 我們想產生一個女性(Woman)類別包含著人類(Human)類別的所有特性，
# 女性(Woman)裡面具有三個屬性－ 胸圍(bust)、腰圍(waist)、臀圍(hip)，
# 兩個方法－初始化(__init__)與印出三圍(printBWH)
# super().__init__會呼叫基礎類別(Human)中的__init__
# 因為Woman繼承Human，所以可以使用Human中的屬性以及方法
class Human:
    def __init__(self,h=0,w=0):
        self.height=h
        self.weight=w
    def BMI(self):
        return self.weight / ((self.height/100)**2)

class Woman(Human):
    def __init__(self, high, weigh, bust=0, waist=0, hip=0):  #像是c++的contructor繼承 前兩數名稱不一定要照bass class
        super().__init__(high,weigh) #呼叫base constructor的{}
        self.bust=bust
        self.waist=waist
        self.hip=hip
    def printBWH(self):
        print("bust={},waist={},hip={}".format(self.bust,self.waist,self.hip))






# #main.py
# import myclass
a = Woman(165,54,83,64,84)
print(a.BMI())
a.printBWH()