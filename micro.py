import RPi.GPIO as GPIO
from statistics import median
import time
import sys
import led

trig_pin = 15                           # GPIO 15
echo_pin = 14                           # GPIO 14
speed_of_sound = 34370                  # 20℃での音速(cm/s)

GPIO.setmode(GPIO.BCM)                  # GPIOをBCMモードで使用
GPIO.setwarnings(False)                 # BPIO警告無効化
GPIO.setup(trig_pin, GPIO.OUT)          # Trigピン出力モード設定
GPIO.setup(echo_pin, GPIO.IN)           # Echoピン入力モード設定

num_date = []
def get_distance(): 
    #Trigピンを10μsだけHIGHにして超音波の発信開始
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.000010)
    GPIO.output(trig_pin, GPIO.LOW)

    while not GPIO.input(echo_pin):
        pass
    t1 = time.time() # 超音波発信時刻（EchoピンがHIGHになった時刻）格納

    while GPIO.input(echo_pin):
        pass
    t2 = time.time() # 超音波受信時刻（EchoピンがLOWになった時刻）格納

    return (t2 - t1) * speed_of_sound / 2 # 時間差から対象物までの距離計算

for i in range(100):
    num_date.append(get_distance())
door_distance = median(num_date)
while True: # 繰り返し処理
    try:
        distance = get_distance()  # 小数点1までまるめ
        print(distance)
        if distance > 80:
            led.rainbow_cycle(0.001)
        else:
            led.No_led()
    except KeyboardInterrupt:                       # Ctrl + C押されたたら
        GPIO.cleanup()                              # GPIOお片付け
        sys.exit()                                  # プログラム終了