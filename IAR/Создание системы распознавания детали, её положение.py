import pygame
import random
import cv2
import imutils
from PIL import ImageGrab

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
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')
    img = cv2.imread('screenshot.png', cv2.IMREAD_COLOR)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
            if keys[pygame.K_UP]:
                pygame.draw.circle(screen, 'WHITE', (approx[0,0,0],approx[0,0,1]), 500)
            
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
                    pygame.draw.circle(screen, 'WHITE', (approx[0,0,0],approx[0,0,1]), 5)
                    pygame.draw.circle(screen, 'GREEN', (approx[1,0,0],approx[1,0,1]), 5)
                    pygame.draw.circle(screen, 'RED', (approx[3,0,0],approx[3,0,1]), 5)
                    
                    return rightBox

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

ModelRun = True
spawn = False

ticket = pygame.time.Clock()
Text = pygame.font.SysFont('Century', 50)

image = pygame.image.load("image of box.png")

countRights = 0

FPS=60
while ModelRun:
    ticket.tick(FPS)
    keys = pygame.key.get_pressed()
    screen.fill('black')

    if spawn == False:
        spawn = True

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
        #box=resized_image

        PositonX = w//2-100
        PositonY = h//2-100
        screen.blit(box, (PositonX, PositonY))

    if spawn == True:
        screen.blit(box, (PositonX, PositonY))
        if keys[pygame.K_SPACE]:
            cv2.waitKey(FPS)
            spawn = False

    partREAL = checkingSizes(sizesbox)
    partDetOPENCV = checkingSizes(scrn())

    if partREAL==partDetOPENCV:
        countRights +=1
        spawn = False
        TextCount = Text.render('Верно '+str(countRights),'True', 'White')
        screen.blit(TextCount, (w//2-100, h//1.1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            ModelRun = False

    pygame.display.update()
