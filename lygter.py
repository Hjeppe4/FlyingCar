import RPi.GPIO as GPIO
import wiringpi as wiringpi
wiringpi.wiringPiSetupGpio()

light1 = 14
light2 = 15

wiringpi.softPwmCreate(light1, 0, 180) 
wiringpi.softPwmCreate(light2, 0, 180 

wiringpi.softPwmWrite(light1, 180)
wiringpi.softPwmWrite(light2, 180)