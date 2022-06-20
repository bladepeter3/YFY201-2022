import vpython as vp
import numpy as np
import math as m
import random

def trjaxs():                                                                  #Plot axis for trajectories
    trax=vp.curve(pos=[vp.vector(-97,-100,0),vp.vector(100,-100,0)],color=vp.color.cyan,canvas=trajec)
    vp.curve(pos=[vp.vector(0,-100,0),vp.vector(0,100,0)],color=vp.color.cyan,canvas=trajec)
    vp.label(pos=vp.vector(0,-110,0),text='0',box=False,canvas=trajec)
    vp.label(pos=vp.vector(60,-110,0),text='x',box=False,canvas=trajec)

def wvfaxs():
    wvfax=vp.curve(pos=[vp.vector(-600,-155,0),vp.vector(800,-155,0)],canvas=wvgraph,color=vp.color.cyan)
    vp.curve(pos=[vp.vector(0,-150,0),vp.vector(0,400,0)],display=wvgraph,colo=vp.color.cyan)
    vp.label(pos=vp.vector(-80,450,0),text='Probability',box=False,canvas=wvgraph)
    vp.label(pos=vp.vector(600,-220,0),text='x',box=False,canvas=wvgraph)
    vp.label(pos=vp.vector(0,-220,0),text='0',box=False,canvas=wvgraph)
    
def energy(path):       #HO energy
    sums=0.
    for i in range(0,N-2):
        sums+=(path[i+1]-path[i])*(path[i+1]-path[i])
    sums+=path[i+1]*path[i+1];
    return sums

def plotpath(path):         #Plot trajectory in x-y scale
    for j in range(0,N):
        trplot.append(pos=vp.vector(20*path[j],2*j-100,0))

def plotwvf(prob):
    for i in range(0,100):
        wvplot.color=vp.color.yellow
        wvplot.append(pos=vp.vector(8*i-400,4.0*prob[i]-150,0))

N=101; M=101; xscale=10 #Initialize
path=np.zeros((M),float); prob=np.zeros((M),float)
trajec=vp.canvas(width=300,height=500,title='Spacetime trajectories')
trplot=vp.curve(color=vp.color.magenta,display=trajec,radius=0.8)

wvgraph=vp.canvas(x=340,y=150,width=500,height=300,title='Ground State Probability')
wvplot=vp.curve(x=range(0,100),canvas=wvgraph)      #Probability
wvfax=vp.curve(color=vp.color.cyan)

trjaxs()
wvfaxs()    #Plot axes
oldE=energy(path)   #find E of path

for i in range(0,1500):     #pick random element
    vp.rate(50)        #slows painting
    element=int(N*random.random()) #Metropolis algorithm
    change=2.0*(random.random()-0.5)
    path[element]+=change   #change path
    newE=energy(path)   #find new E
    if newE>oldE and m.exp(-newE+oldE)<=random.random():
        path[element]-=change       #Reject
        trplot.clear()  #Erase previous trajectory
        plotpath(path)
        trplot.visible=True     #Make visible new trajectory
    elem=int(path[element]*16+50)   #if path=0 , elem=50
    if elem<0:
        elem=0  #negative case not allowed
    if elem>100:
        elem=100    #if exceed max
    prob[elem]+=1   #increase probability for that x
    plotwvf(prob)   #plot prob
    oldE=newE
    print(i)