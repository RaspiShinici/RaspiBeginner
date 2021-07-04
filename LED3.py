# GPIOモジュール
import RPi.GPIO as GPIO
# timeモジュール
import time
# sysモジュール
import sys

# PIN番号
PIN1 = 7
PIN2 = 11
PIN3 = 13

# PIN番号を指定するBOARDモードに設定
GPIO.setmode(GPIO.BOARD)
# 出力PIN指定
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)


# LEDの点滅を交互に繰り返す
while True:
      try:
            # LED1点灯
            GPIO.output(PIN1, GPIO.HIGH)
            GPIO.output(PIN2, GPIO.LOW)
            GPIO.output(PIN3, GPIO.LOW)
            # 0.2秒待機
            time.sleep(0.2)
            # LED2点灯
            GPIO.output(PIN1, GPIO.LOW)
            GPIO.output(PIN2, GPIO.HIGH)
            GPIO.output(PIN3, GPIO.LOW)
            time.sleep(0.2)
            # LED3点灯
            GPIO.output(PIN1, GPIO.LOW)
            GPIO.output(PIN2, GPIO.LOW)
            GPIO.output(PIN3, GPIO.HIGH)
            # 0.2秒待機
            time.sleep(0.2)

      # Ctrl+Cが押された時の処理
      except KeyboardInterrupt:
            # 全てのLEDをLOWにする
            GPIO.output(PIN1, GPIO.LOW)
            GPIO.output(PIN2, GPIO.LOW)
            GPIO.output(PIN3, GPIO.LOW)
            GPIO.cleanup()
            # プログラム終了
            sys.exit()
            
            
      
      
