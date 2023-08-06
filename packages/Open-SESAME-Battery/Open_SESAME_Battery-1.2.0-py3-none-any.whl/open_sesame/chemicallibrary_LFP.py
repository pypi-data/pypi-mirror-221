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

import math
import os

import numpy as np
import pandas as pd

from .chemicallibrary import chemicallibrary


class chemicallibrary_LFP(chemicallibrary):

    def __init__(self):
        FILE_SOC_OCV = os.path.join(os.path.dirname(__file__),
                                    'LFP SoC-OCV.csv')  #make sure we find the file even if the module is imported

        self.v_ref = np.array(pd.read_csv(
            FILE_SOC_OCV, delimiter=';'))[:, 1]  # voltage values at different soc values from 0% to 100% SoC
        #self.r_ref = np.array(pd.read_csv('r-soc-temp (extensive,1Hz).csv', header=None))
        FILE_R_SOC_T = os.path.join(os.path.dirname(__file__), 'r-soc-temp (extensive,1Hz).csv')
        self.r_ref = np.array(pd.read_csv(FILE_R_SOC_T, header=None))

        self.vMax = self.v_ref[-1]
        self.vMin = self.v_ref[0]

        self.refCal = 0.0058212 / 86400  #[%SoH/s] @25 degr. 60%SoC
        self.refCyc = 0.004965  # [%SoR/EFC] @25 degr. and 60%DoD

        self.refSor_cyc = 0.00096  #[%SoR/s] @25 degr. 60%SoC
        self.refSor_cal = 0.02 / 86400  # [%SoR/EFC] @25 degr. and 60%DoD

        self.Q = 6

        self.max_Temp = 50
        self.min_Temp = -20

        self.maxSoC = 1
        self.minSoC = 0

        self.max_DOD = 1

        self.max_Crate = 10
        self.min_Crate = -10

        self.limitflag_temp = 0
        self.limitflag_SoC = 0
        self.limitflag_DoD = 0
        self.limitflag_Crate = 0

    def operational_range_check(self, Temp, SoC, DoD, Crate):

        #Temp check
        if Temp > self.max_Temp:
            Temp = self.max_Temp
            self.limitflag_temp = 1

        if Temp < self.min_Temp:
            Temp = self.min_Temp
            self.limitflag_temp = -1

        #SoC check
        if SoC > self.maxSoC:
            SoC = self.maxSoC
            self.limitflag_SoC = 1
        if SoC < self.minSoC:
            SoC = self.minSoC = 0
            self.limitflag_SoC = -1
        SoC = SoC

        #DoD check
        if DoD > self.max_DOD:
            DoD = self.max_DOD
            self.limitflag_DoD = 1
        if DoD < 0:
            DoD = 0
            self.limitflag_DoD = -1

        #Crate Check
        if Crate > self.max_Crate:
            Crate = self.max_Crate
            self.limitflag_Crate = 1

        if Crate < self.min_Crate:
            Crate = self.min_Crate
            self.limitflag_Crate = -1

        return Temp, SoC, DoD, Crate

    def OCVfromSoC(self, SoC):

        #SoC 0-100
        SoC = SoC * 100

        soc_ceil = math.ceil(SoC)
        soc_floor = math.floor(SoC)

        v_ceil = self.v_ref[soc_ceil]
        v_floor = self.v_ref[soc_floor]

        x = [soc_floor, soc_ceil]
        y = [v_floor, v_ceil]

        v_soc = np.interp(SoC, x, y)

        return v_soc

    def RfromTempSoC(self, SoC, temp):

        R0 = 0.0058

        R = 0.000026 * temp * temp - 0.001568 + R0

        return R


#############################################################################

#SoH Cal

    def Imp_CalSoC(self, SoC):
        #SoC 0-100
        SoC = SoC * 100
        imp = 0.007209 * SoC + 0.321183 + 0.2463
        return imp

    def Imp_CalTemp(self, temp):

        if temp < 20:
            temp = 20
        imp = 0.0231 * math.exp(0.1507 * temp)  #To proof very high
        return imp

    #SoH Cyc
    def Imp_CycAvgSoc(self, asoc):
        asoc = asoc * 100
        imp = 0.007364 * asoc + 0.600775

        return imp

    def Imp_CycTemp(self, temp):

        imp = 0.00145 * temp**2 - 0.064583 * temp + 1.671787

        return imp

    def Imp_CycDod(self, DoD):

        DoD = DoD * 100

        imp = 0.00004 * DoD * DoD + 0.0029 * DoD + 0.3483 + 0.3336
        return imp

    def Imp_CycCrate(self, crate):

        if crate > 0:  # charging

            imp = 0.222773 * math.exp(0.921456 * crate) + 0.7 - 0.09

        else:  # discharging
            crate = abs(crate)
            imp = 0.1112 * math.exp(0.75 * crate) + 0.85 - 0.09

        return imp

    #SoR cyclic stressfactors
    def Imp_SorAvgSoc(self, asoc):

        imp = 13.2802404 * asoc**2 - 14.0147110 * asoc + 4.6872954
        return imp

    def Imp_SorDoD(self, dod):

        dod = 100 * dod
        imp = 0.074210 * math.exp(0.026009 * dod) + 0.5

        return imp

    def Imp_SorCrate(self, crate):

        if crate > 0:  # charging
            #imp = 0.0035 * math.exp(5.5465 * crate)
            #Gemaess NEW charging C-reate 1-4  nominelle C-rate auf 0.7 gesetzt
            imp = 0.7 * math.exp(0.921456 * crate)
        else:
            # discharging
            crate = abs(crate)
            imp = 0.7 * math.exp(0.5152 * crate)

        return imp

    def Imp_SorTemp(self, Temp):
        imp = 0.7526 * math.exp(0.0114 * Temp)

        return imp

    #SoR cal stressfactors
    def Imp_SorCalSoC(self, SoC):

        SoC = SoC * 100
        imp = 1
        return imp

    def Imp_SorCalTemp(self, Temp):
        imp = 1
        return imp
