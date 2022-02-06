import CompleteAlphabet

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
        rep =characters
        if (characters == 'ሐ') or (characters== 'ኀ') or (characters== 'ሃ') or (characters== 'ሓ') or (characters== 'ኃ'):
              print(characters)  
              rep='ሀ'
            
        if (characters == 'ሑ') or (characters== 'ኁ') :
              print(characters)
              rep='ሁ'

        if (characters == 'ሒ') or (characters== 'ኂ') :
              print(characters)
              rep = 'ሂ' 

        if (characters == 'ሔ') or (characters== 'ኄ') :
              print(characters)
              rep='ሄ'
                
        if (characters == 'ሕ') or (characters== 'ኅ') :
              print(characters)
              rep='ህ'
            
        if (characters == 'ሖ') or (characters== 'ኆ') :
              print(characters)
              rep='ሆ'

        if (characters == 'ሰ'):
              print(characters)
              rep='ሠ'
          
        if (characters == 'ሱ'):
              print(characters)
              rep='ሡ'
             
        if (characters == 'ሲ'):
              print(characters)
              rep='ሢ'
            
        if (characters == 'ሳ'):
              print(characters)
              rep='ሣ'
            
        if (characters == 'ሴ'):
              print(characters)
              rep='ሤ'

        if (characters == 'ስ'):
              print(characters)
              rep='ሥ'

        if (characters == 'ሶ'):
              print(characters)
              rep='ሦ'      
            
        file='sound corpus/'+rep+'.wav'
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(2)
        pygame.mixer.music.stop()
    
     

