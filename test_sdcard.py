from machine import Pin, SPI
from sdcard import SDCard

spi = SPI(1, baudrate=40000000, sck=Pin(2), mosi=Pin(3), miso=Pin(4))
try:
    sd = SDCard(spi, Pin(1, Pin.OUT))
except:
    sd = SDCard(spi, Pin(1, Pin.OUT))
vfs = os.VfsFat(sd)
os.mount(vfs, "/sd")

for e in os.listdir('/sd'):
    print(e)