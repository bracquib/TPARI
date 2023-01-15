
from nltk.tokenize import RegexpTokenizer
import os
outpath = "./collections2/"

def tokenize(path):
    files = os.listdir(path);
    for file in files :
        print ("processing file "+file)
        fileHandler = open (path+file, "r")
        out= open (outpath+file+".tok", "w")
        print ("file opened")
        while True:
            line = fileHandler.readline()
            if not line :
                break;
            words = line
            print (words)
            tokenizer = RegexpTokenizer('[A-Za-z]\w{1,}') 
            words2 = tokenizer.tokenize(words)
            for word in words2:
                word3=word.lower()
                out.write(word3+"\n")
        fileHandler.close()
        out.close()


tokenize("./collections/")
