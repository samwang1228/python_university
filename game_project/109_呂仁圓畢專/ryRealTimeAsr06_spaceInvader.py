# In[]
'''
ryRealTimeAsr03_spaceInvader.py

using Real-time asr to do voice control

ref: https://github.com/attreyabhatt/Space-Invaders-Pygame

Renyuan Lyu, 2020/01/05
'''

import math
import random

import pygame
from pygame import mixer


from ryRealTimeAsr06_threading import ryAsrStream, ryGet1secSpeechAndRecogItWithProb

from ryRealTimeAsr06_threading import  ryQ, ryRecogQGet, ryStream

#
# 語音辨識在此開動 ....，
# 結束時記得 做以下 2 行
# asrStream.stop()
# asrStream.close()
#

#asrStream= ryAsrStream()
#asrStream.start()

dataBasePath= '../ryData/'


# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load(dataBasePath+'background.png')

# Sound
mixer.music.load(dataBasePath+"background.wav")

mixer.music.play(-1) ## 這裡是一個 thread

# Caption and Icon
pygame.display.set_caption("SpaceInvader2020: withSpeechCommands by RenyuanLyu @長庚大學")
icon = pygame.image.load(dataBasePath+'ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load(dataBasePath+'player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load(dataBasePath+'enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

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

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def ryShow_recognition(x, y, recResult= None):
    
    if recResult=='_unknown_':
        recResult = ''
    
    score = font.render(f"{recResult}", True, (0, 255, 255))
    screen.blit(score, (x-50, y+50))
    
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# In[]
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
            elif y== 'right':
                playerX_change = +1
            elif y== 'forward':
                playerY_change = -1            
            elif y== 'backward':
                playerY_change = +1   
                
            elif y in ['yes', 'on', 'go']:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound(dataBasePath+"laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    bulletY = playerY
                    
                    fire_bullet(bulletX, bulletY)
                    
            elif y in ['no','off','stop']:
                playerX_change = 0
                playerY_change = 0
            else:
                pass
        #> 語音辨識在此執行 ....
        
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    
    # Background Image
    screen.blit(background, (0, 0))
    
    # 處理來自玩家之互動【事件】 (event)： 鍵盤、滑鼠 之動作....
    eventList= pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound(dataBasePath+"laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

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
    elif playerY >= 550:
        playerY = 550





    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound(dataBasePath+"explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    
    ryShow_recognition(playerX, playerY, recResult= recResult)
    
    pygame.display.update() 
    # 顯示幕必須更新(update)，這是動畫(animation)的根本。

pygame.quit()

#asrStream.stop()
#asrStream.close()

ryStream.stop()
ryStream.close()
