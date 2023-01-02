import adafruit_ssd1306
import board
import busio
from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen

def init():
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(128,64,i2c,addr=0x3c)
    # display white on screen
    oled.fill(1)
    oled.show()

#display black on screen
def clrscr():
    oled.fill(0)
    oled.show()

# display image from web 

def disp_image(url):
    clrscr()
    #url= "https://python-pillow.org/images/pillow-logo.png"
    img=  Image.open(urlopen(url)).resize((128,64), Image.ANTIALIAS).convert('1')
    oled.image(img)
    oled.show()


def disp_text(text,x,y):
    font = ImageFont.load_default()
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    draw.text((x, y), text, font=font, fill=255)
    oled.image(image)
    oled.show()


# more https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-usage




