#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:00:37 2019
@author: Filip B. Maciejewski
@contact: filip.b.maciejewski@gmail.com
"""
import pandas as pd
import numpy as np
import pandas as pd
from math import pi
import cmath as c
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools import visualization
from qiskit.quantum_info import state_fidelity
from qiskit import BasicAer as Aer

import matplotlib.pyplot as plt


def print_array(A):
    data_frame = pd.DataFrame(A).round(3)
    pd.set_option('precision',3)
    print(data_frame)


def create_circuit_draft(qrs=1,crs=1, circuit_name='qc'):
    #qrs - quantum register size
    #circuit_name - name of the circuit

    #create quantum register
    qreg=QuantumRegister(qrs,name='qreg_'+circuit_name)
    #crete classical register
    creg=ClassicalRegister(crs,name='creg_'+circuit_name)
    #create quantum circuit
    circuit=QuantumCircuit(qreg,creg,name=circuit_name)
    
    return circuit,qreg,creg

#
# def SU2(theta,phi,lmbda):
#     arg00=-1j*(phi+lmbda)/2
#     x00=c.exp(arg00)
#
#     arg01=-1j*(phi-lmbda)/2
#     x01=-c.exp(arg01)
#
#     arg10=1j*(phi-lmbda)/2
#     x10=c.exp(arg10)
#
#     arg11=1j*(phi+lmbda)/2
#     x11=c.exp(arg11)
#
#     y0=c.cos(theta/2)
#     y1=c.sin(theta/2)
#
#     M=np.array([[x00*y0,x01*y1],[x10*y1,x11*y0]])
#
#
#     return M
#
#
# def create_rotation(theta,axis='x'):
#     if(axis=='x'):
#         return SU2(theta,-pi/2,pi/2)
#     elif(axis=='y'):
#         return SU2(theta,0,0)
#     elif(axis=='z'):
#         return SU2(0,0,theta)
#     else:
#         raise KeyError('wrong axis')
#
#
#
# def ket_to_state(ket):
#     #ketbra product
#     return np.outer(ket,np.conj(ket))
#
# def state_to_Bloch_vector(rho):
#     if(len(rho.shape)==1):
#         #shape normalization
#         rho=rho.reshape(2,1)
#     if(rho.shape[1]==1):
#         #if ket, go to state
#         rho0=ket_to_state(rho)
#         rho=rho0
#
#
#
#     #get bloch vector
#     x=np.real(rho[0,1]+rho[1,0])
#     y=np.real(1j*(rho[0,1]-rho[1,0]))
#     z=np.real(rho[0,0]-rho[1,1])
#     n=[x,y,z]
#
#
#     return n
#
#





nice_drawing_style={'comment': 'Style file for matplotlib_circuit_drawer (IBM QX Composer style)',
     'textcolor': '#000000',
     'gatetextcolor': '#000000',
     'subtextcolor': '#000000',
     'linecolor': '#000000',
     'creglinecolor': '#b9b9b9',
     'gatefacecolor': '#ffffff',
     'barrierfacecolor': '#bdbdbd',
     'backgroundcolor': '#ffffff',
     'fold': 50,
     'fontsize': 10,
     'subfontsize': 0.000001,
     'figwidth': -1,
     'dpi': 1200,
     'displaytext': {'id': 'QST',
      'u0': 'U_0',
      'u1': 'U_1',
      'u2': 'U_2',
      'u3': 'SU(2)',
      'x': 'X',
      'y': 'Y',
      'z': 'Z',
      'h': 'H',
      's': 'S',
      'sdg': 'S^\\dagger',
      't': 'T',
      'tdg': 'T^\\dagger',
      'rx': 'R_x',
      'ry': 'R_y',
      'rz': 'R_z',
      'reset': '\\left|0\\right\\rangle'},
     'displaycolor': {'id': '#ffca64',
      'u0': '#f69458',
      'u1': '#f69458',
      'u2': '#f69458',
      'u3': '#f69458',
      'x': '#a6ce38',
      'y': '#a6ce38',
      'z': '#a6ce38',
      'h': '#00bff2',
      's': '#00bff2',
      'sdg': '#00bff2',
      't': '#ff6666',
      'tdg': '#ff6666',
      'rx': '#ffca64',
      'ry': '#ffca64',
      'rz': '#ffca64',
      'reset': '#d7ddda',
      'target': '#00bff2',
      'meas': '#f070aa'},
     'latexdrawerstyle': False,
     'usepiformat': True,
     'cregbundle': True,
     'showindex': False,
     'compress': True}



def oracle(circuit,index=np.random.randint(0,4)):
    qreg=circuit.qregs[0]
    if (index==0):
        pass
    elif(index==1):
        circuit.x(qreg[1])
    elif(index==2):
        circuit.cx(qreg[0],qreg[1]) 
    elif(index==3):
        circuit.x(qreg[0])
        circuit.cx(qreg[0],qreg[1]) 
    else:
        raise KeyError('Index too big')
    return circuit





#%%
   





