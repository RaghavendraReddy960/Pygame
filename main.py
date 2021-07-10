import pygame
import random
import math
import sys

pygame.init()
screen = pygame.display.set_mode((800,1000))
running = True
score = 0
score1 = 0
tcore1 = 1
playerImg = pygame.image.load('ufo.png')

playerX = 370
playerY = 900
arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
brr = [1,0]
playerX_change = 0
font = pygame.font.SysFont('comiscans', 40, True)
text = font.render('score: '+ str(score), 1, (0,0,0))
font = pygame.font.SysFont('comiscans', 40, True)
text1 = font.render('score1: '+ str(score1), 1, (0,0,0))
font = pygame.font.SysFont('comiscans', 40, True)
text2 = font.render('level: '+ str(tcore1), 1, (0,0,0))
obstacleImg = pygame.image.load('8.png')
obstacleX = 300
obstacleY = 380
obstacleX_change = 0.2
obstacle1Img = pygame.image.load('8.png')
obstacle1X = 150
obstacle1Y = 300
obstacle2Img = pygame.image.load('8.png')
obstacle2X = 400
obstacle2Y = 180
obstacle3Img = pygame.image.load('8.png')
obstacle3X = 500
obstacle3Y = 460
obstacle4Img = pygame.image.load('8.png')
obstacle4X = 400
obstacle4Y = 600
obstacle5Img = pygame.image.load('8.png')
obstacle5X = 200
obstacle5Y = 720
obstacle6Img = pygame.image.load('8.png')
obstacle6X = 0
obstacle6Y = 660
obstacle6X_change = 0.2
obstacle7Img = pygame.image.load('8.png')
obstacle7X = 200
obstacle7Y = 540
obstacle7X_change = 0.2
obstacle8Img = pygame.image.load('8.png')
obstacle8X = 200
obstacle8Y = 240
obstacle8X_change = 0.2
player1Img = pygame.image.load('8.png')
player1X = 370
player1Y = 16
player1X_change = 0.3
player1Y_change = 0.3
def player(x,y):
	screen.blit(playerImg, (x, y))
def player1(x,y):
	screen.blit(playerImg, (x, y))
def obstacle5(x,y):
	screen.blit(obstacle7Img, (x, y))
def obstacle6(x,y):
	screen.blit(obstacle7Img, (x, y))
def obstacle7(x,y):
	screen.blit(obstacle7Img, (x, y))
def obstacle8(x,y):
	screen.blit(obstacle7Img, (x, y))			
enemyImg = pygame.image.load('8.png')

enemyX = 0
enemyY = 100
enemyX_change = 0.2
enemyY_change = 5

def obstacle(x, y):
	screen.blit(obstacleImg, (x, y))
obstacleImg = pygame.image.load('8.png')

def obstacle2(x, y):
	screen.blit(obstacleImg, (x, y))
obstacleImg = pygame.image.load('8.png')

def obstacle1(x, y):
	screen.blit(obstacle1Img, (x, y))
obstacle1Img = pygame.image.load('8.png')
def obstacle3(x, y):
	screen.blit(obstacle3Img, (x, y))
obstacle3Img = pygame.image.load('8.png')
def obstacle4(x, y):
	screen.blit(obstacle4Img, (x, y))
obstacle4Img = pygame.image.load('8.png')


def enemy(x, y):
	screen.blit(enemyImg, (x, y))
bulletImg = pygame.image.load('8.png')

bulletX = 0
bulletY = 600
bulletX_change = 0
bulletY_change = 0.2
bullet_state = "ready"

score = 0
score1 = 0
global speed 
speed = 0.2
def fire_bullet(x, y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImg, (x, y))
def isCollision(enemyX,enemyY,bulletX,bulletY):
	distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(bulletY-enemyY,2)))
	if distance < 6:
 		return True
	else:
 		return False	
def sCollision(enemyX,enemyY,playerX,playerY):
	distance1 = math.sqrt((math.pow(enemyX-playerX,2))+(math.pow(playerY-enemyY,2)))
	if distance1 < 10:
 		return True
	else:
 		return False
def obstaclec(obstacleX,obstacleY,playerX,playerY):
	obst = math.sqrt((math.pow(obstacleX-playerX,2))+(math.pow(playerY-obstacleY,2)))
	if obst < 10:
 		return True
	else:
 		return False 		
def obstaclec1(obstacle1X,obstacle1Y,playerX,playerY):
	obst1 = math.sqrt((math.pow(obstacle1X-playerX,2))+(math.pow(playerY-obstacle1Y,2)))
	if obst1 < 10:
 		return True
	else:
 		return False 
def obstaclec2(obstacle2X,obstacle2Y,playerX,playerY):
	obst2 = math.sqrt((math.pow(obstacle2X-playerX,2))+(math.pow(playerY-obstacle2Y,2)))
	if obst2 < 10:
 		return True
	else:
 		return False 

def obstaclec3(obstacle3X,obstacle3Y,playerX,playerY):
	obst3 = math.sqrt((math.pow(obstacle3X-playerX,2))+(math.pow(playerY-obstacle3Y,2)))
	if obst3 < 10:
 		return True
	else:
 		return False 
def obstaclec4(obstacle4X,obstacle4Y,playerX,playerY):
	obst4 = math.sqrt((math.pow(obstacle4X-playerX,2))+(math.pow(playerY-obstacle4Y,2)))
	if obst4 < 10:
 		return True
	else:
 		return False 
def obstaclec5(obstacle5X,obstacle5Y,playerX,playerY):
	obst5 = math.sqrt((math.pow(obstacle5X-playerX,2))+(math.pow(playerY-obstacle5Y,2)))
	if obst5 < 10:
 		return True
	else:
 		return False
def obstaclec6(obstacle6X,obstacle6Y,playerX,playerY):
	obst6 = math.sqrt((math.pow(obstacle6X-playerX,2))+(math.pow(playerY-obstacle6Y,2)))
	if obst6 < 10:
 		return True
	else:
 		return False
def obstaclec7(obstacle7X,obstacle7Y,playerX,playerY):
	obst7 = math.sqrt((math.pow(obstacle7X-playerX,2))+(math.pow(playerY-obstacle7Y,2)))
	if obst7 < 10:
 		return True
	else:
 		return False
def obstaclec8(obstacle8X,obstacle8Y,playerX,playerY):
	obst8 = math.sqrt((math.pow(obstacle8X-playerX,2))+(math.pow(playerY-obstacle8Y,2)))
	if obst8 < 10:
 		return True
	else:
 		return False 		 		 		
def player2():
    brr[0] = 0
    brr[1] = 1
    arr[0] = 0
    arr[1] = 0
    arr[2] = 0
    arr[3] = 0
    arr[4] = 0
    arr[5] = 0
    arr[6] = 0
    arr[7] = 0
    arr[8] = 0
    arr[9] = 0
    arr[10] = 0
    playerX =370          	    
    playerY =900
def player3():
	global speed
	print(speed)
	brr[0] = 1
	brr[1] = 0
	arr[0] = 0
	arr[1] = 0
	arr[2] = 0
	arr[3] = 0
	arr[4] = 0
	arr[5] = 0
	arr[6] = 0
	arr[7] = 0
	arr[8] = 0
	arr[9] = 0
	arr[10] = 0
	
		


while running:
	screen.fill((50,150,255))
	screen.blit(text,(20, 13))
	text = font.render('score: '+ str(score), 1, (0,0,0))
	screen.blit(text1,(650, 13))
	text1 = font.render('score1: '+ str(score1), 1, (0,0,0))
	screen.blit(text2,(370, 13))
	text2 = font.render('level: '+ str(tcore1), 1, (0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if brr[0] == 1:
					playerX_change = -0.3
				else:
					player1X_change = -0.3
			if event.key == pygame.K_UP:
				if brr[0] == 1:
					playerY += -20
				else:
					player1Y += 20	
			if event.key == pygame.K_DOWN:
				if brr[0] == 1:
					playerY += 20
				else:
					player1Y += -20	
			if event.key == pygame.K_RIGHT:
				if brr[0] == 1:
					playerX_change = +0.3
				else:
					player1X_change = +0.3
			if 	event.key == pygame.K_SPACE:
				bulletY = 600
				bulletX = playerX
				fire_bullet(bulletX,bulletY)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0
				player1X_change = 0 		
	           


		 	
	playerX += playerX_change
	if playerX <=0:
		playerX = 0
	if playerX >= 736:
	    playerX = 736
	if brr[1] == 1:    
		player1X += player1X_change    
	if player1X <=0:
		player1X = 0
	if player1X >= 736:
	   	player1X = 736	
	enemyX += enemyX_change	
	if enemyX <=0:
		enemyX_change = speed
	if enemyX >= 736:
	    enemyX_change = -speed	
	obstacle6X += obstacle6X_change	
	if obstacle6X <=0:
		obstacle6X_change = speed
	if obstacle6X >= 736:
	    obstacle6X_change = -speed	
	obstacle7X += obstacle7X_change	
	if obstacle7X <=0:
		obstacle7X_change = speed
	if obstacle7X >= 736:
	    obstacle7X_change = -speed
	obstacle8X += obstacle8X_change	
	if obstacle8X <=0:
		obstacle8X_change = speed
	if obstacle8X >= 736:
	    obstacle8X_change = -speed    	    


	if obstacleX <=0:
		obstacleX_change = speed
	if obstacleX >= 736:
	    obstacleX_change = -speed
	obstacleX += obstacleX_change        	
	if bullet_state is "fire":
		fire_bullet(bulletX, bulletY)
		bulletY -= bulletY_change
	collision = isCollision(enemyX,enemyY,bulletX,bulletY)
	if collision:
		bulletY = 480
		bullet_state = "ready"
		score += 1
	collision1 = sCollision(enemyX,enemyY,playerX,playerY)
	collision2 = obstaclec1(obstacle1X,obstacle1Y,playerX,playerY)
	collision3 = obstaclec2(obstacle2X,obstacle2Y,playerX,playerY)
	collision4 = obstaclec3(obstacle3X,obstacle3Y,playerX,playerY)
	collision5 = obstaclec(obstacleX,obstacleY,playerX,playerY)
	collision6 = obstaclec4(obstacle4X,obstacle4Y,playerX,playerY)
	collision7 = obstaclec4(obstacle5X,obstacle5Y,playerX,playerY)
	collision8 = obstaclec4(obstacle6X,obstacle6Y,playerX,playerY)
	collision9 = obstaclec4(obstacle7X,obstacle7Y,playerX,playerY)
	collision10 = obstaclec4(obstacle8X,obstacle8Y,playerX,playerY)				
	if collision1 or collision2 or collision3 or collision4 or collision5 or playerY == 20 or collision6 or collision7 or collision8 or collision9 or collision10:
		playerX = 370
		playerY = 900
		print('3')
		player2()	
	collision1 = sCollision(enemyX,enemyY,player1X,player1Y)
	collision2 = obstaclec1(obstacle1X,obstacle1Y,player1X,player1Y)
	collision3 = obstaclec2(obstacle2X,obstacle2Y,player1X,player1Y)
	collision4 = obstaclec3(obstacle3X,obstacle3Y,player1X,player1Y)
	collision5 = obstaclec(obstacleX,obstacleY,player1X,player1Y)
	collision6 = obstaclec(obstacle4X,obstacle4Y,player1X,player1Y)
	collision7 = obstaclec(obstacle5X,obstacle5Y,player1X,player1Y)
	collision8 = obstaclec(obstacle6X,obstacle6Y,player1X,player1Y)
	collision9 = obstaclec(obstacle7X,obstacle7Y,player1X,player1Y)
	collision10 = obstaclec(obstacle8X,obstacle8Y,player1X,player1Y)
	if collision1 or collision2 or collision3 or collision4 or collision5 or player1Y == 896 or collision6 or collision7 or collision8 or collision9 or collision10:
		player1X = 370
		player1Y = 16
		print('3')
		player3()
		if speed == 0.6:
			enemyX_change = 1
			speed = 1
			obstacleX_change = 1
			obstacle6X_change = 1
			obstacle7X_change = 1
			obstacle8X_change = 1
			tcore1 = 3

		else:		
			enemyX_change = 0.6
			speed = 0.6
			obstacleX_change = 0.6
			obstacle6X_change = 0.6
			obstacle7X_change = 0.6
			obstacle8X_change = 0.6
			tcore1 = 2



	if arr[0] != 1:	
		if brr[0] == 1:
			if playerX != obstacleX and playerY == obstacleY:
				score += 10
				arr[0] = 1
		else:
			if player1X != obstacleX and player1Y == obstacleY - 4:
				score1 += 10
				print(score1)
				arr[0] = 1 
	if arr[1] != 1:	
		if brr[0] == 1:
			if playerX != obstacle1X and playerY == obstacle1Y:
				score += 10
				arr[1] = 1
		else:
			if player1X != obstacle1X and player1Y == obstacle1Y - 4:
				score1 += 10
				arr[1] = 1 	
	if arr[2] != 1:	
		if brr[0] == 1:
			if playerX != obstacle2X and playerY == obstacle2Y:
				score += 10
				arr[2] = 1
		else:
			if player1X != obstacle2X and player1Y == obstacle2Y - 4:
				score1 += 10
				arr[2] = 1 	
	if arr[3] != 1:	
		if brr[0] == 1:
			if playerX != enemyX and playerY == enemyY:
				score += 10
				arr[3] = 1
		else:
			if player1X != enemyX and player1Y == enemyY - 4:
				print('50')
				score1 += 10
				print(score1)
				arr[3] = 1
	if arr[4] != 1:	
		if brr[0] == 1:
			if playerX != obstacle3X and playerY == obstacle3Y:
				score += 10
				arr[4] = 1
		else:
			if player1X != obstacle3X and player1Y == obstacle3Y - 4:
				score1 += 10
				arr[4] = 1 				 	
				arr[3] = 1
	if arr[5] != 1:	
		if brr[0] == 1:
			if playerX != obstacle4X and playerY == obstacle4Y:
				score += 10
				arr[5] = 1
		else:
			if player1X != obstacle4X and player1Y == obstacle4Y - 4:
				score1 += 10
				arr[5] = 1 
	if arr[6] != 1:	
		if brr[0] == 1:
			if playerX != obstacle5X and playerY == obstacle5Y:
				score += 10
				arr[6] = 1
		else:
			if player1X != obstacle5X and player1Y == obstacle5Y - 4:
				score1 += 10
				arr[6] = 1 	
	if arr[7] != 1:	
		if brr[0] == 1:
			if playerX != obstacle6X and playerY == obstacle6Y:
				score += 10
				arr[7] = 1
		else:
			if player1X != obstacle6X and player1Y == obstacle6Y - 4:
				score1 += 10
				arr[7] = 1 	
	if arr[8] != 1:	
		if brr[0] == 1:
			if playerX != obstacle7X and playerY == obstacle7Y:
				score += 10
				arr[8] = 1
		else:
			if player1X != obstacle7X and player1Y == obstacle7Y - 4:
				score1 += 10
				arr[8] = 1 	
	if arr[9] != 1:	
		if brr[0] == 1:
			if playerX != obstacle8X and playerY == obstacle8Y:
				score += 10
				arr[9] = 1
		else:
			if player1X != obstacle8X and player1Y == obstacle8Y - 4:
				score1 += 10
				arr[9] = 1 																		
	
	pygame.draw.rect(screen, (0,0,0),[0, 720, 800, 60])
	pygame.draw.rect(screen, (0,0,0),[0, 300, 800, 60])
	pygame.draw.rect(screen, (0,0,0),[0, 180, 800, 60])
	pygame.draw.rect(screen, (0,0,0),[0, 460, 800, 60])
	pygame.draw.rect(screen, (0,0,0),[0, 600, 800, 60])
	if brr[0]==1:	    	        						
		player(playerX,playerY)
	else:
		player1(player1X,player1Y)		
	enemy(enemyX,enemyY)
	obstacle(obstacleX,obstacleY)
	obstacle1(obstacle1X,obstacle1Y)
	obstacle2(obstacle2X,obstacle2Y)
	obstacle3(obstacle3X,obstacle3Y)
	obstacle4(obstacle4X,obstacle4Y)
	obstacle5(obstacle5X,obstacle5Y)

	obstacle6(obstacle6X,obstacle6Y)
	obstacle7(obstacle7X,obstacle7Y)
	obstacle8(obstacle8X,obstacle8Y)
	pygame.display.update()
