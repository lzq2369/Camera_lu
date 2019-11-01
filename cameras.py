# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:12:20 2019

@author: LZQ
"""
import math
import numpy as np

#相机参数
Phi=math.pi/4;
Psi=math.pi/4;
Theta=math.pi/4;
x0=0;
y0=0;
z0=10;
f=35e-3;
dx=0.026;
dy=0.026;
u0=0;
v0=0;

def rigbt(Phi, Psi, Theta, x0, y0, z0):
    R1=[[1,0,0],
        [0,math.cos(Phi),math.sin(Phi)],
        [0,-math.sin(Phi),math.cos(Phi)]];
    R2=[[math.cos(Psi),0,-math.sin(Psi)],
        [0,1,0],
        [math.sin(Psi),0,math.cos(Psi)]];
    R3=[[math.cos(Theta),math.sin(Theta),0],
        [-math.sin(Theta),math.cos(Theta),0],
        [0,0,1]];
    
    R31=np.dot(R3,R1);
    R=np.dot(R31,R2)
    R=np.array(R);
    T=[[x0],[y0],[z0]];
    R=np.c_[R,T]
#    print(R)
        
        
   
    RT1=[]
    RT1.append(R)
    RT1.append([[0,0,0,1]])
    
    RT = np.concatenate(RT1)
    
    return RT;



def proj(f):
    
    Projection_Matrix = [[f,0,0,0],[ 0,f,0,0],[ 0,0,1,0]];
    
    return Projection_Matrix;
    
    
def pixel(dx,dy,u0,v0):
    
    Pixel_Matrix = [[1/dx ,0 ,u0],[ 0 ,1/dy ,v0],[0 ,0 ,1]];
    
    return Pixel_Matrix;



Camera_Internal_Parameters = np.dot(pixel(dx,dy,u0,v0),proj(f));#相机内参数
#print(Camera_Internal_Parameters.shape)
#print(Camera_Internal_Parameters)


Camera_External_Parameters = rigbt(Phi, Psi, Theta, x0, y0, z0);#相机外参数
#print(Camera_External_Parameters)   

Camera_Parameters = np.dot(Camera_Internal_Parameters,Camera_External_Parameters); #相机参数

