from Accelerometer import main as accelerometerCapture
from Camera import main as cameraCapture
from multiprocessing import Process
from WebServer import main as webServer

try:
    # Function
    p1 = Process(target=accelerometerCapture)
    p2 = Process(target=cameraCapture)
    p3 = Process(target=webServer)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
except KeyboardInterrupt:
    p1.terminate()
    p1.kill()
    p2.terminate()
    p2.kill()
    p3.terminate()
    p3.kill()