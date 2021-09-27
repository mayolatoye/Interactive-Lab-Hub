import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import pygame
pygame.mixer.init()

def playSound():
    pygame.mixer.music.load("./ding.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
emojiFont = ImageFont.truetype("NotoColorEmoji.ttf",size=109)
# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True


buttonA = digitalio.DigitalInOut(board.D23)
buttonA.switch_to_input()

buttonB = digitalio.DigitalInOut(board.D24)
buttonB.switch_to_input()

# EMOJI fonts https://www.raspberrypi.org/forums/viewtopic.php?t=253484

counter = 0 

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)


    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    currentTime = F'{time.strftime("%m/%d/%Y %H:%M:%S")}'
    if not buttonA.value :
        counter = counter + 1 


    if not buttonB.value :
        counter = 0 

    if counter < 2:
        symbol ="🔆" # start your day
        last_button_hit = counter
    elif counter < 4: 
        symbol = "🏋🏾‍♀️" # excercise time
    elif counter < 6: 
        symbol = "☕️" # coffee time
    elif counter < 8: 
        symbol = "🍕" # dinner time
    elif counter < 10: 
        symbol = "🛀🏼" # washtime 
    else:
        symbol = "🌜" # get ready for bed time 


    y = top
    draw.text((x, y),symbol, font=emojiFont, fill="#FFFFFF")
    draw.text((x, y), currentTime, font=font, fill="#FFFFFF")
    lineheight = font.getsize(currentTime)[1]
    y += lineheight
    draw.text((x, y), F"x {counter}", font=font, fill="#FFFFFF")
    draw.text((x, height - lineheight), f"->"*(counter%14), font=font, fill="#FF90FF")

    # Display image.
    disp.image(image, rotation)
    if counter in  [2,4,6,8,10]: 
        playSound()

    time.sleep(1)
