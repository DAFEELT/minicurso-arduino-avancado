import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ser = serial.Serial()

	
ser.port = '/dev/ttyACM0'
ser.baudrate = 9600
ser.timeout  = 1

ser.open()
ser.flushInput()
	
def animate(i):
	pullData = ser.readlines(45)
	xar = []
	yar = []
	for eachLine in pullData:
		if len(eachLine)>1:
			eachLine = eachLine[0:len(eachLine)-2]
			y = int(eachLine)
			xar.append(len(yar))
			yar.append(int(y))
	pullData = ser.readline()
	
	yar.append(int(pullData[0:len(pullData)-2]))
	xar.append(len(yar))
	
	if len(yar)>50:
		xar = []
		yar = []
	
	ax1.plot(xar,yar)
	

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()



