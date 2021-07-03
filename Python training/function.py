def average(*Tuple):
    sum =0
    for x in Tuple:
        sum += x
    print(sum / len(Tuple))
average(5, 6)
average(7,8,9,10)
def add(x,y):
    return x+y
print(add(y=9, x=10))
t = [0]*6
for i in range(6):
    t[i] = input()
for i in range(6):
    print(t[i])