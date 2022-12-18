import time
import numpy as np
from math import atan2, degrees
import paho.mqtt.client as mqtt

def Moving(x0,x1,y0,y1):
    Dx=x1-x0
    Dy=y1-y0
    distance = (Dx**2+Dy**2)**(1/2)
    rads = atan2(Dy,Dx)
    degs = degrees(rads)
    return distance, degs

vars=input().split()
ipmqtt, portmqtt, topicmqtt, vel, velugl, cordsFile = vars

client = mqtt.Client(client_id="botcontroler")
client.connect("localhost", 1883, 60)

vel = float(vel)
velugl = float(velugl)

Cords_X = np.loadtxt("Cords.txt", dtype=float, usecols=0)
Cords_Y = np.loadtxt("Cords.txt", dtype=float, usecols=1)


for i in range(1,len(Cords_X),1):
    dist, ugol=Moving (Cords_X[i-1],Cords_X[i],Cords_Y[i-1],Cords_Y[i])

    time_dist=dist/vel
    time_ugol=ugol/velugl

    time_dist_str=str(time_dist)
    time_ugol_str=str(time_ugol)

    times=time_dist_str +" " + time_ugol_str 

    client.publish(topic="testDPO/practice2", payload=times)

    #print("Поварачаем {} с, по прямой {} с. Ждём приезда на точку...".format(time_ugol,time_dist)) #отрицательное время поворота - поворот по часовой стрелке
    #time.sleep(time_dist+abs(time_ugol)+5)
    
#10.0.2.2 1883 abotcmd1 1.0 30.0 path.txt