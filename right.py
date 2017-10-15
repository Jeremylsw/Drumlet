import serial
import pygame.mixer
import sys
serRight = serial.Serial(port=sys.argv[1], baudrate=int(sys.argv[2]))
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
bass_drum = pygame.mixer.Sound('./sounds/bass.wav')
mediumTom = pygame.mixer.Sound('./sounds/Tom02.wav')
floorTom = pygame.mixer.Sound('./sounds/Tom03.wav')
ride = pygame.mixer.Sound('./sounds/Ride2.wav')
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel3 = pygame.mixer.Channel(2)
channel4 = pygame.mixer.Channel(3)

while 1:
    hitR = bytes.decode(serRight.readline())
    sys.stdout.write(hitR);
    sys.stdout.flush();
    if hitR[0] == '3':
        print("dum")
        channel1.play(mediumTom)
    elif hitR[0] == '4':
        print("dun")
        channel2.play(floorTom)
    elif hitR[0] == '7':
        print("boom")
        channel3.play(bass_drum)
    elif hitR[0] == '8':
        print("tssssssssssss")
        channel4.play(ride)