import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, 0)

led_on = False
while not led_on:
    GPIO.output(21, GPIO.input(20))
    led_on = GPIO.input(20)
    sleep(0.05)

