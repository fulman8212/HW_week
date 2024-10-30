import serial
import threading
import RPi.GPIO as GPIO
import time

gData = ""
data_lock = threading.Lock()

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

PWMA = 18
PWMB = 23
AIN1 = 22
AIN2 = 27
BIN1 = 25
BIN2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

left_motor = GPIO.PWM(PWMA, 100)
right_motor = GPIO.PWM(PWMB, 100)
left_motor.start(0)
right_motor.start(0)

def go():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    left_motor.ChangeDutyCycle(50)
    right_motor.ChangeDutyCycle(50)
    print("Car is moving forward")

def back():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    left_motor.ChangeDutyCycle(50)
    right_motor.ChangeDutyCycle(50)
    print("Car is moving backward")

def left():
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(BIN1, GPIO.LOW)
    GPIO.output(BIN2, GPIO.HIGH)
    left_motor.ChangeDutyCycle(50)
    right_motor.ChangeDutyCycle(50)
    print("Car is turning left")

def right():
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    GPIO.output(BIN1, GPIO.HIGH)
    GPIO.output(BIN2, GPIO.LOW)
    left_motor.ChangeDutyCycle(50)
    right_motor.ChangeDutyCycle(50)
    print("Car is turning right")

def stop():
    left_motor.ChangeDutyCycle(0)
    right_motor.ChangeDutyCycle(0)
    print("Car has stopped")

def serial_thread():
    global gData
    while True:
        if ser.in_waiting > 0:
            with data_lock:
                gData = ser.readline().decode().strip()
                print(f"Received command: {gData}")

def main():
    global gData
    last_command = ""  

    while True:
        with data_lock:
            command = gData
        if command != last_command:  
            if command == "B0":
                go()
            elif command == "B3":
                back()
            elif command == "B1":
                left()
            elif command == "B2":
                right()
            elif command == "B4":
                stop()

            last_command = command 

        if command == "B4":
            with data_lock:
                gData = ""

if __name__ == "__main__":
    try:
        thread = threading.Thread(target=serial_thread)
        thread.start()

        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        ser.close()
