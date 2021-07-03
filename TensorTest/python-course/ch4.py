class student:
    def __init__(self, name):
        self.name = name
movies = ['Matrix', 'Finding Nemo']

class garage:
    def __init__(self):
       self.car = []
    def __len__(self):#要有這個len(object才有用)
        return len(self.car)
    def __getitem__(self, i):
        return self.car[i]

ford = garage()
ford.car.append('fiesto')
ford.car.append('focus')

print(ford[0])#得到car的len
