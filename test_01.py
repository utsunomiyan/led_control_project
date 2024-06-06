import RPi.GPIO as GPIO
import time
import serial

# シリアル通信の設定
ser = serial.Serial('devttyUSB0', 9600)  # シリアルポートとボーレートを適宜変更してください

# GPIOピンの設定
LED_PIN = 18  # LEDが接続されているGPIOピン番号

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try
    while True
        # LEDを点灯
        GPIO.output(LED_PIN, GPIO.HIGH)
        ser.write(b'LED ONn')  # シリアルでLED点灯の状態を送信
        print(LED ON)
        time.sleep(1)

        # LEDを消灯
        GPIO.output(LED_PIN, GPIO.LOW)
        ser.write(b'LED OFFn')  # シリアルでLED消灯の状態を送信
        print(LED OFF)
        time.sleep(1)

except KeyboardInterrupt
    print(Ctrl+C pressed. Exiting...)

finally
    GPIO.cleanup()
    ser.close()  # シリアル通信を終了