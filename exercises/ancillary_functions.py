#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:00:37 2019
@author: Filip B. Maciejewski
@contact: filip.b.maciejewski@gmail.com
"""

import numpy as np
import pandas as pd
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute


def print_array(A):
    data_frame = pd.DataFrame(A).round(3)
    pd.set_option('precision', 3)
    print(data_frame)


def create_circuit_draft(qrs=1, crs=1, circuit_name='qc'):
    # qrs - quantum register size
    # circuit_name - name of the circuit

    # create quantum register
    qreg = QuantumRegister(qrs, name='qreg_' + circuit_name)
    # crete classical register
    creg = ClassicalRegister(crs, name='creg_' + circuit_name)
    # create quantum circuit
    circuit = QuantumCircuit(qreg, creg, name=circuit_name)

    return circuit, qreg, creg




nice_drawing_style = {
    'textcolor': '#000000',
    'gatetextcolor': '#000000',
    'subtextcolor': '#000000',
    'linecolor': '#000000',
    'creglinecolor': '#b9b9b9',
    'gatefacecolor': '#ffffff',
    'barrierfacecolor': '#bdbdbd',
    'backgroundcolor': '#ffffff',
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
    'cregbundle': True,
    'showindex': False}


def oracle(circuit, index=np.random.randint(0, 4)):
    qreg = circuit.qregs[0]
    if (index == 0):
        pass
    elif (index == 1):
        circuit.x(qreg[1])
    elif (index == 2):
        circuit.cx(qreg[0], qreg[1])
    elif (index == 3):
        circuit.x(qreg[0])
        circuit.cx(qreg[0], qreg[1])
    else:
        raise KeyError('Index too big')
    return circuit

# %%
