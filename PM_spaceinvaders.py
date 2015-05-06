import pygame, sys, random
import time
from pygame.locals import *
ORIGINALX = 60
ORIGINALX2 = 0
def doRectsOverlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if ((isPointInsideRect(a.left, a.top, b)) or
            (isPointInsideRect(a.left, a.bottom, b)) or
            (isPointInsideRect(a.right, a.top, b)) or
            (isPointInsideRect(a.right, a.bottom, b))):
            return True

    return False
playerwhite = True
def isPointInsideRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False
foodshoot = True
x = 0
lives = 3
score = 0
##basicFont = pygame.font.SysFont(None, 48)
# set up pygame
pygame.init()
mainClock = pygame.time.Clock()
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
# set up the window
WINDOWWIDTH = 1400
WINDOWHEIGHT = 850
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Input')
basicFont = pygame.font.SysFont(None, 100)
# set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (250, 0, 0)
CYAN = (0, 255, 255)
# set up the player and food data structure
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
shields = []
player = pygame.Rect(750, 800, 100, 10)

foods = []
ammo = pygame.Rect(800 + x, 780, 10, 20)


# set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
moveright = True 
##while ammo2
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 600
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 330
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 600
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 660
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 600
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 990
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 600
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 1320
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 610
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 610
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 330
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 610
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 660
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 610
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 990
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 610
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 1320
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 610
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 620
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 330
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 620
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 660
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 620
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 990
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 620
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 1320
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 620
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 630
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 330
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 630
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 660
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 630
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 990
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 630
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 1320
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 630
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 640
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 330
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 640
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 660
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 640
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 990
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 640
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 1320
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 640
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 650
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 330
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 650
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 660
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 650
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 990
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 650
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 1320
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 650
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))

for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 660
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 330
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 660
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 660
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 660
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 990
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 660
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 1320
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 660
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 670
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 330
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 670
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 660
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 670
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 990
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 670
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
ORIGINALX2 = 1320
for i in range(10):
    ORIGINALX2 += 10
    ORIGINALY2 = 670
    shields.append(pygame.Rect(ORIGINALX2, ORIGINALY2, 10, 10))
MOVESPEED = 3

for i in range(10):
    ORIGINALX += 80
    ORIGINALY = 60
    foods.append(pygame.Rect(ORIGINALX, ORIGINALY, 60, 40))
ORIGINALX = 60
for i in range(10):
    ORIGINALX += 80
    ORIGINALY = 160
    foods.append(pygame.Rect(ORIGINALX, ORIGINALY, 60, 40))
ORIGINALX = 60
for i in range(10):
    ORIGINALX += 80
    ORIGINALY = 260
    foods.append(pygame.Rect(ORIGINALX, ORIGINALY, 60, 40))

aliendead = True
 #run the game loop

while True:
    
    for food in foods:
        if moveright:
            food.right += MOVESPEED
            
        if food.right > (WINDOWWIDTH):
            moveright = False
            for food in foods:
                food.bottom += 35
                food.left -= MOVESPEED
        if not moveright:
            food.left -= MOVESPEED
        if food.left < 0:
            moveright = True
            for food in foods:
                food.bottom += 35
    for i in foods:
        if aliendead:
            p = random.randint(0, len(foods) - 1)
            xvariable = foods[p].left
            yvariable = foods[p].top
            ammo2 = pygame.Rect(xvariable + 24, yvariable + 30, 10, 20)
            aliendead = False
    ammo2.top += 18
            
            
                                       
    
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_UP or event.key == ord('s'):
                moveDown = False
                moveUp = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == ord('x'):
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

     # draw the black background onto the surface
    windowSurface.fill(BLACK)
    if ammo2.bottom > 850:
        aliendead = True
    # move the player
    if moveLeft and player.left > 0:
        player.left -= 20
        ammo.left -= 20
        x -= 20
    if moveRight and player.right < WINDOWWIDTH:
        player.right += 20
        ammo.right += 20
        x += 20
    if moveUp and ammo.bottom < WINDOWHEIGHT:
        ammo.bottom -= 25
        moveUp = True
    if ammo.top < 0:
        ammo = pygame.Rect(800 + x, 780, 10, 20)
        moveUp = False
    
    # draw the player onto the surface
    if playerwhite:
        pygame.draw.rect(windowSurface, WHITE, player)
        pygame.draw.rect(windowSurface, RED, ammo)
    pygame.draw.rect(windowSurface, RED, ammo2)
    # check if the player has intersected with any food squares.
    for food in foods[:]:
        if ammo.colliderect(food):
            moveUp = False
            foods.remove(food)
            ammo = pygame.Rect(800 + x, 780, 10, 20)
            score += 1000
    if ammo2.colliderect(player):
        pygame.draw.rect(windowSurface, BLACK, player)
        pygame.draw.rect(windowSurface, BLACK, ammo)
        aliendead = True
        lives -= 1
    for i in shields:
        if ammo2.colliderect(i):
            shields.remove(i)
            aliendead = True
            
            
        
    for i in shields:
        if ammo.colliderect(i):
            moveUp = False
            shields.remove(i)
            ammo = pygame.Rect(800 + x, 780, 10, 20)
    text = basicFont.render(("Score ="), True, GREEN, BLACK)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx - 580
    textRect.centery = windowSurface.get_rect().centery - 360
    windowSurface.blit(text, textRect)
    text = basicFont.render((str(score)), True, GREEN, BLACK)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx - 330
    textRect.centery = windowSurface.get_rect().centery - 360
    windowSurface.blit(text, textRect)
    text = basicFont.render((str(lives)), True, GREEN, BLACK)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx + 600
    textRect.centery = windowSurface.get_rect().centery - 360
    windowSurface.blit(text, textRect)
    text = basicFont.render(("lives ="), True, GREEN, BLACK)
    textRect = text.get_rect()
    textRect.centerx = windowSurface.get_rect().centerx + 450
    textRect.centery = windowSurface.get_rect().centery - 360
    windowSurface.blit(text, textRect)
            
        

            
    if lives == 0:
        text = basicFont.render(("CONGRATS U ARE A LOSER"), True, CYAN, BLACK)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery   
        windowSurface.blit(text, textRect)
        playerwhite = False
    if foods == []:
        text = basicFont.render(("CONGRATS U WON"), True, CYAN, BLACK)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.centery = windowSurface.get_rect().centery   
        windowSurface.blit(text, textRect)
        


    
    # draw the food
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, CYAN, foods[i])
    for i in range(len(shields)):
        pygame.draw.rect(windowSurface, GREEN, shields[i])

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
