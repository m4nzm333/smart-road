from Accelerometer import main as accelerometerCapture
from Camera import main as cameraCapture
from multiprocessing import Process

try:
    # Function
    p1 = Process(target=accelerometerCapture)
    p2 = Process(target=cameraCapture)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
except KeyboardInterrupt:
    p1.terminate()
    p1.kill()