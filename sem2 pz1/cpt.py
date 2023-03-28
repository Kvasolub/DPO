znaki = ['?', '.', ',', '!', ':', '(', ')', '-', "'",]
Avoid = []
word_count = {}
word_count_dec = {}
word_count_fan = {}
deleted_count = 0
genre = 0
countDec = 0
countFan = 0

def COUNT(word, ge):
        word=word.lower()
        if ge == 0:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        elif ge == 1:
            if word not in word_count_dec:
                word_count_dec[word] = 1
            else:
                word_count_dec[word] += 1     
        else:
            if word not in word_count_fan:
                word_count_fan[word] = 1
            else:
                word_count_fan[word] += 1                     

def DelText(reTEXT, gen, Avoid):
    Text = []
    LinesText = len(reTEXT.readlines())
    reTEXT.seek (0,0)
    
    for i in range(0,LinesText):
        OneLine = str(reTEXT.readline()).split()
        Text += OneLine

    for i in range (0,len(Text)):
        list_text = list(Text[i-deleted_count])
        for j in range (0,8):
            if list_text[0] == znaki[j]:
                list_text[0]=''
            if list_text[len(Text[i-deleted_count])-1] == znaki[j]:
                list_text[len(Text[i-deleted_count])-1]=''
        list_text =  ''.join(list_text)
        s = 0
        for wordAvoid in Avoid:
            if list_text.lower() == wordAvoid or list_text == '':
                s = 1
                break
        if s != 1:
            COUNT(list_text,gen)


Avoid_text = open("iskl.txt","r", encoding = 'utf-8')

LinesAvoid = len(Avoid_text.readlines())
Avoid_text.seek (0,0)

for i in range(0,LinesAvoid):
    OneLine = str(Avoid_text.readline()).split()
    Avoid += OneLine

File_text = open("primer2.txt","r", encoding = 'utf-8')
DelText(File_text, genre, Avoid)

genre = 1

Ntext = open("dec1.txt","r", encoding = 'utf-8')
DelText(Ntext, genre, Avoid)
Ntext = open("dec2.txt","r", encoding = 'utf-8')
DelText(Ntext, genre, Avoid)
Ntext = open("dec3.txt","r", encoding = 'utf-8')
DelText(Ntext, genre, Avoid)
Ntext = open("dec4.txt","r", encoding = 'utf-8')
DelText(Ntext, genre, Avoid)

genre = 2

Ntext = open("fan1.txt","r", encoding = 'utf-8')
DelText(Ntext, genre, Avoid)
Ntext = open("fan2.txt","r", encoding = 'utf-8')
DelText(Ntext, genre, Avoid)
Ntext = open("fan3.txt","r", encoding = 'utf-8')
DelText(Ntext, genre, Avoid)
Ntext = open("fan4.txt","r", encoding = 'utf-8')
DelText(Ntext, genre, Avoid)

for keyText, valueText in word_count.items():
    if valueText == 1:
        break
    for keyDec, valueDec in word_count_dec.items():
        d = abs(valueText - valueDec)
        for keyFan, valueFan in word_count_fan.items():
            f = abs(valueText - valueFan)
    if d > f:
        countDec += 1
    else:
        countFan += 1

if countDec > countFan:
    print('Похоже на детектив')
else:
    print('Похоже на фантастику')  