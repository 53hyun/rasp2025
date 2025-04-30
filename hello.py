import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

LED = 11, 13, 15

GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

try:
    while 1:
        switch = int(input(''))
        
        if switch == 1:
            
            GPIO.output(LED,GPIO.HIGH)
        
        elif switch == 0:
            
            GPIO.output(LED,GPIO.LOW)
            
except Keyboardinterrupt:
    
    pass
    
finally:
    
    GPIO.cleanup()