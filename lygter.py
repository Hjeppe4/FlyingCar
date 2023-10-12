import RPi.GPIO as GPIO
import wiringpi as wiringpi
import time
wiringpi.wiringPiSetupGpio()

light1 = 12
light2 = 13

wiringpi.softPwmCreate(light1, 0, 100) 
wiringpi.softPwmCreate(light2, 0, 100)
print("test")

wiringpi.softPwmWrite(light1, 100)
wiringpi.softPwmWrite(light2, 100)
print("test  2")
time.sleep(3)
wiringpi.softPwmWrite(light1, 0)
wiringpi.softPwmWrite(light2, 0)
print ("test 3 ")