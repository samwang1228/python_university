import pygame as pg
import math
import random
pg.init()
#設定視窗背景
width, height = 640, 480                      
screen = pg.display.set_mode((width, height))   
pg.display.set_caption("沒有意義")         
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))

#藍球建立

ball1 = pg.Surface((70,70))
ball1.fill((255,255,255)) #背景顏色]
pg.draw.circle(ball1, (0,0,255), (35,35), 35, 0)
rect1 = ball1.get_rect()
rect1.center = (random.randint(100,250),random.randint(150,250))       #球隨機起始位置
x1, y1 = rect1.topleft                #球左上角坐標
direction1 = random.randint(50,70)  #起始角度 random.randint(a, b) 回傳一個整數 N (a <= N <= b)。
radian = math.radians(direction1 )  #轉為弳度
dx1 = 5 * math.cos(radian)          #球水平運動速度
dy1 = -5 * math.sin(radian)  #球垂直運動速度

ball2 = pg.Surface((70,70))
ball2.fill((255,255,255))
pg.draw.circle(ball2, (0,255,0), (35,35), 35, 0)
rect2 = ball2.get_rect()
rect2.center = (random.randint(250,300),random.randint(250,300))       #球隨機起始位置
x2, y2 = rect2.topleft                #球左上角坐標
direction = random.randint(20,70)  #起始角度 random.randint(a, b) 回傳一個整數 N (a <= N <= b)。
radian = math.radians(direction )  #轉為弳度
dx2 = 5 * math.cos(radian)          #球水平運動速度
dy2 = -5 * math.sin(radian)         #球垂直運動速度

clock = pg.time.Clock()
#關閉程式的程式碼
running = True
while running:
    clock.tick(60)        #每秒執行30次
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    x1 += dx1  #改變水平位置
    y1 += dy1  #改變垂直位置
    rect1.center = (x1,y1)
    if(rect1.left <= 0 or rect1.right >= screen.get_width()):       #到達左右邊界
        dx1 *= -1    #水平速度變號
    elif(rect1.top <= 1 or rect1.bottom >= screen.get_height()-1):  #到達上下邊界
        dy1 *= -1    #垂直速度變號
    x2 += dx2  #改變水平位置
    y2 += dy2  #改變垂直位置
    rect2.center = (x2,y2)
    if(rect2.left <= 0 or rect2.right >= screen.get_width()):       #到達左右邊界
        dx2 *= -1    #水平速度變號
    elif(rect2.top <= 1 or rect2.bottom >= screen.get_height()-1):  #到達上下邊界
        dy2 *= -1  #垂直速度變號
    # if ((x1 + 35 == x2 - 35 and y1-35 == y2+35) or (x1 - 35 == x2 + 35 and y1-35 == y2+35)):
    #     dx1 *= -1
    #     dx2 *= -1
    # if ((x1 + 35 == x2 - 35 and y1+35 == y2-35) or (x1 - 35 == x2 + 35 and y1+35 == y2-35)):
    #     dx1 *= -1
    #     dx2 *= -1
    # if ((y1 + 35 == y2 - 35 and x1 == x2) or (y1 - 35 == y2 + 35 and x1 == x2)):
    #     dy1 *= -1
    #     dy2 *= -1
    screen.blit(bg, (0,0))
    screen.blit(ball1, rect1.topleft)
    screen.blit(ball2, rect2.topleft)
    pg.display.update()    
pg.quit()