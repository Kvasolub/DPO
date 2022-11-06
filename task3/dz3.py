class Normaliz ():
    def __init__(self,gist):
        a=gist.split() 
        self.Norma=list(map(int,(a)))

def get_new():
    FileGist = open("new_gist.txt","r")
    Xgist=FileGist.readline()
    Ygist=FileGist.readline()
    print("Гистограмма из new файла:",'\n', Xgist, Ygist)
    FileGist.close()
    return Xgist,Ygist

NewX,NewY=get_new()
NewX=Normaliz(NewX).Norma
NewY=Normaliz(NewY).Norma

FileGist = open("gist.txt","r")
minsum=0
sumD=0
mintype=0

while True:
    typeG=FileGist.readline()
    if typeG =='':
        break
    Xgist=FileGist.readline()
    Ygist=FileGist.readline()   
    Xgist=Normaliz(Xgist).Norma
    Ygist=Normaliz(Ygist).Norma

    for i in range(0, len(Xgist)):
        dlina=((NewX[i]-Xgist[i])**2+(NewY[i]-Ygist[i])**2)**1/2
        sumG=+dlina
    if mintype==0:
        minsum=sumG
        mintype=typeG
    else:
        if sumG<minsum:
            minsum=sumG
            mintype=typeG              
    sumG=0

print(mintype)