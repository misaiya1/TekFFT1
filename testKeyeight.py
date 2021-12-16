#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import numpy as np
import pandas as pd
from scipy.fftpack import fft
from math import pi

import wx
import wx.xrc
import locale


CSV_Path = '1_1_17.csv'
print(type(CSV_Path))
print((CSV_Path))

f = open(CSV_Path)
f_csv2 = pd.read_csv(f, engine='python', nrows=200, header=None)
# temp = f_csv2.columns.values
[hang,lie] = f_csv2.shape
name = []
for i in range(lie):
    name.append(f_csv2.iloc[0, i])
print(name)

f = open(CSV_Path)
f_csv2 = pd.read_csv(f, engine='python', nrows=3000, header=1, dtype=float, error_bad_lines=False, warn_bad_lines=False)
f_csv2.columns=name
temp = f_csv2.columns.values
print(temp)


plt.plot(f_csv2["x-axis"], f_csv2["1"], label="CH1")

plt.legend(loc='upper right')
plt.xlabel('Time')

# ax = plt.gca()
# cursor = Cursor(ax, horizOn=False, vertOn=True, useblit=False, color='grey')
# plt.ylabel()
plt.title('CSV File Record Data')
plt.style.use('seaborn-paper')
plt.grid(True)
plt.tight_layout()
plt.show()