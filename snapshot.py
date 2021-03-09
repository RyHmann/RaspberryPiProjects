from picamera import PiCamera, Color
from time import sleep
from datetime import datetime


#Insantiate the camera
pi_cam = PiCamera()

#rotate due to mounting limitations
pi_cam.rotation = 90

#Take a photo each minute for 12 hours
for i in range(720):

    #put datetime on screen
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M")

    #format text
    pi_cam.annotate_text_size = 50
    pi_cam.annotate_text = formatted_time

    #sleep 60s
    sleep(60)

    #camera capture
    file_name_date_component = current_time.strftime("%H_%M")
    camera.capture('/home/pi/Desktop/snapshotpics/snap_' + file_name_date_component + '.jpg')

