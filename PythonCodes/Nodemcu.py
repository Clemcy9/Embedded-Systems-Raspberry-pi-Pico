import network
from time import sleep
wlan= network.WLAN(network.STA_IF)
wlan.active(True)
#print(dir(wlan.scan()))
#print(len(wlan.scan()))

                                                                                
def check_network(w=list(),k=0,v=list()):
    list1={}
    for de in range(0,len(w)):
        for value in w[de]:
            for x in v:
                if b'%s'%(x)==value:
                    #print(x)
                    #print(w[de][3])
                    list1[x]= w[de][3]
    return list1
def calculate_distance(Rssi,v,MeasuredPower=49, EnvironmentalFactor=2):
    for x in v:
        distance=10**((MeasuredPower-Rssi[x])/(10**EnvironmentalFactor))
        print("%s %s"%(x,distance)+"cm")
    
    
#print(check_network(w=wifinet, v=["Port1", "Port2"]))
while True:
    wifinet=wlan.scan()
    calculate_distance(v=["Port1", "Port2"], Rssi=check_network(w=wifinet, v=["Port1", "Port2"]) )
    sleep(1)