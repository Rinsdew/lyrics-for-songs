import sys
from time import sleep
import time
#Lyrics of the song that will be displayed, with numbers indicating the duration of each word.
def print_lyrics():
    lines = [
        ("Well you can have my mustang", 0.08),
        ("That's all I've got in my name", 0.08),
        ("But Jesus Christ don't break my heart", 0.08),
        ("This wedding ring won't ever wipe off", 0.08),
    ]
    #Delay time between each line of the lyrics.
    delays = [0.6, 0.7, 0.6, 0.7]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush() #ensures that the characters are printed one by one without waiting for the buffer to fill up.
            sleep(char_delay) #introduces a small delay between printing each character.
        time.sleep(delays[i]) #introduces a delay between printing each line.
        print('')

print_lyrics()
