import math
import random
import pygame
from pygame import mixer

from ryRealTimeAsr06_threading import ryAsrStream, ryGet1secSpeechAndRecogItWithProb
from ryRealTimeAsr06_threading import  ryQ, ryRecogQGet, ryStream

dataBasePath= '../ryData/'
# Intialize the pygame
pygame.init()

# create the screen
bg_length=800
bg_width=600
screen = pygame.display.set_mode((bg_length, bg_width))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Catch")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#here
# Player
playerImg = pygame.image.load('player_r.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Apples
appleImg = []
appleX = []
appleY = []
appleX_change = []
appleY_change = []
num_of_apples = 3

for i in range(num_of_apples):
    appleImg.append(pygame.image.load('apple.png'))
    appleX.append(random.randint(0, 736))
    appleY.append(random.randint(50, 150))
    appleX_change.append(2)
    appleY_change.append(20)

bulletImg = pygame.image.load(dataBasePath+'bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

global history
history=[]
global ttl_history
ttl_history=" "

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def ck_history(word):
	global ttl_history
	if len(history)==10:
		history[0]=history[1]
		history[1]=history[2]
		history[2]=history[3]
		history[3]=history[4]
		history[4]=history[5]
		history[5]=history[6]
		history[6]=history[7]
		history[7]=history[8]
		history[8]=history[9]
		history[9]=word
		ttl_history=" "
		for i in range(len(history)):
			ttl_history += history[i]+" "
	else:
		history.append(word)
		ttl_history += word +" "

def ryShow_recognition(x, y, recResult= None):
    
    if recResult=='_unknown_':
        recResult = ''
    
    score = font.render(f"{recResult}", True, (0, 255, 255))
    screen.blit(score, (x-50, y+50))

def show_score(x, y): #有
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text(): #有
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y): #有
    screen.blit(playerImg, (x, y))


def apple(x, y, i): #有
    screen.blit(appleImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(appleX, appleY, bulletX, bulletY): #有
    distance = math.sqrt(math.pow(appleX - bulletX, 2) + (math.pow(appleY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

import pygame.time as pgTime
ryClock= pgTime.Clock()
ryLoopRate= 30 # loop/sec 

recProbToConfirm= 0.2

# Game Loop
running = True
while running:

     # 掌握一下這個 while 迴圈的 循環速度 fps= frames (loops) per sec
    dt=  ryClock.tick(ryLoopRate)
    fps= ryClock.get_fps()
    #print(f'dt= {dt:.2f}, fps= {fps:.0f}')

        
    #< 語音辨識在此執行 ....，
    #y, prob= ryGet1secSpeechAndRecogItWithProb()
    
    #'ryQ', 'ryRecogQGet'
    yL= ryRecogQGet(ryQ)
    
    #print(yL)
    recResult= y= ''
    prob=0.0
    for y, prob in yL:
        
        recResult= y
  
        if prob > recProbToConfirm:
            
            if   y=='left':
                playerX_change = -1
                ck_history(y)
            elif y== 'right':
                playerX_change = +1
                ck_history(y)
            elif y== 'up':
                playerY_change = -1
                ck_history(y)            
            elif y== 'down':
                playerY_change = +1
                ck_history(y)   
            elif y in ['yes', 'on', 'go']:
                ck_history(y)
                if bullet_state == "ready":
                    bulletSound = mixer.Sound(dataBasePath+"laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    bulletY = playerY
                    
                    fire_bullet(bulletX, bulletY)        
            elif y in ['no','off','stop']:
                ck_history(y)
                playerX_change = 0
                playerY_change = 0
            else:
                pass
        #> 語音辨識在此執行 ....

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            playerY_change = -5 
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                playerImg = pygame.image.load('player_l.png')
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
                playerImg = pygame.image.load('player_r.png')
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
                playerY_change = 5    

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 480:
        playerY = 480

    # Apple Movement
    for i in range(num_of_apples):

        # Game Over
        if appleY[i] > 440:
            for j in range(num_of_apples):
                appleY[j] = 2000
            game_over_text()
            break

        appleX[i] += appleX_change[i]
        if appleX[i] <= 0:
            appleX_change[i] = 4
            appleY[i] += appleY_change[i]
        elif appleX[i] >= 736:
            appleX_change[i] = -4
            appleY[i] += appleY_change[i]

        # Collision
        collision = isCollision(appleX[i], appleY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("coin.wav")
            explosionSound.play()
            score_value += 1
            appleX[i] = random.randint(0, 736)
            appleY[i] = random.randint(50, 150)

        apple(appleX[i], appleY[i], i)

        # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    history_label =font.render(ttl_history ,True , (30,30,255))
    screen.blit(history_label, (10, 550))
        
    player(playerX, playerY)
    show_score(textX, testY)
    ryShow_recognition(playerX, playerY, recResult= recResult)
    pygame.display.update()

pygame.quit()

#asrStream.stop()
#asrStream.close()

ryStream.stop()
ryStream.close()