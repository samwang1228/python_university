class student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
        
    def average(self):
        return sum(self.marks) / len(self.marks)#sum()把裡面的list相加
        
class WorkingStudent(student):
    def __init__(self, name, school, salary):
        super().__init__(name, salary) #contructor的繼承 super means student
        self.salary = salary
    @property
    def weekly_salary(self): #no argument(parameter) can use property
        return self.salary*37.5
        
rolf = WorkingStudent('Rolf', 'MIT', 15.50)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())  #(57+99)/2
print(rolf.weekly_salary)#有property就不用()
