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

import sys
from sys import exit

import pandas as pd

from .chemicallibrary import chemicallibrary
from .chemicallibrary_LFP import chemicallibrary_LFP
from .chemicallibrary_LTO import chemicallibrary_LTO
from .chemicallibrary_NMC import chemicallibrary_NMC

#input parameters
'''
Inputs:
    -Nominal Energy [Wh]
    -Cell_chemistry [object] 
    -timeresolution [Sec] of input data series 
    -iteration      [int+] amount of iterations 
    -initial_SoC    [0-1] SoC at beginning of the simulation 
    -SoC_max        [0-1] Upper SoC limit respected by the simulation 
    -SoC_min        [0-1] Lower SoC limit respected by the simulation 
    -SoH_repeatsim  [0-1] delta SoH that will be jumped before the simulation gets repeated 
    -fraction_size  [int+] amount of input_series gathered togehter before SoH gets updated 
    -cyc_count alg  [1,2] Choosing the cyc_count algorithem 1=Rainflow 2=Peak to Peak 
    -keep_rep_SoC   [0,1] Desides if the SoC at the end of the data series should be kept for the next repetition of the simulation or not
                            0 = calculate next repetition with initial SoC
                            1= keep the SoC calculated in the simulation before 
    

'''


def get_simulation_parameter(
        nominal_energy,
        Cell_chemistry_obj=chemicallibrary_NMC(),
        timeresolution=60,  #sec
        iteration=1000,  #Anzahl Berechnungen  
        initial_SoC=0.5,
        SoC_max=1,
        SoC_min=0,
        SoH_repeatsim=0.01,
        initial_SoR=1,
        initial_SoH=1,
        fraction_size=4000,
        lim_Mode=1,
        keep_rep_SoC=0,
        cyc_count_alg=1,
        limit_stop_sim=0,
        limit_amount_error=1):

    parameter = pd.DataFrame()

    #SoC related Parameters
    parameter.SoC_max = SoC_max
    parameter.SoC_min = SoC_min
    parameter.initial_SoC = initial_SoC

    #Battery related parameters
    parameter.Cell_chemistry_obj = Cell_chemistry_obj  #this is a chemical libaray object
    parameter.initial_SoR = initial_SoR
    parameter.initial_SoH = initial_SoH
    parameter.nominal_energy = nominal_energy  #Wh

    #Simulation Parameters
    parameter.timeresolution = timeresolution
    parameter.iteration = int(iteration)
    parameter.fraction_size = int(fraction_size)
    parameter.lim_Mode = lim_Mode  #select between one and two
    parameter.cyc_count_alg = cyc_count_alg  #1= Rainflow, 2=Peakt to Peak
    parameter.SoH_repeatsim = SoH_repeatsim
    parameter.keep_rep_SoC = keep_rep_SoC

    parameter.limit_stop_simulation = limit_stop_sim
    parameter.limit_amount = limit_amount_error

    #Battery size in kWh from Wh
    parameter.nominal_energy = parameter.nominal_energy / 1000

    #Input Parameter Check
    param_check = check_parameters(parameter)
    if param_check > 0:
        exit(0)

    return parameter


#Check the given input parameters
def check_parameters(param):
    flag = 0
    if not isinstance(param.Cell_chemistry_obj, chemicallibrary):
        print("ERROR: Cell chemistry object must be instance of class chemicallibrary")
        flag = flag + 1
    if param.timeresolution <= 0 or isinstance(param.timeresolution, float):
        print("ERROR: Time resolution is either <= 0 or is a float value. Please set an interger value greater than 0")
        flag = flag + 1
    if param.iteration < 0:
        print("ERROR: Repetitions are lesser than 0. Please set a value >= 0")
        flag = flag + 1
    if param.initial_SoC < 0 or param.SoC_max < 0 or param.SoC_min < 0 or param.initial_SoC > 1 or param.SoC_max > 1 or param.SoC_min > 1:
        print(
            "ERROR: One or more of inital SoC, SoC_max and SoC_min is either < 0 or > 1. Please set a value between and including 0 and 1"
        )
        flag = flag + 1
    if param.initial_SoC > param.SoC_max or param.initial_SoC < param.SoC_min or param.SoC_min > param.SoC_max:
        print(
            "ERROR: The SoC_min, initial_SoC and SoC_max are not in the correct order. Please check that the values are SoC_min <= initial_SoC <= SoC_max"
        )
        flag = flag + 1
    if param.initial_SoR < 1 or param.initial_SoH > 1:
        print(
            "ERROR: Either initial SoR < 1 or initial SoH > 1. Please ensure that initial SoR >= 1 and initial SoH <= 1"
        )
        flag = flag + 1
    if param.nominal_energy <= 0:
        print("ERROR: Value of nominal energy is <= 0. Please set a value > 0")
        flag = flag + 1
    if param.lim_Mode not in (1, 2):
        print("ERROR: lim_Mode has a value other than 1 or 2. Please ensure that the value is either 1 or 2")
        flag = flag + 1
    if param.cyc_count_alg not in (1, 2):
        print("ERROR: cyc_count_alg has a value other than 1 or 2. Please ensure that the value is either 1 or 2")
        flag = flag + 1
    if param.fraction_size <= 0:
        print("ERROR: Fraction size needs to be bigger than Zero")
        flag = flag + 1
    if param.keep_rep_SoC not in (0, 1):
        print("ERROR: Parameter keep-rep-SoC needs to be 0 or 1")
        flag = flag + 1
    if param.SoH_repeatsim >= 0.05:
        print(
            "ERROR: SoH_repeat_sim needs to be smaller than 0.05 (5%SoH)-Simulation jumps bigger than 5% SoH are leading to inacucrate results"
        )
        flag = flag + 1
    if param.SoH_repeatsim < 0:
        print("ERROR: SoH_repeat_sim can not be negativ")
        flag = flag + 1
    if flag > 0:
        print("Please make the above changes and run again")

    if param.limit_stop_simulation not in (0, 1):
        print("ERROR: Paramater limit_stop_sim must either be 0 or 1")
        flag = flag + 1

    if param.limit_amount < 1:
        print("ERROR: Paramater limit_amount must be bigger or equal 1")
        flag = flag + 1

    return flag
