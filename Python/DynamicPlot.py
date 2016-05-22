
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	pullData = ''
	with open('meusdados.txt', 'r+') as arq:
		with serial.Serial('/dev/ttyACM0',9600,timeout=1) as ser:
			arq.write(ser.readline())
		pullData = arq.read()
	dataArray = pullData.split('\n')
	xar = []
	yar = []
	for eachLine in dataArray:
		if len(eachLine)>1:
			x,y = eachLine.split(',')
			xar.append(int(x))
			yar.append(int(y))
	ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval = 100)
plt.show()


