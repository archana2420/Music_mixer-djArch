import pygame
from pygame import mixer

pygame.mixer.init()
mixer.music.load('Music/Step On Up.mp3')
mixer.music.set_volume(0.9)
mixer.music.play(-1)
sound_effects_1=pygame.mixer.Sound('Music/gimme more.mp3')
sound_effects_1.set_volume(0.5)
# sound_effects_2=pygame.mixer.Sound('new begining.mp3')
# sound_effects_2.play(-1)
# raw_array=sound_effects_2.get_raw()
# raw_array=raw_array[100000:150000]
# edit_1=pygame.mixer.Sound(buffer=raw_array)
# edit_1.play(-1)
while True:
    print("1.play,2.stop,3.add effect 4.quit")
    a=input()
    if a=='1':
        mixer.music.play(-1)
    elif a=='2':
        mixer.music.fadeout()
        mixer.music.stop()
    elif a=='3':
        sound_effects_1.play()
    elif a=='4':
        break