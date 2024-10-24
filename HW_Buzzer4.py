import RPi.GPIO as GPIO
import time

BUZZER = 12


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)


p = GPIO.PWM(BUZZER, 261)
p.start(0)  

freq = [261, 294, 330, 349, 392, 440, 494, 523]

try:
    while True:

        p.start(50)  
        p.ChangeFrequency(freq[2])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[1])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[0])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[1])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[2])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[2])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[2])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[1])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[1])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[1])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[2])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[4])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[4])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[2])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[1])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[0])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[1])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[2])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[2])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[2])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[1])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[1])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[2])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[1])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

        p.start(50)  
        p.ChangeFrequency(freq[0])
        time.sleep(0.5)  
        p.stop()  
        time.sleep(0.1) 

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
