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

from math import cos, sin

import numpy as np
import pandas as pd

from .cyc_counting_algorithm import PeaktoPeak, Rainflow_mod


class degradation():
    '''
    Inputs: 
        -Cell chemistry object 
        timeresolution of input [Sec] 
        -selection of cycle counting algorithm [1/2]
    '''

    def __init__(self, Cell_chemistry_obj, timeresolution, cyc_counting_alg):

        self.timeresolution = timeresolution
        self.Chemistry_obj = Cell_chemistry_obj
        self.delta_SoH = 0
        self.delta_SoR = 0

        self.cyc_counting_alg = cyc_counting_alg

    #Appying cycle counting algorithm and calc stressfactors and delta SoR, SoH
    def compute(self, SoC_prof, Crate_prof, Temp_prof, startindex_fragment):
        '''
        Inputs:
            -SoC_prof    numpy series
            -Crate_prof  numpy series 
            -Temp_prof   numpy series 

        Outputs:
            -Cyc_Results Results of Cycle counting alg  pandas df
            Con_Results  Degradation results for every timestep  pandas df 
        '''

        #___________________________________________________________________________
        #Apply Cylce Counting algorithm

        if self.cyc_counting_alg == 1:
            Cycle_results = Rainflow_mod(SoC_prof, Crate_prof, Temp_prof)

        if self.cyc_counting_alg == 2:
            Cycle_results = PeaktoPeak(SoC_prof, Crate_prof, Temp_prof)

        if len(Cycle_results) == 1:
            #if Cycle_results[0,5]==0:

            Cycle_results[0, :] = 0

        Cycle_results = np.delete(Cycle_results, np.where((Cycle_results[:, 0] == 0))[0], axis=0)

        #___________________________________________________________________________
        #Create Result arrays

        leng = len(Cycle_results)
        deg_results = np.zeros((leng, 20))

        leng = len(SoC_prof)
        con_deg_results = np.zeros((leng, 10))

        #___________________________________________________________________________
        #Calc SF for every Cycle found
        for c in range(0, len(Cycle_results)):

            #Half/fullcycles
            cycle_equivalent = Cycle_results[c, 1] * Cycle_results[c, 0]  #changed!!!!!!!!!!!

            #--------------------------------------------
            # Cycle related stress factors (SF)

            #Get Cycle values
            DoD = Cycle_results[c, 0]
            Crate = Cycle_results[c, 5]

            AVG_Temp = Cycle_results[c, 7]
            AVG_SoC = Cycle_results[c, 4]

            #Check input
            AVG_Temp, AVG_SoC, DoD, Crate = self.Chemistry_obj.operational_range_check(AVG_Temp, AVG_SoC, DoD, Crate)

            #Compute Cyclic SoH Stressfactors
            SF_DoD = self.Chemistry_obj.Imp_CycDod(DoD)
            SF_Crate = self.Chemistry_obj.Imp_CycCrate(Crate)

            Imp_AVGSoC = self.Chemistry_obj.Imp_CycAvgSoc(AVG_SoC)
            Imp_Temp = self.Chemistry_obj.Imp_CycTemp(AVG_Temp)

            #Sum Stressfactors up SoH
            SF_cyclic_sum = SF_DoD * SF_Crate * Imp_AVGSoC * Imp_Temp * cycle_equivalent
            Tot_Soh_cyc = self.Chemistry_obj.refCyc * SF_cyclic_sum

            #--------------------------------------------
            #SoR related stress factors (SF)

            R_SF_Dod = self.Chemistry_obj.Imp_SorDoD(DoD)
            R_SF_Crate = self.Chemistry_obj.Imp_SorCrate(Crate)
            R_SF_AVGSoC = self.Chemistry_obj.Imp_SorAvgSoc(AVG_SoC)
            R_SF_Temp = self.Chemistry_obj.Imp_SorTemp(AVG_Temp)

            R_SoR_sum = R_SF_Dod * R_SF_Crate * R_SF_AVGSoC * R_SF_Temp * cycle_equivalent
            Tot_Sor_cycle = self.Chemistry_obj.refSor_cyc * R_SoR_sum

            #---------------------------------------------
            #Save SF results for each step

            deg_results[c, 0] = SF_DoD
            deg_results[c, 1] = SF_Crate
            deg_results[c, 2] = Imp_AVGSoC
            deg_results[c, 3] = Imp_Temp
            deg_results[c, 4] = SF_cyclic_sum
            deg_results[c, 5] = Tot_Soh_cyc

            deg_results[c, 6] = R_SF_Dod
            deg_results[c, 7] = R_SF_Crate
            deg_results[c, 8] = R_SF_AVGSoC
            deg_results[c, 9] = R_SF_Temp
            deg_results[c, 10] = R_SoR_sum
            deg_results[c, 11] = Tot_Sor_cycle

            deg_results[c, 12] = Cycle_results[c, 0]
            deg_results[c, 13] = Cycle_results[c, 1]
            deg_results[c, 14] = Cycle_results[c, 2]
            deg_results[c, 15] = Cycle_results[c, 3]
            deg_results[c, 16] = Cycle_results[c, 4]
            deg_results[c, 17] = Cycle_results[c, 5]
            deg_results[c, 18] = Cycle_results[c, 6]
            deg_results[c, 19] = Cycle_results[c, 7]

        #___________________________________________________________________________
        #Calendaric Degradation (for each timestamp)

        for x in range(0, len(SoC_prof)):

            #SoH Stressfactors
            SoC = SoC_prof[x]
            Temp = Temp_prof[x]

            #Check input
            Temp, SoC, DoD, Crate = self.Chemistry_obj.operational_range_check(Temp, SoC, 0, 0)

            SF_Cal_SoC = self.Chemistry_obj.Imp_CalSoC(SoC)
            SF_Cal_Temp = self.Chemistry_obj.Imp_CalTemp(Temp)

            #Total
            Tot_cal = SF_Cal_SoC * SF_Cal_Temp * self.Chemistry_obj.refCal * self.timeresolution

            #SoR Stressfactors

            R_SF_Cal_SoC = self.Chemistry_obj.Imp_SorCalSoC(SoC)

            R_SF_Cal_Temp = self.Chemistry_obj.Imp_SorCalTemp(Temp)

            R_Tot_cal = R_SF_Cal_SoC * R_SF_Cal_Temp * self.Chemistry_obj.refSor_cal * self.timeresolution

            #Save Results
            con_deg_results[x, 0] = SF_Cal_SoC
            con_deg_results[x, 1] = SF_Cal_Temp
            con_deg_results[x, 2] = Tot_cal

            con_deg_results[x, 7] = R_SF_Cal_SoC
            con_deg_results[x, 8] = R_SF_Cal_Temp
            con_deg_results[x, 9] = R_Tot_cal  #Total SoR Calendaric aging
            #___________________________________________________________________________
            #Adding cycle results to the continious results

            index = np.asarray(np.where(Cycle_results[:, 3] == x))
            first = index[0]

            if first.size > 0:
                index = int(first[0])
                con_deg_results[x, 3] = deg_results[index, 5]  #TOT_cyc SoH
                con_deg_results[x, 5] = deg_results[index, 11]  #TOT SoR Cyc

            else:
                con_deg_results[x, 3] = 0
                con_deg_results[x, 5] = 0  #Tot_SoR

        #Sum them together
        #SoH
        con_deg_results[:, 4] = con_deg_results[:, 3] + con_deg_results[:, 2]  #Sum Cal and Cyc aging
        #SoR
        con_deg_results[:, 6] = con_deg_results[:, 5] + con_deg_results[:, 9]  #SoR Sum of cal and Cyc Aging

        #___________________________________________________________________________
        #calculate delta SoH and delta_SoR of fragment

        self.delta_SoH = np.sum(con_deg_results[:, 4]) / 100
        self.delta_SoR = np.sum(con_deg_results[:, 6]) / 100

        #___________________________________________________________________________
        #preparing the result array for the output , change to pandas dataframe

        #Updating the Index of cycle Results according to the inputdata as a hole

        deg_results[:, 14] = deg_results[:, 14] + int(startindex_fragment)
        deg_results[:, 15] = deg_results[:, 15] + int(startindex_fragment)

        return deg_results, con_deg_results
