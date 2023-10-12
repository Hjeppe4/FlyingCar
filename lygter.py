import RPi.GPIO as GPIO
import wiringpi as wiringpi
import time
wiringpi.wiringPiSetupGpio()

light1 = 14
light2 = 15

wiringpi.softPwmCreate(light1, 0, 180) 
wiringpi.softPwmCreate(light2, 0, 100)

wiringpi.softPwmWrite(light1, 180)
wiringpi.softPwmWrite(light2, 180)
time.sleep(3)
wiringpi.softPwmWrite(light1, 0)
wiringpi.softPwmWrite(light2, 0)