# GPIOモジュール
import RPi.GPIO as GPIO
# timeモジュール
import time

# PIN番号
PIN = 7
# PIN番号を指定するBOARDモードに設定
GPIO.setmode(GPIO.BOARD)
# 出力PIN指定
GPIO.setup(PIN, GPIO.OUT)

# LEDの点滅を10回繰り返す
for i in range(10):
      num = i + 1
      print(f'{num}回目の点灯')
      # LED点灯
      GPIO.output(PIN, GPIO.HIGH)
      # 0.2秒待機
      time.sleep(0.2)
      # LED消灯
      GPIO.output(PIN, GPIO.LOW)
      time.sleep(0.2)

# 全てのGPIOピンを解放
GPIO.cleanup()
