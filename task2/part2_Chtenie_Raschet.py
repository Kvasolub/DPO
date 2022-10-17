def get_gist():
    FileGist = open("gist.txt","r")
    Ygist=FileGist.readline()
    Xgist=FileGist.readline()
    print("Гистограмма из файла:",'\n', Ygist, Xgist)
    FileGist.close()
    return Ygist,Xgist

Ygist, Xgist = get_gist()

Ygist=Ygist.split()
Xgist=Xgist.split()

Ygist=list(map(int,(Ygist)))
Xgist=list(map(int,(Xgist)))

for i in range(1,len(Xgist)):
   print("Расстояние между",(i+1),"и",(i),"точками",((Xgist[i]-Xgist[i-1])**2+(Ygist[i]-Ygist[i-1])**2)**(1/2))