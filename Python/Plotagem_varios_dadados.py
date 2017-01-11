import serial 
import numpy  
import matplotlib.pyplot as plt
from drawnow import *

ACx= []
ACy= []
ACz = []
Temperatura = []
Girx  = []
Giry = []
Girz = []

arduinoData = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
plt.ion() 											#avisando o matplot que quero fazer algo live
cnt=0

def makeFig(): 										#desenhadora
	plt.ylim(-25000,25000)
	plt.title('Dados do sensor')      				
	plt.grid(True)                                  
	plt.ylabel('Lido')                        	    #Set ylabels
	plt.plot(ACx, 'bo-', label='X')
	plt.legend(loc='upper left')    

	plt2=plt.twinx()                      #Criando um segundo eixo y
	plt2.plot(ACy, 'go-', label='Y')
	plt2.ticklabel_format(useOffset=False)
	plt2.legend(loc='upper right')
    
	plt3=plt.twinx()                      #Criando um terceiro eixo z
	plt3.plot(ACz, 'yo-', label='Z')
	plt3.ticklabel_format(useOffset=False)
	plt3.legend(loc='lower left')
	
	plt4=plt.twinx()
	plt4.plot(ACz, 'rx-', label='T')
	plt4.ticklabel_format(useOffset=False)
	plt4.legend(loc='center right')

while True: #Uhuuulllll
    while (arduinoData.inWaiting()==0):			 #espera ter dado pra ler
        pass
    arduinoString = arduinoData.readline()
    dataArray = arduinoString.split(',')
    
    if len(dataArray)>6: 
		ACx.append(float( dataArray[0])) 			#convertendo dados lidos e adicionando as listas
		ACy.append(float( dataArray[1]))
		ACz.append(float( dataArray[2]))
		Temperatura.append(float( dataArray[3]))
		Girx.append(float( dataArray[4]))
		Giry.append(float( dataArray[5]))
		Girz.append(float( dataArray[6]))
		
		print(dataArray)
		
		drawnow(makeFig)                      
		#plt.pause(0.0000001)                     
		cnt=cnt+1    								#contagem de pontos no grafico
    if(cnt>100):                            		#se tem mais de 50 apagar o mais antigo
    	ACx.pop(0)
        ACy.pop(0)
        ACz.pop(0)
        Temperatura.pop(0)
        Girx.pop(0)
        Giry.pop(0)
        Girz.pop(0)
        
        
