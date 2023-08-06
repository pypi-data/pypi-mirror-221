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

from abc import ABC, abstractmethod
'''
Abstract class which shapes the chemicallibrary for all cell-chemistries
This class can not be changed 
Every function of this abstract class has to be implemented in the abstract methods as well

'''


class chemicallibrary(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def operational_range_check(self):
        pass

    #Performance related Functions
    @abstractmethod
    def OCVfromSoC(self):
        pass

    @abstractmethod
    def RfromTempSoC(self):
        pass

    #Calendaric Stressfactors SOH
    @abstractmethod
    def Imp_CalSoC(self):
        pass

    @abstractmethod
    def Imp_CalTemp(self):
        pass

    # Cyclic Stressfactors SOH
    @abstractmethod
    def Imp_CycAvgSoc(self):
        pass

    @abstractmethod
    def Imp_CycTemp(self):
        pass

    @abstractmethod
    def Imp_CycDod(self):
        pass

    @abstractmethod
    def Imp_CycCrate(self):
        pass

    #SoR Cyclic Stressfactors
    @abstractmethod
    def Imp_SorAvgSoc(self):
        pass

    @abstractmethod
    def Imp_SorDoD(self):
        pass

    @abstractmethod
    def Imp_SorCrate(self):
        pass

    @abstractmethod
    def Imp_SorTemp(self):
        pass

    #SoR Calendaric stressfactors
    @abstractmethod
    def Imp_SorCalSoC(self):
        pass

    @abstractmethod
    def Imp_SorCalTemp(self):
        pass
