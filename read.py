import CompleteAlphabet
import check
import pyttsx3

def computerSay():
    
    engine=pyttsx3.init()
    
    for i in CompleteAlphabet.name_for_characters:
        print(i)
        engine.say(CompleteAlphabet.say(i))
        engine.runAndWait()

def computerReadAlpha(characters):
       engine=pyttsx3.init()
       print(characters)
       engine.say(CompleteAlphabet.say(characters))
       engine.runAndWait()

def readFromCorpus(characters):
        import pygame
        pygame.mixer.pre_init(44100,16,2,4096)
        pygame.mixer.init()
        rep =check.check(characters)              
        file='sound corpus/'+rep+'.wav'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(2)
        pygame.mixer.music.stop()
    
     

