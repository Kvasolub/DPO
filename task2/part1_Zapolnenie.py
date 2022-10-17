import random

def write_gist(Ygist,Xgist):
    FileGist = open("gist.txt","w")
    for i in range(len(Ygist)):
        FileGist.write(Ygist[i])
        FileGist.write(" ")
    FileGist.write('\n')
    for i in range(len(Xgist)):
        FileGist.write(Xgist[i])
        FileGist.write(" ")       
    print("Гистограмма записана в файл:",'\n', Ygist,'\n', Xgist)
    FileGist.close()

Ygist=[0]*10
Xgist=[99,199,299,399,499,599,699,799,899,999]
a=[random.randint(0, 999) for j in range(1000000)]
    
for i in a:
    if i<100:
        Ygist[0]+=1
    elif (i>100 and i<200):
        Ygist[1]+=1
    elif (i>200 and i<300):
        Ygist[2]+=1
    elif (i>300 and i<400):
        Ygist[3]+=1
    elif (i>400 and i<500):
        Ygist[4]+=1
    elif (i>500 and i<600):
        Ygist[5]+=1
    elif (i>600 and i<700):
        Ygist[6]+=1
    elif (i>700 and i<800):
        Ygist[7]+=1
    elif (i>800 and i<900):
        Ygist[8]+=1
    elif (i>900 and i<999):
        Ygist[9]+=1

Ygist=list(map(str,(Ygist)))
Xgist=list(map(str,(Xgist)))

write_gist(Ygist, Xgist)