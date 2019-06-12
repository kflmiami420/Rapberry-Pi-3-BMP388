import bmp388
import time

bmp = bmp388.bmp388()

#Mandatory: GPIO hardware setup to provide information where the cables are connected
bmp.gpio_setup(SCK=32, SDO=36, SDI=38, CS=40)

#Optional: detailed configuration
#bmp.configure(standby_time=0, iir_filter=0, spi_3_wire=0, pressure_oversampling=16, temperature_oversampling=2, power_mode="NORMAL")

# First measurement should be discarded as it might be invalid depending on IIR filter settings
bmp.measure()

for i in range(0, 10):
    bmp.measure()
    print("Temperature: {:.5f} [°C]".format(bmp.temperature))
    print("Pressure: {:.5f} [hPa]".format(bmp.pressure / 100))
    time.sleep(1)
