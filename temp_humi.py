from time import sleep
from datetime import datetime
import Adafruit_DHT as DHT


PIN = 4


for i in range(10):
      while True:
            humi, temp = DHT.read_retry(DHT.DHT11, PIN)
            # 異常な値なら再取得
            if (humi > 90) or (temp > 50):
                  print("- error:", humi, temp)
                  sleep(0.1)
                  continue
            break　

      # 情報を表示
      print("========")
      print("計測日時: ", datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'))
      print("********")
      print("湿度: ", humi, "%")
      print("********")
      print("温度: ", temp, "度")
      sleep(5)
