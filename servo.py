import pigpio 

import time
SERVO_PIN_1 = 13 #Pin番号
SERVO_PIN_2 = 12 #Pin番号
pi = pigpio.pi()#pigpioの設定
def set_angle(angle, NowServo): #サーボモーターの角度を設定する関数 angle:角度 NowServo:動かしたいサーボモーターの番号
    assert 0 <= angle <= 180, 'No' #角度の範囲が異なった場合にエラーをはく
    pulse_width = (angle / 180) * (2500 - 500) + 500 #PWM制御する
    if NowServo == 1: #サーボモーター1の角度を変える
        pi.set_servo_pulsewidth(SERVO_PIN_1,pulse_width)
    elif NowServo == 2: #サーボモーター2の角度を変える
        pi.set_servo_pulsewidth(SERVO_PIN_2,pulse_width)
def lock(Islock,NowServo): #鍵の開閉の関数IslockがFalseで閉じるTrueで開く
    if Islock == False:
        set_angle(90,NowServo)
        time.sleep(1)
    elif Islock == True:
        set_angle(0,NowServo)
        time.sleep(1)
lock(False,1)
lock(True,1)



