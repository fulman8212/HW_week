import RPi.GPIO as GPIO
import time

switch_pins = [5, 6, 13, 19]
switch_counts = [0] * 4  
switch_status = [0] * 4  

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in switch_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        for i, pin in enumerate(switch_pins):
            current_status = GPIO.input(pin)
            if current_status == GPIO.HIGH and switch_status[i] == GPIO.LOW:
                switch_counts[i] += 1
                print(f'SW{ i + 1 } click', switch_counts[i])
            switch_status[i] = current_status
        time.sleep(0.18)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
