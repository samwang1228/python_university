import math
import random
import pygame
from pygame import mixer
import pygame, sys
from ryRealTimeAsr06_threading import ryAsrStream, ryGet1secSpeechAndRecogItWithProb
from ryRealTimeAsr06_threading import  ryQ, ryRecogQGet, ryStream


dataBasePath= '../ryData/'

#initialize pygame
pygame.init() 
background = pygame.image.load('ele/background.png')

# sound
mixer.music.load("ele/background.wav")
mixer.music.play(-1)

# caption and icon
pygame.display.set_caption("Catch")
icon = pygame.image.load('ele/ufo.png')
pygame.display.set_icon(icon)

#variables
blue=(30,30,255)
green=(30,150,30)
X=800
Y=600
speed=0.03
point=0

#screen
win=pygame.display.set_mode((X,Y))
pygame.display.set_caption("Fast Typing Game")
font=pygame.font.SysFont("ComicSansMs",32)

#player pt1
playerImg = pygame.image.load('ele/player_r.png')
logoImg=pygame.image.load('menu/logo.png')
startImg=pygame.image.load('menu/Start.png')
modeImg=pygame.image.load('menu/Mode.png')
uploadImg=pygame.image.load('menu/Upload.png')
downloadImg=pygame.image.load('menu/Download.png')
dirImg=pygame.image.load('menu/Direction.png')
typeImg=pygame.image.load('menu/Type.png')
speechImg=pygame.image.load('menu/Speech.png')
bulletImg = pygame.image.load(dataBasePath+'bullet.png')

# Apples
appleImg = []
appleX = []
appleY = []
appleX_change = []
appleY_change = []
num_of_apples = 3

for i in range(num_of_apples):
    appleImg.append(pygame.image.load('ele/apple.png'))
    appleX.append(random.randint(0, 736))
    appleY.append(random.randint(50, 150))
    appleX_change.append(2)
    appleY_change.append(20)

# Score
font = pygame.font.Font('freesansbold.ttf', 32)
score_value=0 
# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y): #for withkey
    global score_value 
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    win.blit(score, (x, y))

def game_over_text():#for withkey
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    win.blit(over_text, (200, 250))

def player(x, y):#for withkey
    win.blit(playerImg, (x, y))

def apple(x, y, i):#for withkey
    win.blit(appleImg[i], (x, y))

def isCollision(appleX, appleY, bulletX, bulletY):#for withkey
    distance = math.sqrt(math.pow(appleX - bulletX, 2) + (math.pow(appleY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def draw_text(text,font,color,surface,x,y):
    textobj=font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

def main_menu():
    while True:
        win.fill((0, 0, 0))
        win.blit(background, (0, 0))
        win.blit(logoImg, (275, 60))
        win.blit(startImg, (300,300))
        #draw_text('APPLE CATCHER', font,(255,255,255), win, 100,400)
        button_start=pygame.Rect(300,300,200,131)
        
        mx, my=pygame.mouse.get_pos()
        
        click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type==pygame.KEYDOWN:
                if event.key ==pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    click= True

        if button_start.collidepoint((mx,my)):
            if click:
                sec_menu() #play with keyboard
        
        pygame.display.update()

def sec_menu():
    while True:
        win.fill((0, 0, 0))
        win.blit(background, (0, 0))
        
        win.blit(modeImg, (300, 100))
        win.blit(uploadImg, (300,200))
        win.blit(downloadImg, (300, 300))
        mx, my=pygame.mouse.get_pos()

        button_mode=pygame.Rect(300,100,200,131)
        button_upload=pygame.Rect(300,200,200,131)
        button_download=pygame.Rect(300,300,200,131)
        
        click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type==pygame.KEYDOWN:
                if event.key ==pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    click= True
        
        if button_mode.collidepoint((mx,my)):
            if click:
                mode_menu() #play with keyboard
        '''
        if button_upload.collidepoint((mx,my)):
            if click:
                withinput() #upload
        if button_download.collidepoint((mx,my)):
            if click:
                withinput() #download
        '''
        
        pygame.display.update()

def mode_menu():
    while True:
        win.fill((0, 0, 0))
        win.blit(background, (0, 0))
        win.blit(dirImg, (150, 250))
        win.blit(typeImg, (350,250))
        win.blit(speechImg, (550, 250))
        win.blit(modeImg, (350, 100))
        mx, my=pygame.mouse.get_pos()

        button_dir=pygame.Rect(150,250,150,150)
        button_type=pygame.Rect(350,250,150,150)
        button_speech=pygame.Rect(550,250,150,150)
        
        click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type==pygame.KEYDOWN:
                if event.key ==pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    click= True
        
        if button_dir.collidepoint((mx,my)):
            if click:
                withkey() #play with keyboard
        if button_type.collidepoint((mx,my)):
            if click:
                withinput() #play with input
        if button_speech.collidepoint((mx,my)):
            if click:
                withspeech() #play with input
        pygame.display.update()

def withkey():
    global score_value 
    # Player
    playerX = 370
    playerY = 480
    playerX_change = 0
    playerY_change = 0

    running=True
    while running:
        # RGB = Red, Green, Blue
        win.fill((0, 0, 0))
        # Background Image
        win.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                playerY_change = -5 
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                    playerImg = pygame.image.load('ele/player_l.png')
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                    playerImg = pygame.image.load('ele/player_r.png')
            if event.type == pygame.KEYUP:
                playerY_change = 5    

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

        playerX += playerX_change
        playerY += playerY_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= X-64:
            playerX = X-64
        if playerY <= 0:
            playerY = 0
        elif playerY >= Y-64:
            playerY = Y-64

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
            collision = isCollision(appleX[i], appleY[i], playerX, playerY)
            if collision:
                explosionSound = mixer.Sound("ele/coin.wav")
                explosionSound.play()
                score_value += 1
                appleX[i] = random.randint(0, 736)
                appleY[i] = random.randint(50, 150)
            apple(appleX[i], appleY[i], i)
        player(playerX, playerY)
        show_score(10, 10)
        pygame.display.update()

def new_word():
	global chosenWord, pressedWord, word_X, word_Y, text, pointCaption, speed,label
	word_X=random.randint(100,500)
	word_Y=0
	speed +=0.003
	pressedWord=""
	lines=open("ele/words.txt").read().splitlines()
	chosenWord=random.choice(lines)
	text =font.render(chosenWord, True, blue)

win=pygame.display.set_mode((X,Y))
pygame.display.set_caption("Fast Typing Game")
font=pygame.font.SysFont("ComicSansMs",32)

new_word()

def withinput():
    global chosenWord, pressedWord, word_X, word_Y, text, pointCaption, speed,label,point
    running=True
    while running:
	    win.fill((0, 0, 0))
	    win.blit(background, (0, 0))
	    word_Y+=speed
	    win.blit(text,(word_X, word_Y))
	    label = font.render(pressedWord, 1, (255,0,0))
	    win.blit(label, (350, 500))
	    for event in pygame.event.get():
		    if event.type==pygame.QUIT:
			    pygame.quit()
			    sys.exit()
		    elif event.type ==pygame.KEYDOWN:
			    pressedWord +=pygame.key.name(event.key)
			    label = font.render(pressedWord, 1, (255,0,0))
			    #win.blit(label, (350, 500))
			    if chosenWord.startswith(pressedWord):
				    if chosenWord==pressedWord:
					    point+= len(chosenWord)
					    new_word()
			    else:
				    win.blit(label, (350, 500))
				    pressedWord=""

	    pointCaption=font.render(str(point), True, green)
	    win.blit(pointCaption, (10,5))
	
	    if word_Y<Y-5:
		    pygame.display.update()
	    else:
		    event=pygame.event.wait()
		    if event.type ==pygame.KEYDOWN and event.key ==pygame.K_SPACE:
			    speed=0.03
			    point=0
			    new_word()

import pygame.time as pgTime

def withspeech():
    playerX = 370
    playerY = 480
    playerX_change = 0
    playerY_change = 0
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"
    textX = 10
    testY = 10
    global history
    history=[]
    global ttl_history
    ttl_history=" "
    global score_value

    ryClock= pgTime.Clock()
    ryLoopRate= 30 # loop/sec 
    recProbToConfirm= 0.2
    
    running = True
    while running:
        # 掌握一下這個 while 迴圈的 循環速度 fps= frames (loops) per sec
        dt=  ryClock.tick(ryLoopRate)
        fps= ryClock.get_fps()
        #print(f'dt= {dt:.2f}, fps= {fps:.0f}')
        
        #< 語音辨識在此執行 ....，
        # #y, prob= ryGet1secSpeechAndRecogItWithProb()
        # #'ryQ', 'ryRecogQGet'
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
        win.fill((0, 0, 0))
        # Background Image
        win.blit(background, (0, 0))
    
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
        win.blit(history_label, (10, 550))
        
        player(playerX, playerY)
        show_score(textX, testY)
        ryShow_recognition(playerX, playerY, recResult= recResult)
        pygame.display.update()
    pygame.quit()
    ryStream.stop()
    ryStream.close()


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    win.blit(bulletImg, (x + 16, y + 10))

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
    win.blit(score, (x-50, y+50))

main_menu()
        


        