import random
import time
import matplotlib.pyplot as plt

best_time=999
worth_time=0
summa=0

gist=[0]*10
hgist=[99,199,299,399,499,599,699,799,899,999]
a=[random.randint(0, 999) for j in range(1000000)]

for v in range(1,100):

    print("Keep calm and drink kvas. Я считаю время, сейчас на",v,"шаге из 100")
    
    start=time.time()

    for i in a:
        if i<100:
            gist[0]+=1
        elif (i>100 and i<200):
            gist[1]+=1
        elif (i>200 and i<300):
            gist[2]+=1
        elif (i>300 and i<400):
            gist[3]+=1
        elif (i>400 and i<500):
            gist[4]+=1
        elif (i>500 and i<600):
            gist[5]+=1
        elif (i>600 and i<700):
            gist[6]+=1
        elif (i>700 and i<800):
            gist[7]+=1
        elif (i>800 and i<900):
            gist[8]+=1
        elif (i>900 and i<999):
            gist[9]+=1

    end=time.time()

    ptime=end-start
    if ptime<best_time:
        best_time=ptime
    elif ptime>worth_time:
        worth_time=ptime
    summa+=ptime

plt.bar(hgist,gist, 50, bottom=1)


plt.show()

print("Лучшее время",best_time)
print("Худшее время",worth_time)
print("Среднее время",summa/100)
