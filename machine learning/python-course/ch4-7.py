class student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
        
    def average(self):
        return sum(self.marks) / len(self.marks)#sum()把裡面的list相加
        
rolf = student('Rolf', 'MIT')
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())  #(57+99)/2

class foo:
    @classmethod
    def hi(cls):#呼叫class的name 因為是class所以用cls簡寫
        print(cls.__name__)

my_object = foo().hi()

class Bar:
    @staticmethod  #連self都沒有
    def hi():
        print('Hello I don\'t take parameter .')
    
anthor_object = Bar()
anthor_object.hi()
