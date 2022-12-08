from Adafruit_GPIO import I2C
import smbus
from time import sleep
from MySQLHelper import insertAccelerometer, getConfig

tca = I2C.get_i2c_device(address=0x70)

# -------------
# Fungsi untuk ganti channel I2C
# -------------
def tcaSelect(channel):
    """Select an individual channel."""
    if channel > 7:
        return
    tca.writeRaw8(1 << channel)

# Init MPU
def mpuInit(bus, deviceAddress = 0x68):
    PWR_MGMT_1   = 0x6B
    SMPLRT_DIV   = 0x19
    CONFIG       = 0x1A
    GYRO_CONFIG  = 0x1B
    INT_ENABLE   = 0x38
    #write to sample rate register
    bus.write_byte_data(deviceAddress, SMPLRT_DIV, 7)
    #Write to power management register
    bus.write_byte_data(deviceAddress, PWR_MGMT_1, 1)
    #Write to Configuration register
    bus.write_byte_data(deviceAddress, CONFIG, 0)
    #Write to Gyro configuration register
    bus.write_byte_data(deviceAddress, GYRO_CONFIG, 24)
    #Write to interrupt enable register
    bus.write_byte_data(deviceAddress, INT_ENABLE, 1)


def readRawData(bus, addr, deviceAddress):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(deviceAddress, addr)
        low = bus.read_byte_data(deviceAddress, addr+1)
        #concatenate higher and lower value
        value = ((high << 8) | low)
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


# main
def main():
    while True:
        accelEnable = getConfig('accelerometer_record')
        if accelEnable == '1':
            for i in range(3):
                deviceId = i + 1
                tcaSelect(deviceId - 1)
                ACCEL_XOUT_H = 0x3B
                ACCEL_YOUT_H = 0x3D
                ACCEL_ZOUT_H = 0x3F
                GYRO_XOUT_H  = 0x43
                GYRO_YOUT_H  = 0x45
                GYRO_ZOUT_H  = 0x47
                # bus = smbus.SMBus(0) for older version boards
                bus = smbus.SMBus(1)
                mpuInit(bus)
                # MPU6050 device address	
                deviceAddress = 0x68
                #Read Accelerometer raw value
                acc_x = readRawData(bus, ACCEL_XOUT_H, deviceAddress)
                acc_y = readRawData(bus, ACCEL_YOUT_H, deviceAddress)
                acc_z = readRawData(bus, ACCEL_ZOUT_H, deviceAddress)
                #Read Gyroscope raw value
                gyro_x = readRawData(bus, GYRO_XOUT_H, deviceAddress)
                gyro_y = readRawData(bus, GYRO_YOUT_H, deviceAddress)
                gyro_z = readRawData(bus, GYRO_ZOUT_H, deviceAddress)
                #Full scale range +/- 250 degree/C as per sensitivity scale factor
                Ax = acc_x/16384.0
                Ay = acc_y/16384.0
                Az = acc_z/16384.0
                Gx = gyro_x/131.0
                Gy = gyro_y/131.0
                Gz = gyro_z/131.0
                # print('Az = %.5f' % Ax)
                print(deviceId)
                print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az)
                insertAccelerometer(deviceId, Ax, Ay, Az)
                bus.close()
                sleep(.1)
        else:
            print('Accel disabled')
            sleep(3)


