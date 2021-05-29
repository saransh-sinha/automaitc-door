import uos
import utime
#from Servo import Servo
from machine import Pin, UART

print(uos.uname())

#indicate program started visually
led_onboard = Pin(25, Pin.OUT)
led_off = Pin(2, Pin.OUT, Pin.PULL_DOWN)
led_on = Pin(3, Pin.OUT, Pin.PULL_DOWN)
led_onboard.value(0)
led_off.value(0)
led_on.value(0)
utime.sleep(0.1)
led_onboard.value(1)     # Servo Full Sweep Start
uart = UART(0, 9600)
#servo = Servo(2)
led_onboard.value(0)     # Servo Full Sweep End


while True:
    command = uart.read(1)
    
    if("1" in command):
        print("Light OFF")
        led_onboard.value(0)
        led_off.value(1)
        led_on.value(0)
        #servo.GoToDegree(135)
    
    elif("2" in command):
        print("Light ON")
        led_onboard.value(1)
        led_off.value(0)
        led_on.value(1)
        #servo.GoToDegree(45)
    
    utime.sleep_ms(100)
