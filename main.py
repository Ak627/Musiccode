from pygame import mixer
mixer.init()
import random
num = random.randrange(1, 3)
while True:
    try:
        x = int(input("1 to play Simpsons theme, 2 to play UP theme, 3 to play Family Guy theme, enter 4 to shuffle: "))
    except:
        print("Not a number")
        break
    if x == 1:
        mixer.music.load("simpsons.mp3")
    elif x == 2:
        mixer.music.load("marriedlife.mp3")
    elif x == 3:
        mixer.music.load("familyguy.mp3")
    elif x == 4:
        num = random.randrange(1, 3)
        if num == 1:
            mixer.music.load("simpsons.mp3")
        elif num == 2:
            mixer.music.load("marriedlife.mp3")
        elif num == 3:
                    mixer.music.load("familyguy.mp3")


    mixer.music.set_volume(0.7)
    mixer.music.play()
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input(" ")
    
    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break
