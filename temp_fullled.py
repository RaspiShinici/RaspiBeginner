from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime
import Adafruit_DHT as DHT


PORT_DHT = 4

PORT_R = 21
PORT_G = 20
PORT_B = 16


GPIO.setmode(GPIO.BCM)
ports = [PORT_R, PORT_G, PORT_B]

for port in ports:
      GPIO.setup(ports, GPIO.OUT)


def set_color(r, g, b):
      GPIO.output(PORT_R, r)
      GPIO.output(PORT_G, g)
      GPIO.output(PORT_B, b)


try:
      while True:
            print("温度計測中…")
            humi, t = DHT.read_retry(DHT.DHT11, PORT_DHT)

            # 異常値は再取得
            if (humi > 90) or (t > 50):
                  print("- error:", humi, t)
                  sleep(0.1)
                  continue

            print("| 温度=", humi, "%")
            print("| 湿度=", t, "度")

            if t < 10:
                  set_color(0, 0, 1) # 青

            elif 10 <= t < 15:
                  set_color(0, 1, 0) # 緑

            elif 15 <= t < 20:
                  set_color(0, 1, 0) # 白

            elif 20 <= t < 25:
                  set_color(0, 1, 0) # 紫

            else:
                  set_color(1, 0, 0) # 赤

            sleep(10)

except:
      pass

GPIO.cleanup()
