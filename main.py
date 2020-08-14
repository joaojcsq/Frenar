import RPi.GPIO as GPIO
import MAX6675.MAX6675 as MAX6675
from smbus2 import SMBus
from mlx90614 import MLX90614
import time
CSK = 25
CS = 24
DO = 18

sensor_termopar = MAX6675.MAX6675(CSK, CS, DO)

bus = SMBus(1)
sensor_IR = MLX90614(bus, address=0x5A)

try:
    while True:
        time.sleep(5)
        Temp_termopar = sensor_termopar.readTempC()
        Temp_IR = sensor_IR.get_object_1()
        print("#"*30)
        print("Temperatura Termopar ==> {0:0.2F}".format(Temp_termopar))
        print("Temperatura IR ==> {0:0.2F}".format(Temp_IR))

except KeyboardInterrupt:
        print("Finalizado...")
        bus.close()
        GPIO.cleanup()
