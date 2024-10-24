import RPi.GPIO as GPIO
import time

BUZZER = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

p = GPIO.PWM(BUZZER, 261) 
p.start(0)


freq = [261, 294, 330, 349]  # SW1, SW2, SW3, SW4에 해당하는 주파수

switch_pins = [5, 6, 13, 19]


for pin in switch_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        for i, pin in enumerate(switch_pins):
            if GPIO.input(pin) == GPIO.HIGH:  
                p.ChangeFrequency(freq[i])  
                p.start(50)  
                time.sleep(0.5) 
                p.stop()  
                time.sleep(0.1)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
