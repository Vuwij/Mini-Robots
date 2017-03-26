import RPi.GPIO as GPIO
import time
import sys
import curses

# Pin Definitons:
led0 = 19
led1 = 26
key0 = 18
key1 = 23

motorNE = 5
motorNW = 6
motorSE = 16
motorSW = 20


GPIO.setmode(GPIO.BCM)
GPIO.setup(led0, GPIO.OUT) 
GPIO.setup(led1, GPIO.OUT) 
GPIO.setup(motorNE, GPIO.OUT) 
GPIO.setup(motorNW, GPIO.OUT) 
GPIO.setup(motorSE, GPIO.OUT) 
GPIO.setup(motorSW, GPIO.OUT) 
GPIO.setup(key0, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(key1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

def main(stdscr):
	step = 0
	power = 10
	ne = nw = se = sw = 0
	stdscr.nodelay(1)
	try:
	    while 1:
		step += 1
		input = stdscr.getch()
		if input != -1:
			print "keypressed", input
			if input == 119:
				ne = 1
				nw = 1
				se = 1
				sw = 1
			if input == 97:
				ne = 0.5
				nw = 1
				se = 0.5
				sw = 1
			if input == 115:
				ne = 0
				nw = 0
				se = 0
				sw = 0
			if input == 100:
				ne = 1
				nw = 0.5
				se = 1
				sw = 0.5
			if input == 259:
				if (power < 10):	
					power += 1
			if input == 258:
				if (power > 1):
					power -= 1
		a = GPIO.input(key0)
		b = GPIO.input(key1)
				
		GPIO.output(led0, a)
		GPIO.output(led1, b)
		if nw == 0:
			GPIO.output(motorNW, 0)
		else:
			GPIO.output(motorNW, (step % 10) - (nw*power) < 0)
		if ne == 0:
			GPIO.output(motorNE, 0)
		else:
			GPIO.output(motorNE, (step % 10) - (ne*power) < 0)
		if sw == 0:
			GPIO.output(motorSW, 0)
		else:
			GPIO.output(motorSW, (step % 10) - (sw*power) < 0)
		if se == 0:
			GPIO.output(motorSE, 0)
		else:
			GPIO.output(motorSE, (step % 10) - (se*power) < 0)
	
		#print nw*power, " ", ne*power, " ", se*power, " ", sw*power, " ", a, " ", b
		time.sleep(0.003)

	except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
	    pwm.stop() # stop PWM
	    GPIO.cleanup() # cleanup all GPIO

if __name__ == '__main__':
	curses.wrapper(main)
