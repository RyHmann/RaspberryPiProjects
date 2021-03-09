from picamera import PiCamera, Color
from time import sleep
from datetime import datetime

camera = PiCamera()

camera.annotate_text_size = 50


#For loop for 24 hours
#Take a picture every minute
    #Print the current time
    