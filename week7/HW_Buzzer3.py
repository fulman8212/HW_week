import RPi.GPIO as GPIO
import time

BUZZER = 12
SW1 = 5

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

p = GPIO.PWM(BUZZER, 261)
p.start(0)  

try:
    while True:
        sw1Value = GPIO.input(SW1)

        if sw1Value == 1:
            p.start(50)  
               
            frequencies = [262, 294, 330, 349, 392, 440, 494, 523]
           
            p.ChangeFrequency(frequencies[0])
            time.sleep(0.5)

            p.ChangeFrequency(frequencies[0])
            time.sleep(0.5)

            p.ChangeFrequency(frequencies[0])
            time.sleep(0.5)

            p.ChangeFrequency(frequencies[4])
            time.sleep(0.5)

            p.ChangeFrequency(frequencies[4])
            time.sleep(0.5)

            p.ChangeFrequency(frequencies[2])
            time.sleep(0.5)

            p.ChangeFrequency(frequencies[1])
            time.sleep(0.5)
            
            p.stop()  
            time.sleep(0.5) 

        time.sleep(0.1)  

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
