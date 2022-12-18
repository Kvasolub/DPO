import pygame
import paho.mqtt.client as mqtt
import math

pygame.init()

client = mqtt.Client(client_id="botid")
client.connect("localhost", 1883, 20)
client.subscribe("testDPO/practice3")

def on_message(client, userdata, msg):
    moving_mqtt(msg.payload)
    screen.fill(BLACK)
    screen.blit(image,rect)
    pygame.display.update()

def moving_mqtt(m):
    m=str(m.decode('utf-8'))

    time_dist, time_ugol=m.split()

    time_dist= float(time_dist)
    time_ugol= float(time_ugol)

    ugol_povorota=time_ugol*30 #30 -скорость поворота (упростил задачу и не передаю по mqtt скорости)
    dlina=1*time_dist #1 -скорость движения

    X=dlina*math.cos(math.radians(ugol_povorota)) 
    Y=dlina*math.sin(math.radians(ugol_povorota))
    rect.move_ip(X,Y)

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS=60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rect = pygame.Rect((0,0),(32,32))
image = pygame.Surface((32,32))
image.fill(WHITE)
rect.move_ip(0,200)
rect.move_ip(300,0)
screen.fill(BLACK)
screen.blit(image,rect)
pygame.display.update()


client.on_message = on_message       
client.loop_forever()

