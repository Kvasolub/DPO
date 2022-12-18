import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, msg):
    #print (str(msg.payload.decode('utf-8')))
    moving_mqtt(msg.payload)

def moving_mqtt(m):
    m=str(m.decode('utf-8'))
    time_dist, time_ugol=m.split()
    time_dist= float(time_dist)
    time_ugol= float(time_ugol)

    if time_ugol<0:
        porovot="Right"
    else:
        porovot="Left"

    print("Forward {} sec. {} {} sec.".format(time_dist, porovot, abs(time_ugol)))


client = mqtt.Client(client_id="botid")
client.connect("localhost", 1883, 20)
client.subscribe("testDPO/practice2")



client.on_message = on_message
client.loop_forever()

    
#10.0.2.2 1883 abotcmd1 1.0 30.0 path.txt
# mosquitto_pub  -h localhost -t testDPO/practice2 -i client -m "Тестовое сообщение"