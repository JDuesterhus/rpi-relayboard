##################################################
#	CHANNEL		RPI pin		wiringPi	BCM
#	CH1			29			P21			5			
#	CH2			31			P22			6
#	CH3			33			P23			13
#	CH4			36			P27			16
#	CH5			35			P24			19
#	CH6			38			P28			20
#	CH7			40			P29			21
#	CH8			37			P25			26
##################################################
#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

try:
	RelayChannel = [5,6,13,16,19,20,21,26]
	#RelayState = [0,0,0,0,0,0,0,0]

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(RelayChannel, GPIO.OUT, initial=GPIO.HIGH)

	print("Setup The Relay Module is [success]")

	def OpenRelay(channel):
		GPIO.output(RelayChannel[channel], GPIO.LOW)
		print("Channel ", channel, " open")

	def CloseRelay(channel):
		GPIO.output(RelayChannel[channel], GPIO.HIGH)
		print("Channel ", channel, " close")

	def ToggleRelay(channel):
		if GPIO.input(RelayChannel[channel]) == 0:
			GPIO.output(RelayChannel[channel], GPIO.HIGH)
			print("Channel ", channel, " close")
		else:
			GPIO.output(RelayChannel[channel], GPIO.LOW)
			print("Channel ", channel, " open")

	while True:
		#OpenRelay(1)
		ToggleRelay(1)
		time.sleep(0.5)
		#CloseRelay(1)
		time.sleep(2)


except:
	print("exception")
	GPIO.cleanup()

