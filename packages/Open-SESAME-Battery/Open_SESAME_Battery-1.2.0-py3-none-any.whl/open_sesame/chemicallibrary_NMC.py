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


class chemicallibrary_NMC(chemicallibrary):

    def __init__(self):
        FILE_SOC_OCV = os.path.join(os.path.dirname(__file__),
                                    'NMC SOC-OCV 2.csv')  #make sure we find the file even if the module is imported
        FILE_R_SOC_T = os.path.join(
            os.path.dirname(__file__),
            'r-soc-temp (extensive,1Hz).csv')  #make sure we find the file even if the module is imported

        self.v_ref = np.array(
            pd.read_csv(FILE_SOC_OCV))[:, 1]  # voltage values at different soc values from 0% to 100% SoC
        self.r_ref = np.array(pd.read_csv(FILE_R_SOC_T, header=None))
        self.vMax = self.v_ref[-1]
        self.vMin = self.v_ref[0]
        self.refCal = 0.006781 / 86400  #[%SoH/s] @25 degr. 60%SoC
        self.refCyc = 0.0053  # [%SoH/EFC] @25 degr. and 60%DoD

        self.refSor_cyc = 0.015 * 0.71  # [%SoR/EFC] @25 degr. and 60%DoD
        self.refSor_cal = 0.02 / 86400  #[%SoR/s] @25 degr. 60%SoC

        self.Q = 5

        self.max_Temp = 60
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

        socConsider = math.ceil(SoC * 100)
        return self.v_ref[socConsider]

    def RfromTempSoC(self, SoC, temp):

        if temp > 40:
            temp = 40

        if temp < -20:
            temp = -20

        socConsider = int(SoC * 100)
        tempConsider = int(temp - (-20))
        return self.r_ref[tempConsider, socConsider]

    #SoH Cal
    def Imp_CalSoC(self, soc):
        soc = soc * 100
        imp = 0.0077305 * soc + 0.2525478 + 0.3034
        return imp

    def Imp_CalTemp(self, temp):

        if temp < 15:  #Optimum Point
            temp = 15

        imp = 0.327751 * np.exp(0.055573 * temp) - 0.31
        return imp

    #SoH Cyc
    def Imp_CycAvgSoc(self, asoc):  #AvGSoC value between 0-100

        asoc = asoc * 100
        imp = 0.007364 * asoc + 0.600775

        return imp

    def Imp_CycTemp(self, temp):

        imp = 0.001585 * temp**2 - 0.064583 * temp + 1.631787

        return imp

    def Imp_CycDod(self, dod):
        dod = 100 * dod
        imp = 0.00011293 * dod**2 - 0.00436831 * dod + 0.9

        return imp

    def Imp_CycCrate(self, crate):

        if crate > 0:

            #imp = 0.222773 * math.exp(0.921456*crate)+0.7-0.09 #Original

            imp = 1.2 * crate * crate - 0.2 * crate + 0.8

        else:
            crate = abs(crate)
            #imp=0.1112*math.exp(0.9*crate)+0.85-0.12 #Original

            imp = 0.3 * crate * crate - 0.1 * crate + 0.8
        return imp

    #SoR cyclic stressfactors
    def Imp_SorAvgSoc(self, asoc):  #AvGSoC value between 0-100

        imp = 13.2802404 * asoc**2 - 14.0147110 * asoc + 4.6872954

        return imp

    def Imp_SorDoD(self, dod):
        #DoD 0-100
        dod = 100 * dod
        imp = 0.074210 * math.exp(0.026009 * dod) + 0.5

        return imp

    def Imp_SorCrate(self, crate):

        if crate > 0:  # charging
            imp = 0.5 * math.exp(0.815 * crate)  # stress factor for charging c-rate (sor increase)

        else:  # discharging OK
            imp = 0.5 * math.exp(0.51022509 * abs(crate))
        return imp

    def Imp_SorTemp(self, Temp):

        imp = 1  #Temp

        return imp

    #SoR cal stressfactors
    def Imp_SorCalSoC(self, SoC):
        SoC = SoC * 100
        imp = 1
        return imp

    def Imp_SorCalTemp(self, Temp):

        imp = 1
        return imp
