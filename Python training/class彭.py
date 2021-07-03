class Point:
    def __init__(self,x,y):#like menber variable and constructor 
        self.x = x
        self.y = y
    def show(self):#like member fumction
        print(self.x, self.y)
    def distence(self,targetx, targety):
        return ((self.x-targetx)**2+(self.y-targety)**2)**0.5
p1 = Point(5, 6)
p1.show()
print(p1.distence(0, 0))
class File:
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, mode="r", encoding="utf-8")
    def read(self):
        return self.file.read()
    def close(self):
        self.file.close()
f1 = File("data1.txt")
f1.open()
print(f1.read())
f1.close()
f2 = File("data2.txt")
f2.open()
print(f2.read())
f2.close()

