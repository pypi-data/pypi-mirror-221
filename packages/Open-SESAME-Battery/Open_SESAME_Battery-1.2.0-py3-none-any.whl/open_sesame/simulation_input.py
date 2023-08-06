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
import pandas as pd


#this class defines a simulation input object
class simulation_input():

    def __init__(self):
        #set up some dummy arrays
        self.power_W = np.zeros(1)  #current vector in Amps. Charge current positive, discharge negative
        self.ambient_temperature_C = np.zeros(1)  #ambient temperature vector in °C

    #get data as pandas data frame with time vector as index
    def get_as_dataframe(self):
        data = {'power_W': self.power_W.tolist(), 'ambient_temperature_C': self.ambient_temperature_C.tolist()}
        df = pd.DataFrame(data)

        self.length_data = len(df)
        return df

    #overwrites internal numpy values with data from pandas dataframe, expects time as index
    def restore_from_dataframe(self, inputframe):
        self.power_W = np.array(inputframe['power_W'].tolist())
        self.ambient_temperature_C = np.array(inputframe['ambient_temperature_C'].tolist())

    #writes data to a csv file
    def write_csv(self, filename, separator=';'):
        df = self.get_as_dataframe()
        df.to_csv(filename, sep=separator)

    #reads data from a csv file
    def read_csv(self, filename, separator=';'):
        df = pd.read_csv(filename, sep=separator)

        self.length_data = len(df)
        self.restore_from_dataframe(df)

    #provides some statistical key values to check if the data correspond to the expectations
    def describe(self):
        df = self.Results.get_as_dataframe()
        return df.describe()
