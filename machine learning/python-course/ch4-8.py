class fixfloat:
    def __init__(self, amount):
        self.amount = amount
        
    def __repr__(self):
        return f'<fixfloat {self.amount:.2f}>'

    # @staticmethod
    # def from_sum(value1, value2): #self like this
    #     return fixfloat(value1 + value2)
    @classmethod
    def from_sum(cls,value1, value2): #self like this
        return cls(value1 + value2)
        
number = fixfloat.from_sum(18.789, 0.785)
print(number)

class euro(fixfloat):
    def __init__(self, amount):
      super().__init__(amount)
      self.symbol = '$'
      
    def __repr__(self):
        return f'<USA {self.symbol}{self.amount:.2f}>'

money = euro.from_sum(16.890, 9.677)#此時如果base function是用static那麼它的repr會變成base的要改成classmethon才形
print(money)

