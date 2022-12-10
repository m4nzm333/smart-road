from cv2 import VideoCapture, imwrite
from time import sleep
from datetime import datetime
from MySQLHelper import getConfig

def main():
    cam_port = 0
    cam = VideoCapture(cam_port)

    while True:
        accelEnable = getConfig('camera_record')
        if accelEnable == '1':
            result, image = cam.read()
            if result:
                imwrite(f"camera/{datetime.now().strftime('%Y%m%d%H%M%S%f')}.png", image)
            else:
                print("No image detected. Please! try again")
            sleep(.5)
        else:
            print('Camera disabled')
            sleep(3)