import RPi.GPIO as GPIO
import time


PWMA = 18  # 왼쪽 모터 PWM 핀
AIN1 = 22  # 왼쪽 모터 방향 핀 1
AIN2 = 27  # 왼쪽 모터 방향 핀 2
PWMB = 23  # 오른쪽 모터 PWM 핀
BIN1 = 24  # 오른쪽 모터 방향 핀 1
BIN2 = 25  # 오른쪽 모터 방향 핀 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

L_Motor = GPIO.PWM(PWMA, 500)
R_Motor = GPIO.PWM(PWMB, 500)
L_Motor.start(0)
R_Motor.start(0)

try:
    while True:
        # 왼쪽 
        GPIO.output(AIN1, 0)
        GPIO.output(AIN2, 1)
        L_Motor.ChangeDutyCycle(50)  

        # 오른쪽
        GPIO.output(BIN1, 1)
        GPIO.output(BIN2, 0)
        R_Motor.ChangeDutyCycle(50)  

        time.sleep(1.0) 

       
        L_Motor.ChangeDutyCycle(0)  
        R_Motor.ChangeDutyCycle(0)  

        time.sleep(1.0)  

except KeyboardInterrupt:
    pass

L_Motor.stop()
R_Motor.stop()
GPIO.cleanup()
