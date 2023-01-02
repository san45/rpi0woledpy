import adafruit_ssd1306
import board
import busio
from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen


i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128,64,i2c,addr=0x3c)
# display white on screen
oled.fill(1)
oled.show()

#display black on screen
oled.fill(0)
oled.show()

# display image from web 

url= "https://python-pillow.org/images/pillow-logo.png"
img=  Image.open(urlopen(url)).resize((128,64), Image.ANTIALIAS).convert('1')                                                                             onvert('1')
oled.image(img)
oled.show()

# more https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-usage




