
import time
import board
import busio
import adafruit_bmp3xx

i2c = busio.I2C(board.SCL, board.SDA)
bmp388 = adafruit_bmp3xx.BMP3XX_I2C(i2c)

bmp388.pressure_oversampling = 8
bmp388.temperature_oversampling = 2

bmp388.sea_level_pressure = 1015.7  #(1015.7 hectopascals at my location)

while True:
    print("--------------------------")
    print("Temperature:  {0:0.2f} Deg C ".format(bmp388.temperature))
    print("Pressure:     {:6.1f}  HpA   ".format(bmp388.pressure))
    print("Altitude:     {0:0.2f} Press ".format(bmp388.sea_level_pressure))
    time.sleep(1)
