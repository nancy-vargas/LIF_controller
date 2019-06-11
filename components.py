import serial
import time

class Laser():
	def __init__(self):
		self.dev_id = "/dev/ttyUSB0"
		self.ser = serial.Serial(self.dev_id, baudrate=19200,
			xonxoff=0, timeout=1)
	def delete(self):
		self.ser.close()
	def on(self):
		self.ser.write(b'SSSD 1\r\n')
	def off(self):
		self.ser.write(b'SSSD 0\r\n')

try:
	laser=Laser()
	laser.on()
	time.sleep(5)
	laser.off()
except Exception as e:
	print(e)
finally:
	try:
		laser.delete()
	except:
		pass