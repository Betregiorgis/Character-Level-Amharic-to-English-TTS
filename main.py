import read
from os import execv
import sys
op = str(input("Type 'c' convert text to speech using computer TTS feature: \nType 's' to use text to speech from custom sound corpus: \nType 'f' to list and convert text to speech all alphabets in the corpus automaticaly using0 the built in TTS feature: "))

if op=='f':
    
    read.computerSay()
   
if op=='s':
    
    char = str(input("Input Character to read: "))
    
    read.readFromCorpus(char)

if op=='c':
    
    char = str(input("Input Character to read: "))
    
    read.computerReadAlpha(char)

    if __name__=='__main__':
            #os.fsync(fd)
            execv(sys.argv[0],sys.argv)
