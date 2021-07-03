import os
import time

context = '我愛吳棱恩.........'
while True:
    print(context)
    time.sleep(1)
    os.system('cls')
    context = context[1:] + context[0]
   

    
