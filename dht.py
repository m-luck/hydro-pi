import RPi.GPIO as GPIO
import dht11
import time
import datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=17)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print(f"Temperature: {result.temperature}")
        print(f"Humidity: {result.humidity}")
    else: 
        print('nothing'+str(result.error_code))
    time.sleep(1)

