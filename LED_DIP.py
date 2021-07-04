# 必要なライブラリのインポート
import RPi.GPIO as GPIO
import time, sys

# ポート番号の指定
PORT_R = 17
PORT_G = 27
PORT_B = 22
# DIPスイッチのポート番号
DIP1 = 5
DIP2 = 6
DIP3 = 13

GPIO.setmode(GPIO.BCM)
ports = [PORT_R, PORT_G, PORT_B]
dips = [DIP1, DIP2, DIP3]

for port in ports:
      GPIO.setup(port, GPIO.OUT)
for port in dips:
      GPIO.setup(port, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LEDをRGBの指定の色に設定
def set_color(r, g, b):
      GPIO.output(PORT_R, r)
      GPIO.output(PORT_G, g)
      GPIO.output(PORT_B, b)
      print(r, g, b)

try:
      while True:
            r = g = b = GPIO.LOW
            if GPIO.input(DIP1) == GPIO.LOW:
                  r = GPIO.HIGH
            if GPIO.input(DIP2) == GPIO.LOW:
                  g = GPIO.HIGH
            if GPIO.input(DIP3) == GPIO.LOW:
                  b = GPIO.HIGH
            set_color(r, g, b)
            time.sleep(0.3)

except KeyboardInterrupt:
      pass
GPIO.cleanup()
