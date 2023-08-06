"""
OPEN-SESAME

------------------------------------------------------------------------------
MIT License

 

Copyright (c) 2022

 

Author: BEYELER Marco (Bern University of Applied Science, https://www.bfh.ch)

Contributor: BHOIR Shubham Sharad (CSEM, https://www.csem.ch)

Contributor: BROENNIMANN Stefan (Bern University of Applied Science, https://www.bfh.ch)

Contributor: MOULLET Yoann (Bern University of Applied Science, https://www.bfh.ch)

 

Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal

in the Software without restriction, including without limitation the rights

to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:

 

The above copyright notice and this permission notice shall be included in all

copies or substantial portions of the Software.

 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

SOFTWARE.
------------------------------------------------------------------------------
"""

import matplotlib.pyplot as plt
import pandas as pd
from cell import Cell
from performance_analysis import performance_analysis

#Test function
result = pd.DataFrame()

result["SoC"] = [0.5]
result["SoR"] = [1]
result["SoH"] = [1]
result["Q"] = [10]
result["Capacity"] = [50]

path = '//bfhfilerbe01.bfh.ch/blm8/Documents/MT/Open_Sesame/develeopment/test_input2.csv'
data = pd.read_csv(path, delimiter=';')

lim_Mode = 2
SoC_max = 1
SoC_min = 0

temps = performance_analysis(data, result, SoC_max, SoC_min, lim_Mode)

result = temps

fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)
axs[0].plot(result["SoC"])
axs[0].set_ylabel('SoC')
axs[0].grid(True)

axs[1].scatter(result.index, result["C-Rate"])
axs[1].set_ylabel('C-Rate')
axs[1].grid(True)

axs[2].plot(result["Cell_Voltage"])
axs[2].set_ylabel('Cell_Voltage [V]')
axs[2].grid(True)

fig.tight_layout()

plt.show()
