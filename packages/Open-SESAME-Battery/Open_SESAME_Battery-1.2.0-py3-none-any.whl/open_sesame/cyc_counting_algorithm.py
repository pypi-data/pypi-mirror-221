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

import numpy as np
import rainflow
from scipy.signal import find_peaks as fp


def Rainflow_mod(signal, Crate, Temp):
    '''
    Return variables:
    
    column 0:Range of half-cycle
    column 1:Counting 1=full cycle 0=half cycle  
    column 2:index where cycle starts 
    column 3:index where cycle ends 
    column 4:Average SoC 
    column 5:Average C-Rate 
    column 6:Information if the halfcycles was built from a fullcycle 
    column 7:Average Temperature 
 
    '''
    #Result list
    rf_list = []

    #-----------------------------------------------------------------------------
    #Apply Rainflow algorithm
    for rng, mean, count, i_start, i_end in rainflow.extract_cycles(signal):

        rf_list.append([rng, count, i_start, i_end, mean, 0])

    #return empty array if now Cycles are found
    flag = not np.any(rf_list)
    if flag:
        rf_list2 = []
        rf_list2 = np.array(rf_list2)
        return
    #-----------------------------------------------------------------------------
    #Spliting fullcycles in two "unsymetric" half cycles

    rf_list = np.array(rf_list)

    rf_list2 = []

    for x in range(0, len(rf_list)):

        #Copy allready excisting half cycles
        if rf_list[x, 1] == 0.5:

            a = rf_list[x, 0]
            b = rf_list[x, 1]
            c = rf_list[x, 2]
            d = rf_list[x, 3]
            e = rf_list[x, 4]
            f = rf_list[x, 5]
            g = 0
            rf_list2.append([a, b, c, d, e, f, g])

        if rf_list[x, 1] == 1:

            start = int(rf_list[x, 2])
            end = int(rf_list[x, 3])

            y_start = signal[int(rf_list[x, 2])]
            y_end = signal[int(rf_list[x, 3])]

            #positive Cycle (starts with charging)
            if y_start > y_end:

                #First half cycle
                a = y_start - y_end
                b = 0.5
                c = rf_list[x, 2]
                d = rf_list[x, 3]
                mean_range = signal[start:end]
                e = np.mean(mean_range)
                f = rf_list[x, 5]
                g = 1
                rf_list2.append([a, b, c, d, e, f, g])

                #second half cycle
                #Create point
                y_point = y_end  #Copy Y form the end point

                #Searching closest rf point in order to take singal piece
                distmin1 = start - rf_list[:, 2]
                distmin2 = start - rf_list[:, 3]

                distmin1[distmin1 <= 0] = 10000000000000000000000000000  # A very large number
                distmin2[distmin2 <= 0] = 10000000000000000000000000000

                #min could be a start or an endpoint
                min1 = np.nanmin(distmin1)
                min2 = np.nanmin(distmin2)

                if min1 <= min2:
                    index_min = np.argmin(distmin1)
                    location = 2

                else:
                    index_min = np.argmin(distmin2)
                    location = 3

                #Reference point is the point found by RF before the cycle
                ref_point = int(rf_list[index_min, location])

                #Cut out signal point
                signal_piece = signal[ref_point:start]

                #Find nearest dicrete datapoint
                absolute_val_array = np.abs(signal_piece - y_point)
                smallest_difference_index = absolute_val_array.argmin()

                y_point = signal_piece[smallest_difference_index]

                x_point = ref_point + smallest_difference_index

                #Write Values in array
                a = y_start - y_point
                b = 0.5
                c = int(x_point)
                d = int(start)
                mean_range = signal[x_point:start]
                e = np.mean(mean_range)
                f = rf_list[x, 5]
                g = 1
                rf_list2.append([a, b, c, d, e, f, g])

            if y_start < y_end:

                #First half cycle
                a = y_end - y_start
                b = 0.5
                c = rf_list[x, 2]
                d = rf_list[x, 3]
                mean_range = signal[start:end]
                e = np.mean(mean_range)
                f = rf_list[x, 5]
                g = 1
                rf_list2.append([a, b, c, d, e, f, g])

                #second half cycle
                #Create point
                y_point = y_end  #Copy Y form the end point

                #Searching closest rf point in order to take singal piece
                distmin1 = start - rf_list[:, 2]
                distmin2 = start - rf_list[:, 3]

                distmin1[distmin1 <= 0] = 10000000000000000000000000000  # A very large number
                distmin2[distmin2 <= 0] = 10000000000000000000000000000

                #min could be a start or an endpoint
                min1 = np.nanmin(distmin1)
                min2 = np.nanmin(distmin2)

                if min1 <= min2:
                    index_min = np.argmin(distmin1)
                    location = 2

                else:
                    index_min = np.argmin(distmin2)
                    location = 3

                #Reference point is the point found by RF before the cycle
                ref_point = int(rf_list[index_min, location])

                #Cut out signal point
                signal_piece = signal[ref_point:start]

                #Find nearest dicrete datapoint
                absolute_val_array = np.abs(signal_piece - y_point)
                smallest_difference_index = absolute_val_array.argmin()

                y_point = signal_piece[smallest_difference_index]
                x_point = ref_point + smallest_difference_index

                #Write Values in array
                a = y_point - y_start
                b = 0.5
                c = int(x_point)
                d = int(start)
                mean_range = signal[x_point:start]
                e = np.mean(mean_range)
                f = rf_list[x, 5]
                g = 1
                rf_list2.append([a, b, c, d, e, f, g])

    #Save as numpy
    rf_list2 = np.array(rf_list2)
    z = np.zeros((len(rf_list2), 1))
    rf_list2 = np.append(rf_list2, z, axis=1)

    #-----------------------------------------------------------------------------
    #Defining Average C-Rate and Temp of each of Cycle
    for x in range(0, len(rf_list2)):

        start = int(rf_list2[x, 2])
        end = int(rf_list2[x, 3])
        index_ingorelist = []

        for y in range(0, len(rf_list2)):

            if x != y:
                start_check = rf_list2[y, 2]
                end_check = rf_list2[y, 3]

                if (start_check > start) and (end_check < end):

                    a = start_check
                    b = end_check
                    index_ingorelist.append([a, b])

        index_ingorelist = np.array(index_ingorelist)

        #Calc Crate of Cycle
        flag = not np.any(index_ingorelist)

        #If there are no cycles between start and end
        if flag:

            Crate_piece = Crate[start:end]
            #AVG_Crate=np.mean(Crate_piece)
            Crate_mod = Crate_piece

            Temp_piece = Temp[start:end]
            AVG_Temp = np.mean(Temp_piece)

            SoC_mod = signal[start:end]

        #If there are cycles in between
        else:

            Crate_mod = np.copy(Crate)
            Crate_mod = Crate_mod.astype(np.float)
            Crate_mod[0:start] = np.nan
            Crate_mod[end:len(Crate_mod)] = np.nan

            Temp_mod = np.copy(Temp)
            Temp_mod = Temp_mod.astype(np.float)
            Temp_mod[0:start] = np.nan
            Temp_mod[end:len(Temp_mod)] = np.nan

            SoC_mod = np.copy(signal)
            SoC_mod = SoC_mod.astype(np.float)
            SoC_mod[0:start] = np.nan
            SoC_mod[end:len(SoC_mod)] = np.nan

            for i in range(0, len(index_ingorelist)):

                #initialise NAn everywhere where there are fullcycles
                Crate_mod[int(index_ingorelist[i, 0]):int(index_ingorelist[i, 1])] = np.nan

                Temp_mod[int(index_ingorelist[i, 0]):int(index_ingorelist[i, 1])] = np.nan
                SoC_mod[int(index_ingorelist[i, 0]):int(index_ingorelist[i, 1])] = np.nan
        #Compute mean ignore nan and zeros

            AVG_Temp = np.nanmean(Temp)

        #Change Zeros to nan in order to ignore

        diff_SoC = np.diff(SoC_mod, n=1)
        diff_SoC = np.append(diff_SoC, 0)

        Crate_mod[diff_SoC == 0] = np.nan

        if Crate_mod != []:
            AVG_Crate = np.nanmean(Crate_mod)

        else:
            AVG_Crate = 0

        rf_list2[x, 7] = AVG_Temp
        rf_list2[x, 5] = AVG_Crate

    rf_list2[np.isnan(rf_list2)] = 0
    return rf_list2


def PeaktoPeak(signal, Crate, Temp):
    '''
    Return variables: 
    
    column 0:Range of half-cycle
    column 1:Counting 1=full cycle 0=half cycle  
    column 2:index where cycle starts 
    column 3:index where cycle ends 
    column 4:Average SoC 
    column 5:Average C-Rate 
    column 6:Information if the halfcycles was built from a fullcycle 
    column 7:Average Temperature 
 
    '''

    signal_pos = signal
    signal_neg = -1 * signal

    valleys = fp(signal_neg)[0]
    peaks = fp(signal_pos)[0]

    last_element = int(len(signal))
    #Add first and last index

    valleys = np.append(valleys, [0, last_element - 1])

    peakandvalleys = np.hstack((valleys, peaks))
    peakandvalleys.sort()

    rf_list = []

    for i in range(0, len(peakandvalleys) - 1):

        start = peakandvalleys[i]
        end = peakandvalleys[i + 1]

        signal_piece = signal[start:end]
        Crate_piece = Crate[start:end]
        Temp_piece = Temp[start:end]

        #Calc Cycle information
        AVG_SoC = np.mean(signal_piece)
        #AVG_Crate=np.mean(Crate_piece)
        AVG_Temp = np.mean(Temp_piece)

        #Calc AVG Crate a
        diff_SoC = np.diff(signal_piece, n=1)
        diff_SoC = np.append(diff_SoC, 0)
        Crate_piece[diff_SoC == 0] = np.nan
        AVG_Crate = np.nanmean(Crate_piece)

        dod = abs(signal[start] - signal[end])

        a = dod
        b = 0.5
        c = start
        d = end
        e = AVG_SoC
        f = AVG_Crate
        g = 0
        h = AVG_Temp

        rf_list.append([a, b, c, d, e, f, g, h])

    rf_list = np.array(rf_list)

    rf_list[np.isnan(rf_list)] = 0

    return rf_list
