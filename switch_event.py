# 必要なライブラリのインポート
import RPi.GPIO as GPIO
import time


# ピン番号を指定
SWITCH = 12
LED = 40
# LEDの状態を定義
LED_VALUE = GPIO.LOW

# ピン番号を指定するBOARDモードに設定
GPIO.setmode(GPIO.BOARD)
# ピン番号12を入力に設定(プルダウン抵抗)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# ピン番号40を出力に設定
GPIO.setup(LED, GPIO.OUT)

# スイッチの切替イベントの定義
def callback_change_switch(INPUT):
      global LED_VALUE
      
      if LED_VALUE == GPIO.LOW:
            GPIO.output(LED, GPIO.HIGH)
            LED_VALUE = GPIO.HIGH
            print('LED点灯')
      else:
            GPIO.output(LED, GPIO.LOW)
            LED_VALUE = GPIO.LOW
            print('LED消灯')
                  
# イベント設定
GPIO.add_event_detect(
      SWITCH,
      GPIO.RISING,
      callback=callback_change_switch,
      bouncetime=200)

try:
      print('now running...')
      while True:
            time.sleep(0.1)

except KeyboardInterrupt:
      GPIO.cleanup()
      
