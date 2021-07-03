import pygame as pg
import random
import math
import time
import random 
#       0
#0      -> +           get_width()
#       get_hight()
#建立球體
print("You want to play easy mode or difficult mode")
s=input()
s2=input("you want to fast mode or normal mode or slow mode\n")
Type=0
speed_fast=0
if s=='easy':
    Type=1
elif(s=='difficult'):
    Type=2
if(s2=='fast'):
    speed_fast=2
elif(s2=='slow'):
    speed_fast=1
class Ball(pg.sprite.Sprite):
    dx = 0         #x位移量
    dy = 0         #y位移量
    x = 0          #球x坐標
    y = 0          #球y坐標
    direction = 0  #球移動方向
    speed = 0      #球移動速度
 
    def __init__(self, sp, srx, sry, radium, color):
        pg.sprite.Sprite.__init__(self)
        self.speed = sp
        self.x = srx
        self.y = sry
        #繪製球體
        self.image = pg.Surface([radium*2, radium*2])#寬 長  
        self.image.fill((41,36,33))
        pg.draw.circle(self.image, color, (radium,radium), radium, 0)
        #pygame.draw.circle(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
        self.rect = self.image.get_rect()  #取得球體區域
        self.rect.center = (srx,sry)       #初始位置
        self.direction = random.randint(30,70)  #移動角度

 #球體移動 
    def update(self):         
        radian = math.radians(self.direction)    #角度轉為弳度
        self.dx = self.speed * math.cos(radian)  #球水平運動速度
        self.dy = -self.speed * math.sin(radian) #球垂直運動速度 因為最上面為0
        self.x += self.dx     #計算球新坐標
        self.y += self.dy
        self.rect.x = self.x  #移動球圖形
        self.rect.y = self.y
        #到達左右邊界
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()-10):  
            self.bouncelr()
        elif(self.rect.top <= 10):  #到達上邊界
            self.y+=20
            self.bounceup()
        if(self.rect.bottom >= screen.get_height()-10):  #到達下邊界出界
            return True
        else:
            return False
 
    def bounceup(self):  #上邊界反彈
        self.direction = 359- self.direction
        #360 - self.direction

    def bouncelr(self):  #左右邊界反彈
        self.direction =(180-self.direction)%360 
        #(180 - self.direction) % 360

#磚塊類別            
class Brick(pg.sprite.Sprite):
    def __init__(self, color, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([38, 13])  #磚塊長寬38x13
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#板子類別
class Pad(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('test.jpg')  #滑板圖片
        self.image = pg.transform.scale(self.image, (50, 5))#更改照片大小
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)#滑板初始位置中間
        self.rect.y = screen.get_height() - self.rect.height - 30 #一開始的y方向
        
#板子位置隨滑鼠移動 
    def update(self):  
        pos = pg.mouse.get_pos()  #[0]為x [1]為y
        self.rect.x = pos[0]       #滑鼠x坐標
        #self.rect.y=pos[1]
        #不要移出右邊界
        if self.rect.x > screen.get_width() - self.rect.width:
            self.rect.x = screen.get_width() - self.rect.width

#結束程式
def gameover(message): 
    global running
    #顯示訊息
    text = ffont.render(message, 1, (255,0,255))  
    screen.blit(text, (screen.get_width()/2-150,screen.get_height()/2-20))
    pg.display.update()  #更新畫面
    time.sleep(3)        #暫停3秒    
    running = False      #結束程式

pg.init()
score = 0  #得分
dfont = pg.font.SysFont("Arial", 20)    #下方訊息字體
ffont = pg.font.SysFont("SimHei", 32)   #結束程式訊息字體
soundhit = pg.mixer.Sound("explosion.wav")  #碰到磚塊音效
#soundpad = pg.mixer.Sound("explosion.wav")  #碰到滑板音效
#背景
screen = pg.display.set_mode((600, 400))
pg.display.set_caption("打磚塊好好玩")
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((21,20,20))
#background = pg.image.load('pg.png')
#background = pg.transform.scale(background , (600, 400))
#background = pg.Surface(screen.get_size())
allsprite = pg.sprite.Group()  #建立全部角色群組
bricks = pg.sprite.Group()     #建立磚塊角色群組
ball = Ball(15, random.randint(100, 300), 350, 10, (255,123,188)) #建立粉球
if(Type==2):
    ball2 = Ball(10, 200, 350, 10, (25,123,188))
    allsprite.add(ball2)
allsprite.add(ball)  #加入全部角色群組
pad = Pad()          #建立滑板球物件
allsprite.add(pad)   #加入全部角色群組

#建立磚塊
for row in range(0, 5):          #5列方塊
    for column in range(0, 15):  #每列15磚塊
        if row == 1 or row == 0: 
            brick = Brick((153,205,255), column * 40 + 1, row * 15 + 1)   #位置為40*15
        if row == 2: 
            brick = Brick((94,175,254), column * 40 + 1, row * 15 + 1)    
        if row == 3 or row == 4:  
            brick = Brick((52,153,207), column * 40 + 1, row * 15 + 1)  
        bricks.add(brick)     #加入磚塊角色群組
        allsprite.add(brick)  #加入全部角色群組
        
clock = pg.time.Clock()        
downmsg = "Press Left Click Button to start game!"  #起始訊息
playing = False  #開始前球不會移動
running = True

#運行的程式碼
while running:
    if(speed_fast==2):
        clock.tick(50) #每秒畫幾次
    elif(speed_fast==0):
        clock.tick(20) #每秒畫幾次
    elif(speed_fast==1):
        clock.tick(10) #每秒畫幾次
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    buttons = pg.mouse.get_pressed()  #檢查滑鼠按鈕
    if buttons[0]:            #按滑鼠左鍵後球可移動       
        playing = True
        
    #遊戲進行中
    if playing == True:  
        screen.blit(background, (0,0))  #清除繪圖視窗
        fail = ball.update()  #移動球體
        if fail:              #球出界
            gameover("You failed! See you next time~")
        if(Type==2):
             fail2 = ball2.update()  #移動球體
             if fail2:              #球出界
                 gameover("You failed! See you next time~")
        pad.update()          #更新滑板位置
        #檢查球和磚塊碰撞
        hitbrick = pg.sprite.spritecollide(ball, bricks, True)  
        if len(hitbrick) > 0:  #球和磚塊發生碰撞
            score += len(hitbrick)  #計算分數
            soundhit.play()    #球撞磚塊聲
            ball.rect.y += 20  #球向下移
            ball.bounceup()    #球反彈
            if len(bricks) == 0:  #所有磚塊消失
                gameover("          Congratulations!!")
        #檢查球和滑板碰撞
        if(Type==2):
            hitbrick2 = pg.sprite.spritecollide(ball2, bricks, True)  
            if len(hitbrick2) > 0:  #球和磚塊發生碰撞
                score += len(hitbrick2)  #計算分數
                soundhit.play()    #球撞磚塊聲
                ball2.rect.y += 21  #球向下移
                ball2.bounceup()    #球反彈
                if len(bricks) == 0:  #所有磚塊消失
                    gameover("Congratulations!!")
        #檢查球和滑板碰撞
        hitpad = pg.sprite.collide_rect(ball, pad) 
        if hitpad:  #球和滑板發生碰撞
            #soundpad.play()  #球撞滑板聲
            ball.bounceup()  #球反彈
        allsprite.draw(screen)  #繪製所有角色
        downmsg = "Score: " + str(score)
    #繪製下方訊息 
        if(Type==2):
            hitpad2 = pg.sprite.collide_rect(ball2, pad)
            if hitpad2:  #球和滑板發生碰撞
                #soundpad.play()  #球撞滑板聲
                ball2.bounceup()  #球反彈
        allsprite.draw(screen)  #繪製所有角色
        downmsg = "Score: " + str(score)
    message = dfont.render(downmsg, 1, (255,0,255))
    screen.blit(message, (screen.get_width()/2-125,screen.get_height()-30))
    pg.display.update()
pg.quit()