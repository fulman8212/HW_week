import RPi.GPIO as GPIO
import time

PWMA = 18  # 왼쪽 모터 PWM 핀
AIN1 = 22  # 왼쪽 모터 방향 핀 1
AIN2 = 27  # 왼쪽 모터 방향 핀 2
PWMB = 23  # 오른쪽 모터 PWM 핀
BIN1 = 24  # 오른쪽 모터 방향 핀 1
BIN2 = 25  # 오른쪽 모터 방향 핀 2

SW1 = 5  
SW2 = 6  
SW3 = 13 
SW4 = 19  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

L_Motor = GPIO.PWM(PWMA, 500)
R_Motor = GPIO.PWM(PWMB, 500)
L_Motor.start(0)
R_Motor.start(0)

try:
    while True:
        if GPIO.input(SW1) == 1:  # 전진
            # 왼쪽모터 
            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 1)
            L_Motor.ChangeDutyCycle(50)  

            # 오른쪽모터
            GPIO.output(BIN1, 1)
            GPIO.output(BIN2, 0)
            R_Motor.ChangeDutyCycle(50)  

        elif GPIO.input(SW2) == 1:  # 오른쪽 회전
            print("SW2: 오른쪽")
            GPIO.output(AIN1, 0)
            GPIO.output(AIN2, 1)
            L_Motor.ChangeDutyCycle(50) 
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            R_Motor.ChangeDutyCycle(50) 

        elif GPIO.input(SW3) == 1:  # 왼쪽 회전
            print("SW3: 왼쪽")
            GPIO.output(AIN1, 1)
            GPIO.output(AIN2, 0)
            L_Motor.ChangeDutyCycle(50)  
            GPIO.output(BIN1, 1)
            GPIO.output(BIN2, 0)
            R_Motor.ChangeDutyCycle(50) 

        elif GPIO.input(SW4) == 1:  # 후진
            print("SW4: 후진")
            GPIO.output(AIN1, 1)
            GPIO.output(AIN2, 0)
            L_Motor.ChangeDutyCycle(50)  
            GPIO.output(BIN1, 0)
            GPIO.output(BIN2, 1)
            R_Motor.ChangeDutyCycle(50)  

        else:
            L_Motor.ChangeDutyCycle(0)
            R_Motor.ChangeDutyCycle(0)

        time.sleep(0.1)  

except KeyboardInterrupt:
    pass


L_Motor.stop()
R_Motor.stop()
GPIO.cleanup()
