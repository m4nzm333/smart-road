from cv2 import VideoCapture, imwrite
from time import sleep

cam_port = 0
cam = VideoCapture(cam_port)

while True:
    result, image = cam.read()
    if result:
        imwrite("GeeksForGeeks.png", image)

    else:
        print("No image detected. Please! try again")
    
    sleep(1)