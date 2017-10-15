import serial
import pygame.mixer
import sys
serLeft = serial.Serial(port=sys.argv[1], baudrate=int(sys.argv[2]))
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
snare = pygame.mixer.Sound('./sounds/snare.wav')
hihat = pygame.mixer.Sound('./sounds/HiHat1.wav')
smallTom = pygame.mixer.Sound('./sounds/Tom01.wav')
crash = pygame.mixer.Sound('./sounds/Cymbal 01.wav')
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)

while 1:
    hitL = bytes.decode(serLeft.readline())
    sys.stdout.write(hitL)
    sys.stdout.flush()
    if hitL[0] == '1':
        print("dumm")
        channel2.play(snare)
    elif hitL[0] == '2':
        print("dum")
        channel3.play(smallTom)
    elif hitL[0] == '5':
        print("tss")
        channel4.play(hihat)
    elif hitL[0] == '6':
        print("tssssssss")
        channel4.play(crash)