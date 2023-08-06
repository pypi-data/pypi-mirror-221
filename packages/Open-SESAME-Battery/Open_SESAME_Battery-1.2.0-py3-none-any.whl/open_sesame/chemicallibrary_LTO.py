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


class chemicallibrary_LTO(chemicallibrary):

    def __init__(self):
        FILE_SOC_OCV = os.path.join(os.path.dirname(__file__), 'LTO SoC-OCV.csv')
        self.v_ref = np.array(pd.read_csv(FILE_SOC_OCV))[:, 1]

        self.vMax = self.v_ref[-1]
        self.vMin = self.v_ref[0]

        self.refCal = 0.0024 / 86400  #[%SoH/s] @25 degr. 60%SoC
        self.refCyc = 0.002 * 0.625  # [%SoH/EFC] @25 degr. and 60%DoD

        self.refSor_cyc = 0.0001  # [%SoR/EFC] @25 degr. and 60%DoD
        self.refSor_cal = 0.038 / 86400  #[%/s] @25 degr. 60%SoC

        self.Q = 20

        self.max_Temp = 50
        self.min_Temp = -20

        self.maxSoC = 1
        self.minSoC = 0

        self.max_DOD = 1

        self.max_Crate = 20
        self.min_Crate = -8

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

        #Temperature independent function
        SoC = SoC * 100
        mOHm = 0.00001 * SoC * SoC - 0.0028 * SoC + 1.268
        Rout = mOHm / 1000

        return Rout

    #SoH Cal
    def Imp_CalSoC(self, SoC):
        #SoC 0-100
        SoC = SoC * 100

        imp = 0.0112 * SoC + 0.2368 + 0.0911

        return imp

    def Imp_CalTemp(self, temp):

        if temp < 15:
            temp = 15

        imp = 0.06371687 * math.exp(0.10018649 * temp) + 0.22

        return imp

    #SoH Cyc
    def Imp_CycAvgSoc(self, asoc):
        imp = 1
        return imp

    def Imp_CycTemp(self, temp):

        temp = abs(temp)
        imp = 0.26915027 * math.exp(0.04196425 * temp) + 0.23072
        return imp

    def Imp_CycDod(self, DoD):
        DoD = DoD * 100

        imp = 0.0248 * math.exp(0.0345 * DoD) + 0.21
        imp = 0.0248 * math.exp(0.0345 * DoD) + 0.21 + 0.6

        return imp

    def Imp_CycCrate(self, crate):

        if crate <= 0:
            imp = 0.0272 * crate * crate - 0.0286 * crate + 0.8514

        if crate >= 0:

            imp = 0.15 * math.exp(0.85 * crate) + 0.7 - 0.09

        return imp

    #SoR cyclic stressfactors
    def Imp_SorAvgSoc(self, asoc):
        imp = 1
        return imp

    def Imp_SorDoD(self, dod):
        imp = 1
        return imp

    def Imp_SorCrate(self, crate):
        imp = 1
        return imp

    def Imp_SorTemp(self, Temp):
        imp = 0.1595 * math.exp(0.0754 * Temp)
        return imp

    #SoR cal stressfactors
    def Imp_SorCalSoC(self, SoC):

        SoC = SoC * 100
        imp = 0.0025 * SoC + 0.45551 + 0.4

        return imp

    def Imp_SorCalTemp(self, Temp):

        imp = 0.157171 * math.exp(0.074408 * Temp)

        return imp
