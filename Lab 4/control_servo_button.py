import time
from adafruit_servokit import ServoKit
import qwiic_button 
import board
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
import colorsys
import numpy as np
from board import SCL, SDA
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import digitalio


# Setup board
# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
BORDER = 5


# Setup ripe and unripe avocado values

# day time ripe_rgb = np.array((73.39, 62.32, 38.75))
# day time unripe_rgb = np.array((81.79, 77.68, 52.32))
ripe_rgb = np.array((111.85, 74.02, 44.38))
unripe_rgb = np.array((152.68, 105.63, 64.29))

# Set up color board
#i2c = board.I2C()


apds = APDS9960(i2c)
apds.enable_color = True

# These constants control how much the sensor amplifies received light
APDS9660_AGAIN_1X = 0
APDS9660_AGAIN_4X = 1
APDS9660_AGAIN_16X = 2
APDS9660_AGAIN_64X = 3


# Set up button
my_button = qwiic_button.QwiicButton()    

# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
servo = kit.servo[2]

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
servo.set_pulse_width_range(500, 2500)

apds.color_gain = APDS9660_AGAIN_16X

# If button is pressed do below.

while True:   

        
    if my_button.is_button_pressed() == True:
            try:
                # wait for color data to be ready

                    # Set the servo to 180 degree position
                    servo.angle = 180
                    time.sleep(2)
                    while not apds.color_data_ready:
                        time.sleep(0.005) 
                    
                    # create some variables to store the color data in
                    # get the data and print the different channels
                    r1, g1, b1, c1 = apds.color_data
                    servo.angle = 0
                    time.sleep(2)
                    while not apds.color_data_ready:
                        time.sleep(0.005) 
                    r2, g2, b2, c2 = apds.color_data

                    r1, g1, b1 = [x /5.6 for x in [r1, g1, b1]]
                    print("The color channel first reading shows:\n")
                    print("red: ", r1)
                    print("green: ", g1)
                    print("blue: ", b1,"\n")

                    r2, g2, b2 = [x /5.6 for x in [r2, g2, b2]]
                    print("The color channel second reading shows:\n")
                    print("red: ", r2)
                    print("green: ", g2)
                    print("blue: ", b2,"\n")
                    #h, l, s = colorsys.rgb_to_hls(r, g, b)

                    # Get an average of these 2 values
                    first_reading = np.array([r1,g1,b1])
                    second_reading = np.array([r2,g2,b2])

                    avg = (first_reading + second_reading)/2
                    r = avg[0]
                    g = avg[1]
                    b = avg[2]

                    print("The color channel average reading shows:\n")
                    print("red: ", r)
                    print("green: ", g)
                    print("blue: ", b,"\n")

                    # Caluculate Eucledian distance
                    food_rgb = np.array((r,g,b))
                    ripe_dist = np.sqrt(np.sum(np.square(ripe_rgb-food_rgb)))
                    unripe_dist = np.sqrt(np.sum(np.square(unripe_rgb-food_rgb)))

                    # Clear display.
                    oled.fill(0)
                    oled.show()

                    font = ImageFont.load_default()
                    # Create blank image for drawing.
                    # Make sure to create image with mode '1' for 1-bit color.
                    image = Image.new("1", (oled.width, oled.height))
                    draw = ImageDraw.Draw(image)

                    # Draw a white background
                    draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)
                    # Draw a smaller inner rectangle
                    draw.rectangle(
                        (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
                        outline=0,
                        fill=0,
                    )


                    if ripe_dist > unripe_dist:
                        text1 = "Avocado unripe!"
                        text2 = "Wait 3 days"

                        print(text1)
                        # Write to the oled


                        # Draw Some Text
                        (font_width, font_height) = font.getsize(text1)
                        draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2),
                                text1, font=font, fill=255)

                        # Display image
                        oled.image(image)
                        oled.show()

                        # clear to show more details of what user should do instead
                        time.sleep(2)
                        # Clear display.
                        oled.fill(0)
                        oled.show()

                        font = ImageFont.load_default()
                        # Create blank image for drawing.
                        # Make sure to create image with mode '1' for 1-bit color.
                        image = Image.new("1", (oled.width, oled.height))
                        draw = ImageDraw.Draw(image)

                        # Draw a white background
                        draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)
                        # Draw a smaller inner rectangle
                        draw.rectangle(
                            (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
                            outline=0,
                            fill=0,
                        )
                        # Draw Some Text
                        (font_width, font_height) = font.getsize(text2)
                        draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2),
                                text2, font=font, fill=255)

                        # Display image
                        oled.image(image)
                        oled.show()
                        print(text2)
                    else:
                        #oled.text(0,1,"The avocado is ripe, eat quickly")  
                        print("The avocado is ripe, eat quickly")
                        text1 = "Avocado is ripe!"
                        text2 = "Eat quickly!"
                        print(text1)
                        # Write to the oled
                        # Draw Some Text
                        (font_width, font_height) = font.getsize(text1)
                        draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2),
                                text1, font=font, fill=255)

                        # Display image
                        oled.image(image)
                        oled.show()

                        # clear to show more details of what user should do instead
                        time.sleep(2)
                        # Clear display.
                        oled.fill(0)
                        oled.show()

                        font = ImageFont.load_default()
                        # Create blank image for drawing.
                        # Make sure to create image with mode '1' for 1-bit color.
                        image = Image.new("1", (oled.width, oled.height))
                        draw = ImageDraw.Draw(image)

                        # Draw a white background
                        draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)
                        # Draw a smaller inner rectangle
                        draw.rectangle(
                            (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
                            outline=0,
                            fill=0,
                        )
                        # Draw Some Text
                        (font_width, font_height) = font.getsize(text2)
                        draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2),
                                text2, font=font, fill=255)

                        # Display image
                        oled.image(image)
                        oled.show()
                        print(text2)

            except KeyboardInterrupt:
            # Once interrupted, set the servo back to 0 degree position
                servo.angle = 0
                time.sleep(0.5)
