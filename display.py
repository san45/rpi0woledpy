import adafruit_ssd1306
import board
import busio
import requests
import time
from PIL import Image, ImageDraw, ImageFont
from urllib.request import urlopen


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


def disp_text(text):
    font = ImageFont.load_default()
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)
    l=len(text)
    if  l in range(21,127):
        for i in range(0,l//21+1):
            draw.text((0, i*10), text[i*21:], font=font, fill=255)
            print( text[i*21:],i)
    elif l > 127:
        for i in range(0,5):
            draw.text((0, i*10), text[i*21:], font=font, fill=255)
            print( text[i*21:],i)
        lastline= text[5*21:5*21+21-3]+"..."
        draw.text((0, 50),lastline, font=font, fill=255)
        print(lastline,5)
    else:
            draw.text((0, 0), text, font=font, fill=255)
    oled.image(image)
    oled.show()

def news_reader(token):
    url=f"https://newsapi.org/v2/top-headlines?country=in&apiKey={token}"
    response=requests.get(url)
    if response.status_code == 200 :
        resp_json=response.json()
        for each in resp_json['articles']:
            if each['urlToImage'] :
                disp_image(each['urlToImage'])
                time.sleep(2)
            if each['title'] :
                disp_text(each['title'])
                time.sleep(5)
    else:
        disp_text("Unable to fetch news")

# more https://learn.adafruit.com/monochrome-oled-breakouts/circuitpython-usage




