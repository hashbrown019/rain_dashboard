import RPi.GPIO as GPIO
import time

# import board
# import adafruit_dht
import msg
import conf
from lcd_l2c import lcd_
import _send_http_


POWER_PIN = 21  # GPIO pin tpara sa manuall power sa RAIN module
DO_PIN = 7     # GPIO pin Data para sa Rain module

print("starting ")
msg.kill_serial()
print("Running ")

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(POWER_PIN, GPIO.OUT)  # configure the power pin as an OUTPUT
	GPIO.setup(DO_PIN, GPIO.IN)




def get_rain_senso():
	setup()
	GPIO.output(POWER_PIN, GPIO.HIGH)  # turn the rain sensor's power ON
	time.sleep(0.01)                   # wait 10 milliseconds
	rain_state = GPIO.input(DO_PIN)
	GPIO.output(POWER_PIN, GPIO.LOW)
	if rain_state == GPIO.HIGH:
		return "0"
	else:
		return "1"

TRIG_PIN=11
ECHO_PIN=12
def ultra_sonic():
	setup()
	TRIG = 23
	ECHO = 24
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	GPIO.output(TRIG, False)
	# print( "Waiting For Sensor To Settle")
	time.sleep(1)
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()      

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	print( "Distance:",distance,"cm")
	return distance


def loop(mm,hmm):
	msg.kill_serial()
	RAIN = get_rain_senso()
	DISTANCE = float("{:.1f}".format(ultra_sonic()))
	STAT = 'idle'
	if(DISTANCE <= conf.WATER_LEVEL_LIMIT):
		STAT = "danger"
		msg.kill_serial()
		if(hmm):
			
			msg.send_msg(f"Warning\nDanger Flood\n{conf.TEST_SITE_CNAME}\nWater Level High at {DISTANCE} \nWith Raindrops {RAIN}/sec")
		else:
			mm = "GSM not Ready"
	else:
		pass
	
	_send_http_.snet_data(DISTANCE,RAIN,STAT)
	lcd_(f'D/s:{RAIN}, lvl:{DISTANCE}     {mm}')





# ================================================================
def cleanup():
	msg.kill_serial()
	GPIO.cleanup()

note_msg = ""
if __name__ == "__main__":
	try:
		setup()
		count_down_msg = 5
		while True:
			hmm = count_down_msg==0
			if(hmm):
				note_msg = "GSM Ready"
			else:
				note_msg = f"GSM in [{count_down_msg}] "
				count_down_msg -= 1
			loop(note_msg,hmm)
			time.sleep(0.5)  # pause for 1 second to avoid reading sensors frequently and prolong the sensor lifetime
	except KeyboardInterrupt:
		lcd_("Terminated")
		cleanup()
	except Exception as e:
		lcd_(f"ERROR : {e}")
		cleanup()
		raise e
