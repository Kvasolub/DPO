import pygame
import random
import cv2
import imutils
import pyautogui
import math
import numpy as np

def Bisection(PositonX, PositonY, Xcrab, Ycrab, SpeedConv, SpeedCrab, point, previous):
    distantX = abs(point - Xcrab)
    distantY = abs(PositonY - Ycrab) 
    radian = math.atan2(distantY, distantX)
    time = distantX/(SpeedCrab*math.cos(radian))
    positionBox = PositonX + time * SpeedConv
    if positionBox < point and abs(point-positionBox) > 10:
        previous = point
        radian = Bisection(PositonX, PositonY, Xcrab, Ycrab, SpeedConv, SpeedCrab, point/2, previous)
    elif positionBox > point and abs(point-positionBox) > 10:
        radian = Bisection(PositonX, PositonY, Xcrab, Ycrab, SpeedConv, SpeedCrab, point + (previous - point)/2, previous)
    return(radian)

def checkingSizes(sizesbox):
    if sizesbox == boxes[0]:
        part = 'Box №1'
    elif sizesbox == boxes[1]:
        part = 'Box №2'  
    else:
        part = 'Box №3'
    return part

def accounting(detSize, Size):
    if (Size * 0.9 <= detSize <= Size * 1.05):
        return True
    else:
        return False

def scrn():
    imgscreen = pyautogui.screenshot()
    img = np.array(imgscreen)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # если убрать, то время обработки увеличивается
    img  = cv2.medianBlur(img,7)
    edges = cv2.Canny(img, 0, 5)

    cont = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
    cont = imutils.grab_contours(cont)
    cont = sorted(cont, key=cv2.contourArea, reverse = False)

    rightBox=0

    for i in cont:
        approx = cv2.approxPolyDP(i, 25, True)

        if len(approx) == 4:
            
            detSize1 = ((approx[1,0,0]-approx[0,0,0])**2+(approx[1,0,1]-approx[0,0,1])**2)**0.5
            detSize2 = ((approx[3,0,0]-approx[0,0,0])**2+(approx[3,0,1]-approx[0,0,1])**2)**0.5
            
            for lst in boxes:
                right1=False
                right2=False
                for realSize in lst:
                    if accounting(detSize1,realSize):
                        right1=True
                    if accounting(detSize2,realSize):
                        right2=True
                if right1 and right2:
                    rightBox = lst

                    return rightBox, approx

def movecord(xcrab,ycrab,xgoal,ygoal):
    disX = xgoal-xcrab
    disY = ygoal-ycrab
    return  math.atan2(disY,disX)

def center(fdot):
    xcenter = sum([fdot[i,0,0] for i in range(0,4,2)])/2
    ycenter = sum([fdot[i,0,1] for i in range(0,4,2)])/2
    return xcenter, ycenter

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN, pygame.HWSURFACE)
pygame.display.set_caption("Model")

infoObject = pygame.display.Info()

w=infoObject.current_w
h=infoObject.current_h

boxes = [[]*3]*3
boxes[0] = [50, 100, 150]
boxes[1] = [100, 200, 300]
boxes[2] = [175, 400, 90]

PositonX = -w//6.3
PositonY = h//16
SpeedConv = 5
SpeedCrab = 8

goalX = 0
goalY = 0

Xcrab = w//2
Ycrab = h-100

ModelRun = True
spawn = False
stop = False
Menu = True

ticket = pygame.time.Clock()
Text = pygame.font.SysFont('Century', 50)
TextMenu = pygame.font.SysFont('Century', 100)
TextMenuCredits = pygame.font.SysFont('Century', 40)
image = pygame.image.load("Image of box.png")

nameDetBox = ''

while ModelRun:
    ticket.tick(60)
    keys = pygame.key.get_pressed()
    screen.fill('black')

    while Menu == True:
        keys = pygame.key.get_pressed()
        ticket.tick(60)
        screen.fill('black')
        TextScreen = TextMenu.render('Модель движения ','True', 'White')
        screen.blit(TextScreen, (w//3.8, h//2.5))
        TextScreen = Text.render('prees SPACE to start','True', 'White')
        screen.blit(TextScreen, (w//2.85, h//1.7))
        TextScreen = TextMenuCredits.render('ФИО','True', 'White')
        screen.blit(TextScreen, (w//1.2, h//1.2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                Menu = False
                ModelRun = False 
            elif keys[pygame.K_SPACE] == 1:
                Menu = False
        pygame.display.update()

    pygame.draw.rect(screen, (10, 10, 10), (0, 50, w, 400))
    
    if spawn == True:
        PositonX += SpeedConv
    else:
        sizesbox = random.choice(boxes)
        size1, size2 = random.sample(sizesbox, 2)
        resized_image = pygame.transform.scale(image, (size1, size2))
        if sizesbox == boxes[0]:
            resized_image.fill('Gray')
        elif sizesbox == boxes[1]:
            resized_image.fill('Red')  
        else:
            resized_image.fill('Blue')
        angle = random.randint(0, 180)
        box = pygame.transform.rotate(resized_image, angle)
        spawn = True
        rads = None

    if PositonX > w//1.2:
        spawn = False
        nameDetBox = ''
        PositonX = -w//6.3
        PositonY = h//16
    else:
        screen.blit(box, (PositonX, PositonY))
        part = checkingSizes(sizesbox)
        TextScreen = Text.render(part,'True', 'White')
        screen.blit(TextScreen, (0, h//1.1))

    if nameDetBox == '' and PositonX>w//10:
        nameDetBox, FourDot = scrn()
        nameDetBox = checkingSizes(nameDetBox) 
        goalX, goalY = center(FourDot)

    elif nameDetBox != '' and PositonX>w//10:        
        if rads == None:
            rads = Bisection(PositonX, PositonY, Xcrab, Ycrab, SpeedConv, SpeedCrab, w, 0)
        Xcrab = Xcrab-SpeedCrab*math.cos(rads)
        Ycrab = Ycrab-SpeedCrab*math.sin(rads)
        
    TextScreenDet = Text.render(nameDetBox,'True', 'White')
    screen.blit(TextScreenDet, (w-300, h//1.1))
    
    goalX += SpeedConv

    if (abs(Xcrab-goalX) < 50 and abs(Ycrab-goalY) < 50) or (abs(Xcrab-goalX) < 50 and Ycrab-goalY > 150) :
        process = True
        while process == True:
            keys = pygame.key.get_pressed()
            ticket.tick(60)
            screen.fill('black')
            pygame.draw.rect(screen, (10, 10, 10), (0, 50, w, 400))
            screen.blit(box, (PositonX, PositonY))
            pygame.draw.circle(screen, 'GREEN',(Xcrab, Ycrab),50)
            pygame.display.update()

            goalX = 800
            goalY = 900

            rads = movecord(Xcrab, Ycrab, goalX, goalY)
            Xcrab = Xcrab+SpeedCrab*math.cos(rads)
            Ycrab = Ycrab+SpeedCrab*math.sin(rads)
            PositonX = PositonX+SpeedCrab*math.cos(rads)
            PositonY = PositonY+SpeedCrab*math.sin(rads)

            if rads < 0.01:
                process = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    ModelRun = False
        PositonX = -w//6.3
        PositonY = h//16
        nameDetBox = ''
        goalX = 0
        goalY = 0
        spawn = False

    pygame.draw.circle(screen, 'GREEN',(Xcrab, Ycrab),30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            ModelRun = False 

    pygame.display.update()
