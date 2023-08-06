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
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap, ListedColormap


#this class defines a simulation output object
class simulation_output():

    def __init__(self, Results, own_params):
        '''
        Inputs:
            -Result list 
        '''

        try:
            self.pref_results = Results[0]
            self.Cylces_results = Results[1]
            self.deg_results = Results[2]

            self.timeresultion = own_params.timeresolution

            #Last_array
            Last_array = self.pref_results[-1]

            tempo = self.pref_results[0]
            self.timesteps_it = len(tempo)

            #____________________________________________________________
            #SoH and SoR Resultarray
            start_SoH = own_params.initial_SoH
            start_SoR = own_params.initial_SoR

            length = len(self.pref_results)
            Results = np.zeros((length, 11))

            for x in range(1, length):

                #Open Array
                temp = self.pref_results[x - 1]

                Results[0, 0] = start_SoH
                Results[0, 1] = start_SoR
                Results[0, 6] = 0

                Results[x, 0] = temp.SoH.iloc[-1]
                Results[x, 1] = temp.SoR.iloc[-1]
                Results[x, 6] = temp.calculation_iteration.iloc[-1]

                temp = self.deg_results[x - 1]

                Results[0, 2] = start_SoH
                Results[0, 3] = start_SoH
                Results[0, 4] = start_SoH

                Results[0, 7] = start_SoR
                Results[0, 8] = start_SoR
                Results[0, 5] = start_SoR

                if x == 1:
                    delta_iteration = temp.calculation_iteration.iloc[-1]
                else:
                    delta_iteration = Results[x, 6] - Results[x - 1, 6]

                    if delta_iteration == 0:

                        delta_iteration = 1

                Results[x, 2] = Results[x - 1, 2] - (temp.SoH_ToT_Cyc.sum() / 100) * delta_iteration  #SoH_cyc
                Results[x, 3] = Results[x - 1, 3] - (temp.SoH_ToT_Cal.sum() / 100) * delta_iteration  #SoH_cal
                Results[x, 4] = Results[x - 1, 4] - (temp.SoH_ToT_Cal.sum() / 100 +
                                                     temp.SoH_ToT_Cyc.sum() / 100) * delta_iteration

                Results[x, 7] = Results[x - 1, 7] + temp.SoR_Tot_cal.sum() / 100 * delta_iteration  #SoH_cyc
                Results[x, 8] = Results[x - 1, 8] + temp.SoR_ToT_Cyc.sum() / 100 * delta_iteration  #SoH_cal
                Results[x, 5] = Results[x - 1, 5] + (temp.SoR_ToT_Cyc.sum() / 100 +
                                                     temp.SoR_Tot_cal.sum() / 100) * delta_iteration  #SoR

                Results[x, 9] = Results[x, 6] * self.timesteps_it * own_params.timeresolution / (60 * 60 * 24)
                Results[x, 10] = round(Results[x, 9] / 365, 2)

            #Save as PD Dataframe
            columns = [
                'SoH', 'SoR', 'SoH_cyc', 'SoH_cal', 'Tot_SoH', 'SoR_Tot', 'calculation_iteration', 'SoR_Cal', 'SoR_Cyc',
                'time_days', 'time_years'
            ]
            Results = pd.DataFrame(Results, columns=columns)

            self.Results = Results

            self.SoH_end = self.Results.Tot_SoH.iloc[-1]  #Last_array.SoH.iloc[-1]
            self.SoR_end = self.Results.SoR_Tot.iloc[-1]  #self.SoR_end=Last_array.SoR.iloc[-1]

        except Exception as e:
            print("failure on simulation output")
            print(e)  # Print out error

    #Plot SoC at three different times of the simulation (beginning, end , middle)
    def Plot_SoC(self, min_steps=0, max_steps=-1):
        try:
            First = self.pref_results[0]

            middlearray = len(self.pref_results)
            middle_index = round(middlearray / 2)

            Middle = self.pref_results[middle_index]

            Last = self.pref_results[-1]

            First_iteration = First.calculation_iteration.loc[0]
            Last_iteration = Last.calculation_iteration.loc[0]
            Middle_iteration = Middle.calculation_iteration.loc[0]

            fig1, axs = plt.subplots()

            string = "iteration:" + str(Last_iteration)
            axs.plot(Last.SoC[min_steps:max_steps] * 100, label=string)

            string = "iteration:" + str(Middle_iteration)
            axs.plot(Middle.SoC[min_steps:max_steps] * 100, label=string)

            string = "iteration:" + str(First_iteration)
            axs.plot(First.SoC[min_steps:max_steps] * 100, label=string)

            axs.set_ylabel('SoC[%]')
            axs.set_xlabel('timestep')
            axs.grid(True)

            plt.legend()
            plt.show()

        except Exception as e:
            print("failure on Plot_SoC")
            print(e)  # Print out error

    #Heatmap
    def SoC_heatmap_plt(self):
        M = []
        m = []
        finSoC = []
        f = []
        iter = []
        grp = int(3600 / self.timeresultion)
        daysPerIter = len(self.pref_results[0]) / (86400 / self.timeresultion)
        day_t = 0
        for i in range(len(self.pref_results)):
            day = 0
            while day < daysPerIter:
                iter.append(day_t + 1)
                n = 0
                while n < 24:
                    M.append(max(self.pref_results[i].SoC[day * 24 * grp + n * grp:day * 24 * grp + (n + 1) * grp]))
                    m.append(min(self.pref_results[i].SoC[day * 24 * grp + n * grp:day * 24 * grp + (n + 1) * grp]))
                    f.append(
                        max(
                            max(self.pref_results[i].limChekV[day * 24 * grp + n * grp:day * 24 * grp + (n + 1) * grp]),
                            max(self.pref_results[i].limCHeckSoC[day * 24 * grp + n * grp:day * 24 * grp +
                                                                 (n + 1) * grp])))
                    n = n + 1
                day = day + 1
                day_t = day_t + 1
        for i in range(len(M)):
            if f[i] != 0:
                finSoC.append(-1)
                continue
            if m[i] < (1 - M[i]):
                finSoC.append(m[i] * 100)
            else:
                finSoC.append(M[i] * 100)

        finSoC = np.array(finSoC).reshape(len(self.pref_results), 24)
        finSoC = pd.DataFrame(finSoC.T, columns=iter)
        plt.figure()

        colors = ["red", "lawngreen", "red"]
        cmap = LinearSegmentedColormap.from_list("mycmap", colors)

        newcolors = cmap(np.linspace(0, 1, 256))
        black = np.array([0 / 256, 0 / 256, 0 / 256, 1])
        newcolors[:4, :] = black
        newcmp = ListedColormap(newcolors)

        ax = sns.heatmap(finSoC,
                         vmin=-2,
                         vmax=100,
                         xticklabels=10,
                         yticklabels=np.array(range(1, 25)),
                         cmap=newcmp,
                         center=50,
                         cbar_kws={'label': 'SoC (%)'})
        ax.set(title='SoC heatmap', xlabel='Days', ylabel='Hour')

        return

    def Plot_SoH(self, Mode):
        '''
        Mode 1 = x axis reperesents the iteration nr.
        Mode 2 = x axis reperesents the days simulated 
        Mode 3 = x axis reperesents the years simulated
        '''
        try:
            Res = self.Results

            if Mode == 1:
                x_axis_str = 'iterations #'
                x_value = Res.calculation_iteration

            if Mode == 2:
                x_axis_str = 'time [days]'
                x_value = Res.time_days

            if Mode == 3:
                x_axis_str = 'time [years]'
                x_value = Res.time_years
            else:
                print("Not a valid Print mode choosed")

            fig1, axs = plt.subplots(2, 1, sharex=True)
            fig1.tight_layout()
            fig1.subplots_adjust(hspace=0.08)

            axs[0].plot(x_value, Res.Tot_SoH * 100, 'ro-', label="Total SoH")
            axs[0].plot(x_value, Res.SoH_cyc * 100, '--o', alpha=0.5, label="SoH Cyclic")
            axs[0].plot(x_value, Res.SoH_cal * 100, '--o', alpha=0.5, label="SoH Calendaric")
            axs[0].legend()
            axs[0].ticklabel_format(useOffset=False)
            axs[0].set_ylabel('SoH [%]')
            axs[0].grid(True)

            axs[1].plot(x_value, Res.SoR_Tot * 100, 'ro-', label="Total SoR")
            axs[1].plot(x_value, Res.SoR_Cyc * 100, '--o', alpha=0.5, label="SoR Cyclic")
            axs[1].plot(x_value, Res.SoR_Cal * 100, '--o', alpha=0.5, label="SoR Calendaric")
            axs[1].legend()
            axs[1].set_ylabel('SoR [%]')
            axs[1].ticklabel_format(useOffset=False)
            axs[1].set_xlabel(x_axis_str)
            axs[1].grid(True)

            plt.legend()
            plt.show()

        except Exception as e:
            print("failure on Plot_SoH")
            print(e)  # Print out error

    #Calculate the equivalent full cycles seen  by the simulation
    def EFC_calc(self):

        #From fisrt cycle
        temp_res = self.Cylces_results[0]

        DoD_temp = temp_res.CC_DoD.abs()
        DoD_temp = DoD_temp.sum() / 2
        EFC_beginn = DoD_temp

        #From last cycle
        last = len(self.Cylces_results)
        temp_res = self.Cylces_results[last - 1]

        DoD_temp = temp_res.CC_DoD.abs()
        DoD_temp = DoD_temp.sum() / 2
        EFC_end = DoD_temp

        #Get the average
        AVG_EFC = (EFC_beginn + EFC_end) / 2

        #Get the amount of iterations

        if AVG_EFC != 0:

            amount_iteration = temp_res.calculation_iteration[0]
            EFC_tot = AVG_EFC * amount_iteration

        else:
            AVG_EFC = 0
            EFC_tot = 0

        #AVG_EFC =per iteration
        #EFC_tot = Over the hole simulation
        return AVG_EFC, EFC_tot

    #Calculate the Energythreput of the battery
    def Energy_threwput(self, timestep, iteration_length_days):

        #get first and last iteration
        startarray = self.pref_results[0]
        endarray = self.pref_results[-1]

        #timestep in hours
        timestep_hours = timestep / (60 * 60)

        startarray['power_upd'].values[startarray['power_upd'].values > 0] = 0
        startarray.power_upd = startarray.power_upd.abs()
        #Get Energy sum in kWh
        E_sum_kWh_start = startarray.power_upd.sum() * timestep_hours / 1000

        endarray['power_upd'].values[endarray['power_upd'].values > 0] = 0
        endarray.power_upd = endarray.power_upd.abs()
        E_sum_kWh_end = endarray.power_upd.sum() * timestep_hours / 1000

        #Get average out of the two
        AVG_E_sum_kWh = (E_sum_kWh_start + E_sum_kWh_end) / 2
        self.AVG_E_sum_it = AVG_E_sum_kWh
        self.AVG_E_sum_day = AVG_E_sum_kWh / iteration_length_days

        return

    def cyc_histogram(self, cycle_nr, cyc_min_DoD):

        #cyc_min_DoD = devines the minimal DoD from which on  cycles are shown

        Cylce_res = self.Cylces_results[cycle_nr - 1]
        deg_res = self.deg_results[cycle_nr - 1]
        per_res = self.pref_results[cycle_nr - 1]

        #--------------------------------------------------------------------------------------
        plt_data = pd.DataFrame()

        plt_data["Charge C-Rate"] = Cylce_res.CC_AVG_Crate
        plt_data["Discharge C-Rate"] = Cylce_res.CC_AVG_Crate

        plt_data["Charge C-Rate"][Cylce_res["CC_AVG_Crate"] < 0] = pd.NA
        plt_data["Discharge C-Rate"][Cylce_res["CC_AVG_Crate"] > 0] = pd.NA

        plt_data["Charge C-Rate"][Cylce_res["CC_DoD"] < cyc_min_DoD] = pd.NA
        plt_data["Charge C-Rate"][Cylce_res["CC_DoD"] < cyc_min_DoD] = pd.NA

        plothight = 4
        plotwidth = 4

        fig, axes = plt.subplots(1, 2, figsize=(plotwidth, plothight), sharey=True)
        sns.histplot(ax=axes[0], data=plt_data["Discharge C-Rate"], bins=20, stat='count')
        axes[0].grid(True)

        sns.histplot(ax=axes[1], data=plt_data["Charge C-Rate"], bins=20, stat='count')
        axes[1].grid(True)
        plt.show()

        #--------------------------------------------------------------------------------------
        plt_data = pd.DataFrame()

        plt_data["DoD"] = Cylce_res.CC_DoD
        plt_data["DoD"][Cylce_res["CC_DoD"] < cyc_min_DoD] = pd.NA
        plt_data["DoD"] = plt_data["DoD"] * 100

        fig, axes = plt.subplots(figsize=(plotwidth, plothight), sharey=True)
        sns.histplot(ax=axes, data=plt_data["DoD"], bins=20, stat='count')
        axes.grid(True)
        plt.show()

        #--------------------------------------------------------------------------------------
        plt_data = pd.DataFrame()

        plt_data["AVG Temp"] = Cylce_res.CC_AVG_Temp
        plt_data["AVG Temp"][Cylce_res["CC_DoD"] < cyc_min_DoD] = pd.NA

        fig, axes = plt.subplots(figsize=(plotwidth, plothight), sharey=True)
        sns.histplot(ax=axes, data=plt_data["AVG Temp"], bins=20, stat='count')
        axes.grid(True)
        plt.show()

        #--------------------------------------------------------------------------------------
        plt_data = pd.DataFrame()

        plt_data["AVG SoC"] = Cylce_res.CC_AVG_SoC
        plt_data["AVG SoC"][Cylce_res["CC_DoD"] < cyc_min_DoD] = pd.NA
        plt_data["AVG SoC"] = plt_data["AVG SoC"] * 100

        fig, axes = plt.subplots(figsize=(plotwidth, plothight), sharey=True)
        sns.histplot(ax=axes, data=plt_data["AVG SoC"], bins=20, stat='count')
        axes.grid(True)
        plt.show()

        return

    def joint_plot(self, cycle_nr, cyc_min_DoD):

        Cylce_res = self.Cylces_results[cycle_nr - 1]

        plt_data = pd.DataFrame()

        plt_data["C-Rate"] = Cylce_res.CC_AVG_Crate
        plt_data["C-Rate"][Cylce_res["CC_DoD"] < cyc_min_DoD] = pd.NA

        plt_data["DoD"] = Cylce_res.CC_DoD
        plt_data["DoD"][Cylce_res["CC_DoD"] < cyc_min_DoD] = pd.NA
        plt_data["DoD"] = plt_data["DoD"] * 100

        a_data = plt_data

        #--------------------------------------------------------------------------------------

        Cylce_res = self.Cylces_results[cycle_nr - 1]

        plt_data = pd.DataFrame()

        plt_data["Temp"] = Cylce_res.CC_AVG_Temp
        plt_data["Temp"][Cylce_res["CC_DoD"] < cyc_min_DoD] = pd.NA

        plt_data["DoD"] = Cylce_res.CC_DoD
        plt_data["DoD"][Cylce_res["CC_DoD"] < cyc_min_DoD] = pd.NA
        plt_data["DoD"] = plt_data["DoD"] * 100

        b_data = plt_data

        ax = sns.jointplot(data=b_data,
                           x="DoD",
                           y="Temp",
                           height=5,
                           ratio=2,
                           marginal_ticks=True,
                           dropna=True,
                           xlim=(0, 100))
        plt.show()

        ax = sns.jointplot(data=a_data,
                           x="DoD",
                           y="C-Rate",
                           height=5,
                           ratio=2,
                           marginal_ticks=True,
                           dropna=True,
                           xlim=(0, 100))
        plt.show()

        #--------------------------------------------------------------------------------------

        Cylce_res = self.Cylces_results[cycle_nr - 1]

        plt_data = pd.DataFrame()

        plt_data["Temp"] = Cylce_res.CC_AVG_Temp
        plt_data["Temp"][Cylce_res["CC_DoD"] < cyc_min_DoD] = pd.NA

        plt_data["DoD"] = Cylce_res.CC_DoD
        plt_data["DoD"][Cylce_res["CC_DoD"] < cyc_min_DoD] = pd.NA
        plt_data["DoD"] = plt_data["DoD"] * 100

        b_data = plt_data

        ax = sns.jointplot(data=b_data,
                           x="DoD",
                           y="Temp",
                           height=5,
                           ratio=2,
                           marginal_ticks=True,
                           dropna=True,
                           xlim=(0, 100))
        plt.show()

        ax = sns.jointplot(data=a_data,
                           x="DoD",
                           y="C-Rate",
                           height=5,
                           ratio=2,
                           marginal_ticks=True,
                           dropna=True,
                           xlim=(0, 100))
        plt.show()

        #--------------------------------------------------------------------------------------
        per_res = self.pref_results[cycle_nr - 1]

        per_data = pd.DataFrame()
        per_data["SoC"] = per_res.SoC
        per_data["SoC"] = per_data["SoC"] * 100
        per_data["Temp"] = per_res.Bat_temp

        ax = sns.jointplot(data=per_data,
                           x="SoC",
                           y="Temp",
                           height=5,
                           ratio=2,
                           marginal_ticks=True,
                           dropna=True,
                           xlim=(0, 100),
                           kind="kde")
        plt.show()

        return

    def sf_analysis(self, cycle_nr):

        Cylce_res = self.Cylces_results[cycle_nr - 1]
        deg_res = self.deg_results[cycle_nr - 1]
        per_res = self.pref_results[cycle_nr - 1]

        plt_data = pd.DataFrame()

        plt_data["Cyc. Cha. C-Rate"] = Cylce_res.SF_Crate
        plt_data["Cyc. Dis. C-Rate"] = Cylce_res.SF_Crate

        plt_data["Cyc. Cha. C-Rate"][Cylce_res["CC_AVG_Crate"] < 0] = pd.NA
        plt_data["Cyc. Dis. C-Rate"][Cylce_res["CC_AVG_Crate"] > 0] = pd.NA

        plt_data["Cyc. DoD"] = Cylce_res.SF_DoD
        plt_data["Cyc. AVG_SoC"] = Cylce_res.SF_AVGSoC
        plt_data["Cyc. AVG-Temp"] = Cylce_res.SF_Temp

        cal_data = pd.DataFrame()
        cal_data["Cal. SoC"] = deg_res.SF_Cal_SoC
        cal_data["Cal. Temp"] = deg_res.SF_Cal_Temp

        per_data = pd.DataFrame()
        per_data["SoC"] = per_res.SoC
        per_data["Temp"] = per_res.Bat_temp

        data = pd.concat([cal_data, plt_data], axis=1)

        fig1, ax = plt.subplots(figsize=(16, 6))
        sns.boxplot(ax=ax, data=data, width=0.7, whis=[5, 95], showfliers=False, saturation=0.8)
        #ax.axhline(1, linestyle='--', color='r')
        ax.set_ylabel('Stressfaktor []')
        ax.grid(True)

        plt.show()

    def EoA_criteria(self):

        First_it = self.pref_results[0]

        max_SoC = First_it.SoC.max()
        min_SoC = First_it.SoC.min()

        delta_SoC = max_SoC - min_SoC

        EoA_C = delta_SoC

        return EoA_C

    def Per_plot(self, result_iteration):

        for u in range(0, len(self.pref_results)):

            search = self.pref_results[u]

            if search.calculation_iteration.iloc[-1] == result_iteration:
                first_temp = self.pref_results[u]
                break

        #columns = ['SoR','SoH','SoC','Crate','power_upd','OCV_voltage','V_Bat','I_Updated','Resistance','limChekV','limCHeckSoC','Bat_temp','power_sim_in','Act_Energy','Act_Q','Absout_SoC']

        plt.rc('font', size=18)
        plt.rcParams['axes.xmargin'] = 0

        fig1, axs = plt.subplots(3, 1, sharex=True)
        fig1.tight_layout()
        fig1.subplots_adjust(hspace=0.08)

        axs[0].plot(first_temp.SoC * 100)
        axs[0].ticklabel_format(useOffset=False)
        axs[0].set_ylabel('SoC[%]')
        axs[0].grid(True)

        axs[1].plot(first_temp.OCV_voltage, label="OCV")
        axs[1].plot(first_temp.V_Bat, label="V_Bat")
        axs[1].set_ylabel('Voltage')
        axs[1].ticklabel_format(useOffset=False)
        axs[1].grid(True)

        axs[2].plot(first_temp.power_upd, label="Power possible")
        axs[2].plot(first_temp.power_sim_in, label="Power requested")
        axs[2].set_ylabel('Power')
        axs[2].ticklabel_format(useOffset=False)
        axs[2].grid(True)

        fig1.set_size_inches(16, 6)
        fig1.align_ylabels(axs[:])

        plt.legend()
        plt.show()
