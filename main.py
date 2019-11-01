# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:45:36 2019

@author: LZQ
"""

import os
import numpy as np
import re
from cameras import Camera_Parameters
import matplotlib.pyplot as plt 

def read(path):
	
	
	def is_f(x):
		return x[0] == 'f'
	
	def is_v(x):
		if x[0] == 'v':
			if x[1] == ' ':
				return True
			return False
	
	open_file = open(path, 'r')
	read_file = open_file.readlines()
	
	list_f = filter(is_f, read_file)            
	list_v = filter(is_v, read_file)            
	
	obj_indices = []
	for n in list_f:
		obj_indices.append(list(x - 1 for x in map(int, re.split(r'[/\s]', n)[1:7:2])))
	obj_indices = np.array(obj_indices) 
	obj_num1 = np.array(obj_indices)   
	rows1=obj_num1.shape[0]
	new_array1 = np.zeros((rows1,1))
	for i in range(rows1):
		new_array1[i]=np.array([1])
	obj_indices=np.c_[obj_indices,new_array1]
		
	obj_vertex = []
	for n in list_v:
		obj_vertex.append(list(map(float, re.split(r'\s', n)[1:4])))
	obj_vertex = np.array(obj_vertex)
	obj_num2 = np.array(obj_vertex)   
	rows2=obj_num2.shape[0]
	new_array2 = np.zeros((rows2,1))
	for i in range(rows2):
		new_array2[i]=np.array([1])
	obj_vertex=np.c_[obj_vertex,new_array2]
	
	
	
	return obj_vertex, obj_indices

def getLukuo(v_uv):
    v_uv1=v_uv;
    v1_rows=np.shape(v_uv1)[0]
    v_rows=np.shape(v_uv)[0]
    temp=[]
    v_uv_M=[]
    u_uv_M=[]
    for i in range(v1_rows):
        for j in range(v_rows):
            if  v_uv[j,0]== v_uv1[i,0] and len(v_uv1) != 0:
                temp.append(v_uv[j,1])
               
        
        first_temp=np.shape(temp)[0];
        if first_temp !=0:
            v_min=min(temp)
            v_max=max(temp)
            v_uv_M.append([v_uv[i,0],v_min])
            v_uv_M.append([v_uv[i,0],v_max])
        del temp[:]
    #print(v_uv_M)        
    for i in range(v1_rows):
        for j in range(v_rows):
            if  v_uv[j,1]== v_uv1[i,1] and len(v_uv1) != 0:
                temp.append(v_uv[j,0])
               
        
        first_temp=np.shape(temp)[0];
        if first_temp !=0:
            v_min=min(temp)
            v_max=max(temp)
            u_uv_M.append([v_min,v_uv[i,1]])
            u_uv_M.append([v_max,v_uv[i,1],])
        del temp[:]
    v_uvs=[list(i) for i in set(tuple(j) for j in v_uv_M+u_uv_M)];
#    print(v_uvs)  
    return v_uvs






def main():
    source=os.getcwd()+'/'+'car1.obj';
    vertexs,indices=read(source);
    vertexs_num=np.array(vertexs);
    vertexs_rows=vertexs_num.shape[0];
    print(vertexs_rows)
    v_uv=np.zeros((vertexs_rows,3))
    for i in range(vertexs_rows):
        v_uv[i]=np.dot(Camera_Parameters,vertexs[i]);
        Zc=v_uv[i,2];
        v_uv[i,0]=int(1000*v_uv[i,0]/Zc+100);
        v_uv[i,1]=int(1000*v_uv[i,1]/Zc+200);
        v_uv[i,2]=v_uv[i,2]/Zc;
        
  
    v_uvs=getLukuo(v_uv)
    v_uvs_rows=np.shape(v_uvs)[0]
    
    print(np.shape(v_uv))
    print(np.shape(v_uvs))
    fname = open("E:/lzqData/3d/3dProjection/myLu_projection_match/cfw_python/v_uvs.txt",'w')
    for i in range(v_uvs_rows):
        for j in range(2):
            fname.write(str(v_uvs[i][j])+"   ")
        fname.write('\n')
    
      
#    print(v_uvs[:][1])  
    vus_array=np.array(v_uvs)
#    print(vus_array[:,0])
    plt.plot( vus_array[:,0],vus_array[:,1], '.', label='Data', color='black')
 
    plt.xlabel('u')
    plt.ylabel('v')
    plt.title('v_uvs')
    plt.legend()
    plt.show()
   
    
if __name__ == '__main__':
    main()
        

  




