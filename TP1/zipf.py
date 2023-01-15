from operator import itemgetter  
import os

def frequence(path):
    files = os.listdir(path);
    dico = {}
    for file in files :
        f = open (path+file, "r")
        while True:
            line = f.readline()
            if not line :
                break;
            if line in dico:
                dico[line] = dico[line] + 1
            else:
                dico[line] = 1
        f.close()
    for i in dico:
        print (i,dico[i])
    for elem in reversed(sorted(dico.items(), key = itemgetter(1))):
        print (elem[0],elem[1])
    
frequence("./collections2/")