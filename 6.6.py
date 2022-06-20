import vpython as vp
import random
import winsound

lamda1=0.005            #decay constant
max=800.                #80.
time_max=500
seed=68111
number=nloop=max        #Initial value
graph1=vp.graph(title='Spontaneous Decay',xtitle='Time',ytitle='Number',xmin=0,xmax=500,ymin=0,ymax=900)  #90
decayfunc=vp.gcurve(color=vp.color.green)
for time in vp.arange(0,time_max+1):       #Time loop
    for atom in vp.arange(1,number+1):     #Decay loop
        decay=random.random()
        if (decay<lamda1):
            nloop=nloop-1               #A decay
            winsound.Beep(600,100)      #Sound Beep
    number=nloop
    decayfunc.plot(pos=(time,number))
    vp.rate(30)
    
    
    