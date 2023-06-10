import pygame
import random

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
SpeedConv = 100

ModelRun = True
spawn = False
stop = False

ticket = pygame.time.Clock()
Text = pygame.font.SysFont('Century', 50)

image = pygame.image.load("qu.png")


while ModelRun:
    ticket.tick(60)
    keys = pygame.key.get_pressed()
    screen.fill('black')

    pygame.draw.rect(screen, (10, 10, 10), (0, 50, w, 400))
    
    if spawn == True:
        PositonX += SpeedConv
        screen.blit(box, (PositonX, PositonY))
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
        PositonX = -w//6.3

    if PositonX>w+100:
        spawn = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            ModelRun = False 

    pygame.display.update()