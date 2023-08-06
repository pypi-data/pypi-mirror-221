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

import numpy as np
#Libraries
import pandas as pd

from .cell import Cell
from .degradation_analysis import degradation
from .thermal_model import thermal_model


#simulation function:
#Inputs: data= data series of power_w and ambient_temperature_C, input_parameters
def simulation(data, input_parameter):

    #Predefine Lists for simulation Results
    Perf_Result_list = list()
    Cyc_Result_list = list()
    Deg_Result_list = list()

    #Simulation internal variables
    entry_break = 0  #Variable for stopping the while-loop
    act_repetition = 1  # repetition variable
    data.power_Wcop = data.power_W / 1000  #Up from here the simulation is calculating the Power in kW

    #_______________________________________________________________________________________________
    # Repeat Simulation until amount of iteration is reached
    while act_repetition <= input_parameter.iteration:

        #_______________________________________________________________________________________________
        # Building Class Objects
        if act_repetition == 1:

            #Degradation obj
            Bat_deg = degradation(input_parameter.Cell_chemistry_obj, input_parameter.timeresolution,
                                  input_parameter.cyc_count_alg)

            #Cell
            initial_Bat_temp = data.ambient_temperature_C[0]

            Cell_Obj = Cell(input_parameter.initial_SoC, initial_Bat_temp, input_parameter.initial_SoR,
                            input_parameter.initial_SoH, input_parameter.nominal_energy, input_parameter.lim_Mode,
                            Bat_deg.Chemistry_obj.Q)

            #Thermal Model
            thermal_mod = thermal_model(1, 2, 3, data.ambient_temperature_C[0])

        if Cell_Obj.SoH == 0:
            break

        #_______________________________________________________________________________________________
        #predefine output arrays

        Cyc_results = pd.DataFrame()
        deg_results = pd.DataFrame()
        performance_results = pd.DataFrame()

        #_______________________________________________________________________________________________
        #Predefine fractions of the inputdata

        inputdata_len = len(data.power_Wcop)
        amount_fractions = math.ceil(inputdata_len / input_parameter.fraction_size)
        start_index = 0

        #_______________________________________________________________________________________________
        # Looping threw fractions
        start_SoH = Cell_Obj.SoH
        start_SoR = Cell_Obj.SoR

        #Core Simulation for fractions
        for i in range(0, int(amount_fractions)):

            end_index = start_index + input_parameter.fraction_size

            #Check if end_index in range of input_data
            if end_index >= inputdata_len:
                end_index = inputdata_len

            #select straight from numpy input data
            fraction_power = data.power_Wcop[start_index:end_index]
            fraction_Tambient = data.ambient_temperature_C[start_index:end_index]

            index_cyc = start_index
            start_index = end_index

            #_______________________________________________________________________________________________
            #Performance Analysis
            temp_results_np = np.zeros((len(fraction_power), 16))  #Create temperorary result array

            #Core simulation for each fraction
            for x in range(0, len(fraction_power)):

                #Apply Temperature Model
                bat_temp = thermal_mod.cell_temp_calc(fraction_power[x], fraction_Tambient[x])

                #Get circuit parameters

                Resistance = Bat_deg.Chemistry_obj.RfromTempSoC(Cell_Obj.SoC, bat_temp)
                OCVoltage = Bat_deg.Chemistry_obj.OCVfromSoC(Cell_Obj.SoC)  #SoC value of the timestep before SoC 0-1
                Vmax = Bat_deg.Chemistry_obj.vMax
                Vmin = Bat_deg.Chemistry_obj.vMin

                #Check Voltage and SoC limits
                Cell_Obj.CheckV(Resistance, fraction_power[x], OCVoltage, Vmax, Vmin)

                Cell_Obj.CalSoC(Cell_Obj.Power_upd, input_parameter.timeresolution, input_parameter.SoC_max,
                                input_parameter.SoC_min)

                #save results of fragment
                temp_results_np[x] = [
                    Cell_Obj.SoR, Cell_Obj.SoH, Cell_Obj.SoC, Cell_Obj.Crate, Cell_Obj.Power_upd * 1000, OCVoltage,
                    Cell_Obj.Vinst, Cell_Obj.updated_current, Resistance, Cell_Obj.limCheckV, Cell_Obj.limCheckSoC,
                    bat_temp, fraction_power[x] * 1000, Cell_Obj.act_Energy * 1000, Cell_Obj.act_Q, Cell_Obj.aSoC
                ]

            #_______________________________________________________________________________________________
            #degradation Analysis
            Cyc_results_temp, deg_results_temp = Bat_deg.compute(temp_results_np[:, 2], temp_results_np[:, 3],
                                                                 fraction_Tambient[:], index_cyc)

            #_______________________________________________________________________________________________
            #Update SoH and SoR

            Cell_Obj.update(Bat_deg.delta_SoH, Bat_deg.delta_SoR)

            temp_results_np[:, 1] = Cell_Obj.SoH
            temp_results_np[:, 0] = Cell_Obj.SoR

            #_______________________________________________________________________________________________
            #Save Results of fraction  in numpy files

            if i == 0:
                Cyc_results = Cyc_results_temp
                deg_results = deg_results_temp
                performance_results = temp_results_np

            else:
                Cyc_results = np.concatenate((Cyc_results, Cyc_results_temp), axis=0)
                deg_results = np.concatenate((deg_results, deg_results_temp), axis=0)
                performance_results = np.concatenate((performance_results, temp_results_np), axis=0)

            if Cell_Obj.Capacity == 0:
                break

        #_______________________________________________________________________________________________
        #pass on key results to next repetition

        #delta SoH and SoR of the current repetition
        delta_SoH = start_SoH - Cell_Obj.SoH
        delta_SoR = Cell_Obj.SoR - start_SoR

        #keep simulated SoC for the next repetition or not
        if input_parameter.keep_rep_SoC == 0:
            Cell_Obj.SoC = input_parameter.initial_SoC

        #_______________________________________________________________________________________________

        #Save Results in pandas Dataframe
        columns = [
            'SF_DoD', 'SF_Crate', 'SF_AVGSoC', 'SF_Temp', 'SF_cyc_sum', 'Tot_SoH_cyc', 'R_SF_DoD', 'R_SF_Crate',
            'R_SF_AVGSoC', 'R_SF_Temp', 'R_SoR_Sum', 'Tot_SoR_cycle', 'CC_DoD', 'CC_Full_half_c', 'CC_startindex',
            'CC_endindex', 'CC_AVG_SoC', 'CC_AVG_Crate', 'CC_info', 'CC_AVG_Temp'
        ]
        Cyc_results = pd.DataFrame(Cyc_results, columns=columns)
        Cyc_results["calculation_iteration"] = act_repetition

        columns = [
            'SF_Cal_SoC', 'SF_Cal_Temp', 'SoH_ToT_Cal', 'SoH_ToT_Cyc', 'SoH_sum_degr', 'SoR_ToT_Cyc', 'SoR_sum_degr',
            'R_SF_Cal_SoC', 'R_SF_Cal_Temp', 'SoR_Tot_cal'
        ]
        deg_results = pd.DataFrame(deg_results, columns=columns)
        deg_results["calculation_iteration"] = act_repetition

        columns = [
            'SoR', 'SoH', 'SoC', 'Crate', 'power_upd', 'OCV_voltage', 'V_Bat', 'I_Updated', 'Resistance', 'limChekV',
            'limCHeckSoC', 'Bat_temp', 'power_sim_in', 'Act_Energy', 'Act_Q', 'Absout_SoC'
        ]
        performance_results = pd.DataFrame(performance_results, columns=columns)
        performance_results["calculation_iteration"] = act_repetition

        #_______________________________________________________________________________________________
        #How to treat limits

        if performance_results.limCHeckSoC.sum() > input_parameter.limit_amount:

            print("!--------------------------------------")
            print("SoC limit has been reached in Iteration:", act_repetition)
            index = performance_results[performance_results.limCHeckSoC == True].first_valid_index()
            print("index of first occurence:", index)

            if input_parameter.limit_stop_simulation == 1:
                ("Simulation stopped because a limit was reached")
                break

        if performance_results.limChekV.sum() > input_parameter.limit_amount:

            print("!--------------------------------------")
            print("Voltage limit has been reached in Iteration:", act_repetition)
            index = performance_results[performance_results.limChekV == True].first_valid_index()
            print("index of first occurence:", index)

            if input_parameter.limit_stop_simulation == 1:
                ("Simulation stopped because a limit was reached")
                break

        #_______________________________________________________________________________________________
        #How to treat limits

        Perf_Result_list.append(performance_results)
        Cyc_Result_list.append(Cyc_results)
        Deg_Result_list.append(deg_results)

        #_______________________________________________________________________________________________
        #print out information for User
        '''
        print("---------------------------------------")
        print("Current iteration:", act_repetition,'/', input_parameter.iteration )
        print("Current Battery SoH:",round(performance_results.SoH.iloc[-1]*100,2),'%') 
        print("Current Battery SoR:",round(performance_results.SoR.iloc[-1],2),'[]')
        '''
        #_______________________________________________________________________________________________
        #Simulation controll

        #Passing on SoH if iterations are skipped
        if input_parameter.SoH_repeatsim != 0:

            #calc actual repetition
            nr_repetition = math.floor(input_parameter.SoH_repeatsim / delta_SoH)

            if nr_repetition == 0:
                nr_repetition = 1

            act_repetition_old = act_repetition
            act_repetition = act_repetition + nr_repetition

            #Handle the end of the simulation
            if act_repetition > input_parameter.iteration:

                if entry_break == 1:

                    break

                if entry_break == 0:

                    act_repetition = input_parameter.iteration
                    entry_break = entry_break + 1
                    nr_repetition = input_parameter.iteration - act_repetition_old

            #Update SOH and SoR
            #Cell_Obj.update(nr_rep_notrounded*delta_SoH,nr_rep_notrounded*delta_SoR)

            if nr_repetition > 1:
                factor_deg = nr_repetition - 1

            if nr_repetition <= 1:
                factor_deg = 0

            Cell_Obj.update(factor_deg * delta_SoH, factor_deg * delta_SoR)

        #Update repetition variable when there is no approx sim
        if input_parameter.SoH_repeatsim == 0:

            act_repetition = act_repetition + 1
            nr_repetition = 1

    #_______________________________________________________________________________________________
    #Genrate Output
    Output = [Perf_Result_list, Cyc_Result_list, Deg_Result_list]

    return Output
