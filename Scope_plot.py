# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 11:00:45 2016

@author: lkock
"""

import numpy as np
import matplotlib.pyplot as plt
from Tkinter import Tk
from tkFileDialog import askopenfilename


filename = askopenfilename(title="Select Antenna Data File")

data = np.loadtxt(filename,delimiter=',',usecols=range(0,2),skiprows=16)
plt.figure()
plt.subplot(211)
plt.plot(data[:,0],data[:,1])
grid()
ylabel("Voltage [V]")
xlabel("Time [sec]")
plt.subplot(212)
plt.psd(data[:,1],Fs=1/(data[1,0]-data[0,0]))
