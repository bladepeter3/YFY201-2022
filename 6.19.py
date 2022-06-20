import vpython as vp
import numpy as np
import math as m

def potentials():
    for i in range(0,Nmax):
        xL=-18.0+i*dx                              
        V_L[i]=10*(xL+10)**2/2                     #left well left figure
        xR=2.0+i*dx
        V_R[i]=10*(xR-10)**2/2                     #right well left figure
    for j in range(0,Nmax+addi):
        xL=-18+j*dx                                #both wells of right figure
        if j<=125: V2[j]=10.*(xL+10)**2/2          #LHS
        if j>125 and j<325: V2[j]=V2[125]          #Pert lowers
        if j>=325: V2[j]=10.*(xL-10)**2/2          #RHS right side

def plotpotentials():
    for i in range(0,Nmax):
        cLx[i]=10*Xleft[i]+15;  cRx[i]=10*Xright[i]-15      #Widen
        cLy[i]=10*(Xleft[i]+10)**2/2-100; cRy[i]=10*(Xright[i]-10)**2/2-100  #BIG wide without perturbation wells
    for i in range(0,Nmax+addi):
        allcx[i]=8*Xall[i]          #for the BIG with perturbation well
        allcy[i]=V2[i]-100
    
def making_lists1():
    for i in range(0,Nmax):
        tempcL[i]=[cLx.tolist()[i],cLy.tolist()[i],cLz.tolist()[i]]
        tempcR[i]=[cRx.tolist()[i],cRy.tolist()[i],cRz.tolist()[i]]
        tempvl[i]=[Xleft.tolist()[i],V_L.tolist()[i],cRz.tolist()[i]]
        tempvr[i]=[Xright.tolist()[i],V_R.tolist()[i],cRz.tolist()[i]]
    for i in range(0,Nmax+addi):
        tempallc[i]=[allcx.tolist()[i],allcy.tolist()[i],allcz.tolist()[i]]
        tempvall[i]=[Xall.tolist()[i],V2.tolist()[i],allcz.tolist()[i]]
    
def making_lists2():
    for j in range(0,Nmax):
        tempvl2[j]=[cLx.tolist()[j],50*(RePsiL[j]**2+ImPsiL[j]**2)+150,cRz.tolist()[j]]  
        tempvr2[j]=[cRx.tolist()[j],50*(RePsiR[j]**2+ImPsiR[j]**2)+150,cRz.tolist()[j]]
    for j in range(0,Nmax+addi):
        tempvall2[j]=[allcx.tolist()[j],70*(RePsi2R[j]**2+Psi2R[j]**2)+150+50*(RePsi2L[j]**2+ImPsi2L[j]**2),allcz[j]]

dx = 0.08 ; dx2 = dx*dx ; 
k0=5.; dt = dx2/8 ; Nmax =200; addi=250
V_L=np.zeros((Nmax),float)
V_R=np.zeros((Nmax),float)
V2=np.zeros((Nmax+addi),float)
RePsiL=np.zeros((Nmax+1),float);ImPsiL=np.zeros((Nmax+1),float)
Rho=np.zeros((Nmax+1),float); RhoR=np.zeros((Nmax+1),float)
RePsiR=np.zeros((Nmax+1),float);ImPsiR=np.zeros((Nmax+1),float)
RePsi2L=np.zeros((Nmax+addi),float)
ImPsi2L=np.zeros((Nmax+addi),float)
RhoAL=np.zeros((Nmax+addi),float)
Rho2R=np.zeros((Nmax+addi),float)
RePsi2R=np.zeros((Nmax+addi),float)
Psi2R=np.zeros((Nmax+addi),float)
Xleft=vp.arange(-18.,-2.,dx)
cLx=np.zeros((Nmax),float)
cLy=np.zeros((Nmax),float)
cLz=np.zeros((Nmax),float)
Xright=vp.arange(2.0,18.,dx)
cRx=np.zeros((Nmax),float)
cRy=np.zeros((Nmax),float)
cRz=np.zeros((Nmax),float)
Xall=vp.arange(-18,18,dx)
allcx=np.zeros((Nmax+addi),float)
allcy=np.zeros((Nmax+addi),float)
allcz=np.zeros((Nmax+addi),float)

tempcL=np.zeros((Nmax),float).tolist();tempcR=np.zeros((Nmax),float).tolist()
tempvl=np.zeros((Nmax),float).tolist();tempvr=np.zeros((Nmax),float).tolist()
tempallc=np.zeros((Nmax+addi),float).tolist();tempvall=np.zeros((Nmax+addi),float).tolist()

potentials()
plotpotentials()
making_lists1()

g=vp.canvas(width=500,height=500,center=vp.vector(0,0,20));
cL=vp.curve(pos=tempcL,color=vp.color.red)
cR=vp.curve(pos=tempcR,color=vp.color.yellow)
vp.curve(pos=[vp.vector(0,250,0),vp.vector(0,-250,0)])                          #Vert line tru x=0
PlotObj=vp.curve(pos=tempvl,color=vp.color.red,radius=0.8)
PlotObjR=vp.curve(pos=tempvr,color=vp.color.yellow,radius=0.8)
escena2=vp.canvas(width=500,x=500);
allc=vp.curve(pos=tempallc,color=vp.color.green)
vp.curve(pos=[vp.vector(0,250,0),vp.vector(0,-250,0)])                          #vertical line tru x=0
PlotAllR=vp.curve(pos=tempvall,color=vp.color.cyan,radius=0.8,display=escena2)


for i in range(Nmax):
    RePsiL[i]=m.exp(-5*((Xleft[i]+10))**2)*m.cos(k0*Xleft[i])                 #Initial psi
    ImPsiL[i]=m.exp(-5*((Xleft[i]+10))**2)*m.sin(k0*Xleft[i])
    Rho[i]=RePsiL[i]*RePsiL[i]+ImPsiL[i]*ImPsiL[i]
    RePsiR[i]=m.exp(-5*((Xright[i]-10))**2)*m.cos(-k0*Xright[i])                #Just On side
    ImPsiR[i]=m.exp(-5*((Xright[i]-10))**2)*m.sin(-k0*Xright[i])
    RhoR[i]=RePsiR[i]**2+ImPsiR[i]**2
for i in range(0,450):                                                          #initial conditions
    x=-18+i*dx                                                                  #gives −18<=x<=18
    if i<=225:
            RePsi2L[i]=m.exp(-5*(x+10)**2)*m.cos(k0*x)                        #to middle
            ImPsi2L[i]=m.exp(-5*(x+10)**2)*m.sin(k0*x)
    else:                                                                       #too small set=0
        RePsi2L[i]=0.
        ImPsi2L[i]=0.
    RhoAL[i]=50.*(RePsi2L[i]**2+ImPsi2L[i]**2)                                  #Right psi
for j in range(0,450):
    x=-18+j*dx
    if j<=225:
        RePsi2R[j]=0.                                                           #too small , make it 0
        Psi2R[j]=0.
    else:
        RePsi2R[j]=m.exp(-5*(x-10)**2)*m.cos(-k0*x)                             #Left psi
        Psi2R[j]=m.exp(-5*(x-10)**2)*m.sin(-k0*x)
    Rho2R[j]=50.*(RePsi2R[j]**2+Psi2R[j]**2)
    
    
    
    tempvl2=np.zeros((Nmax),float).tolist()
    tempvr2=np.zeros((Nmax),float).tolist()
    tempvall2=np.zeros((Nmax+addi),float).tolist()

for t in range(0,10000):
    vp.rate(100)
    for i in range(1,Nmax):
        RePsiL[i]=RePsiL[i]-(dt/dx2)*(ImPsiL[i+1]+ImPsiL[i-1]-2*ImPsiL[i])+dt*V_L[i]*ImPsiL[i]
        ImPsiL[i]=ImPsiL[i]+(dt/dx2)*(RePsiL[i+1]+RePsiL[i-1]-2*RePsiL[i])-dt*V_L[i]*RePsiL[i]
        RePsiR[i]=RePsiR[i]-(dt/dx2)*(ImPsiR[i+1]+ImPsiR[i-1]-2*ImPsiR[i])+dt*V_R[i]*ImPsiR[i]
        ImPsiR[i]=ImPsiR[i]+(dt/dx2)*(RePsiR[i+1]+RePsiR[i-1]-2*RePsiR[i])-dt*V_R[i]*RePsiR[i]
        RePsi2L[i]=RePsi2L[i]-(dt/dx2)*(ImPsi2L[i+1]+ImPsi2L[i-1]-2*ImPsi2L[i])+dt*V2[i]*ImPsi2L[i]
        ImPsi2L[i]=ImPsi2L[i]+(dt/dx2)*(RePsi2L[i+1]+RePsi2L[i-1]-2*RePsi2L[i])-dt*V2[i]*RePsi2L[i]
        RePsi2R[i]=RePsi2R[i]-(dt/dx2)*(Psi2R[i+1]+Psi2R[i-1]-2*Psi2R[i])+dt*V2[i]*Psi2R[i]
        Psi2R[i]=Psi2R[i]+(dt/dx2)*(RePsi2R[i+1]+RePsi2R[i-1]-2*RePsi2R[i])-dt*V2[i]*RePsi2R[i]
        
    making_lists2()
        
    PlotObj=vp.curve(pos=tempvl2,color=vp.color.red,radius=0.8)
    PlotObjR=vp.curve(pos=tempvr2,color=vp.color.yellow,radius=0.8)
    PlotAllR=vp.curve(pos=tempvall2,color=vp.color.cyan,radius=0.8,display=escena2)
    print(t)

        









