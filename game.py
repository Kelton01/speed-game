import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

seven = 11
six = 13
five = 15
four = 16
three = 18
two = 22
one = 24
led_list = [seven,six,five,four,three,two,one]

GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for x in led_list:
	GPIO.setup(x, GPIO.OUT)

def allOff():
	for x in led_list:
		GPIO.output(x, GPIO.LOW)
		
		
def startGame():
	initial_time = time.time()
	elapsed = 0
	level = 2

	while level <= 10:
		button = GPIO.input(32)
		elapsed = time.time() - initial_time
		if elapsed % (7/level) >= (0/level) and elapsed % (7/level) <= (1/level):
			allOff()
			GPIO.output(seven,GPIO.HIGH)
			if button == 0:
				level = 100
		elif elapsed % (7/level) > (1/level) and elapsed % (7/level) <= (2/level):
			allOff()
			GPIO.output(six,GPIO.HIGH)
			if button == 0:
				level = 100
		elif elapsed % (7/level) > (2/level) and elapsed % (7/level) <= (3/level):
			allOff()
			GPIO.output(five,GPIO.HIGH)
			if button == 0:
				level = 100
		elif elapsed % (7/level) > (3/level) and elapsed % (7/level) <= (4/level):
			allOff()
			GPIO.output(four,GPIO.HIGH)
			if button == 0:
				level = 100
		elif elapsed % (7/level) > (4/level) and elapsed % (7/level) <= (5/level):
			allOff()
			GPIO.output(three,GPIO.HIGH)
			if button == 0:
				level = 100
		elif elapsed % (7/level) > (5/level) and elapsed % (7/level) <= (6/level):
			allOff()
			GPIO.output(two,GPIO.HIGH)
			if button == 0:
				level = 100
		elif elapsed % (7/level) > (6/level) and elapsed % (7/level) <= (7/level):
			allOff()
			GPIO.output(one,GPIO.HIGH)
			if button == 0:
				level += 2
				GPIO.output(one,GPIO.HIGH)
				time.sleep(.2)
				GPIO.output(one,GPIO.LOW)
				time.sleep(.2)
				GPIO.output(one,GPIO.HIGH)
				time.sleep(.2)
				GPIO.output(one,GPIO.LOW)
				time.sleep(.2)
				GPIO.output(one,GPIO.HIGH)
				time.sleep(.2)
				GPIO.output(one,GPIO.LOW)
				time.sleep(.2)
				elapsed = 0


start = False

while 1:
	button = GPIO.input(32)
	allOff()
	if button == 0:
		time.sleep(.5)
		startGame()
		time.sleep(.2)
