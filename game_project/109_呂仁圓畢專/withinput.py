import math
import random
import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Catch")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

blue=(30,30,255)
green=(30,150,30)
X=800
Y=600
speed=0.03
point=0
global history
history=[]
global ttl_history
ttl_history=" "

def new_word():
	global chosenWord, pressedWord, word_X, word_Y, text, pointCaption, speed,label
	word_X=random.randint(100,500)
	word_Y=0
	speed +=0.003
	pressedWord=""
	lines=open("words.txt").read().splitlines()
	chosenWord=random.choice(lines)
	text =font.render(chosenWord, True, blue)

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


win=pygame.display.set_mode((X,Y))
pygame.display.set_caption("Fast Typing Game")
font=pygame.font.SysFont("ComicSansMs",32)

new_word()

while True:
	win.fill((0, 0, 0))
	win.blit(background, (0, 0))
	word_Y+=speed
	win.blit(text,(word_X, word_Y))
	label = font.render(pressedWord, 1, (255,0,0))
	win.blit(label, (350, 500))

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type ==pygame.KEYDOWN:
			pressedWord +=pygame.key.name(event.key)
			label = font.render(pressedWord, 1, (255,0,0))
			#win.blit(label, (350, 500))
			if chosenWord.startswith(pressedWord):
				if chosenWord==pressedWord:
					point+= len(chosenWord)
					ck_history(chosenWord)
					new_word()
			else:
				win.blit(label, (350, 500))
				win.blit(history_label, (100, 700))
				pressedWord=""
	

	pointCaption=font.render(str(point), True, green)
	win.blit(pointCaption, (10,5))
	history_label =font.render(ttl_history ,True , blue)
	win.blit(history_label, (10, 550))

	if word_Y<Y-5:
		pygame.display.update()
	else:
		event=pygame.event.wait()
		if event.type ==pygame.KEYDOWN and event.key ==pygame.K_SPACE:
			speed=0.03
			point=0
			new_word()
