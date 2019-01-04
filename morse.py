letters = {
...     'a':['.-'],'b':['-...'],
...     'c':['-.-.'],'d':['-..'],
...     'e':['.'],'f':['..-.'],
...     'g':['--.'],'h':['....'],
...     'i':['..'],'j':['.---'],
...     'k':['-.-'],'l':['.-..'],
...     'm':['--'],'n':['-.'],
...     'o':['---'],'p':['.--.'],
...     'q':['--.-'],'r':['.-.'],
...     's':['...'],'t':['-'],
...     'u':['..-'],'v':['...-'],
...     'w':['.--'],'x':['-..-'],
...     'y':['-.--'],'z':['--..']
...     }


def morsecode(message): 
    message = message.lower() 
    arr = []
    result = ''
    
    for i in range(len(message)):
        arr.append('   ') if message[i] == ' ' else arr.append(letters[message[i]])
        result += arr[i][0] + ' '
    
    return result
