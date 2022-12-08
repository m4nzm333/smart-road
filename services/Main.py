from Accelerometer import main as accelerometerCapture
from multiprocessing import Process

try:
    # Function
    p1 = Process(target=accelerometerCapture)
    p1.start()
    p1.join()
except KeyboardInterrupt:
    p1.terminate()
    p1.kill()