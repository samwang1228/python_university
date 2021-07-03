import pygame, random

pygame.init()
background=(200,200,255)
blue=(30,30,255)
green=(30,150,30)

X=600
Y=400
speed=0.03
point=0

def new_word():
	global chosenWord, pressedWord, word_X, word_Y, text, pointCaption, speed
	word_X=random.randint(100,500)
	word_Y=0
	speed +=0.003
	pressedWord=""
	lines=open("words.txt").read().splitlines()
	chosenWord=random.choice(lines)
	text =font.render(chosenWord, True, blue)

win=pygame.display.set_mode((X,Y))
pygame.display.set_caption("Fast Typing Game")
font=pygame.font.SysFont("ComicSansMs",32)

new_word()

while True:
	win.fill(background)
	word_Y+=speed
	win.blit(text,(word_X, word_Y))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type ==pygame.KEYDOWN:
			pressedWord +=pygame.key.name(event.key)
			if chosenWord.startswith(pressedWord):
				if chosenWord==pressedWord:
					point+= len(chosenWord)
					new_word()
			else:
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