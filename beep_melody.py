import wiringpi
from time import sleep

PORT = 18
DELAY = 0.5

# 周波数指定
C = 262
D = 294
E = 330
F = 349
G = 392
A = 440
B = 494
R = 0

musical_score = [C,D,E,R, C,D,E,R, G,E,D,C, D,E,D,R,
          C,D,E,R, C,D,E,R, G,E,D,C, D,E,C,C,
          G,G,E,G, A,A,G,R, E,E,D,D, C,R,R,R]

wiringpi.wiringPiSetupGpio()
wiringpi.softToneCreate(PORT)

for tone in musical_score:
    wiringpi.softToneWrite(PORT, tone)
    sleep(DELAY)
    wiringpi.softToneWrite(PORT, 0)
    sleep(0.1)
