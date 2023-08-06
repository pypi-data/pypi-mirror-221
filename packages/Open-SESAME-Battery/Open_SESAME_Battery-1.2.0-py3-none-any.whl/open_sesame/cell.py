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


class Cell():

    def __init__(self, initial_SoC, initial_Temp, Initial_SoR, initial_SoH, initial_Capacity, lim_Mode, initial_Q):

        self.SoC = initial_SoC  #SoC of the battery gets updated in method CalSoC

        self.Temp = initial_Temp  #Temperature of the battery must be updated externaly
        self.SoR = Initial_SoR  #state of health of the Resistance must be updated externaly
        self.SoH = initial_SoH  #State of health of the battery (Capacity) must be updated externaly

        self.Vinst = 0  #Current Voltage at the Cellpoles
        self.act_Resistance = 0  #Resitance at current operating condition

        self.limCheckV = False  #Variable contains information if a Voltage limit is reached
        self.limCheckSoC = False  #Variable contains information if a SoC limit is reached

        self.Q = initial_Q  #electric Charge of battery in Ah
        self.Capacity = initial_Capacity  #Battery Capacity in kWh
        self.Q_ini = initial_Q  # initial electric charge of battery in Ah
        self.Capacity_ini = initial_Capacity  # initial battery charge in kWh

        self.deltaC = 0  #usable or used Energy of timestep
        self.updated_current = 0  #Current of the timestep

        self.act_Energy = self.SoC * self.Capacity
        self.act_Q = self.SoC * self.Q

        #behavior when a limit is reached
        #Mode1=reject requested Power
        #Mode2=calculate highest possible Current
        self.lim_Mode = lim_Mode

        if self.lim_Mode != 1 and self.lim_Mode != 2:
            self.lim_Mode = 2

        self.Crate = 0
        self.Power_upd = 0


#Check if the Voltage limites are reached under the current conditions
#Adjust or reject the requested Power

    def CheckV(self, Resistance, Power, OCVoltage, Vmax, Vmin):
        '''
        Inputs:
            -Resistance[Ohm], (Will be multiplied by the SoR)
            -Power [kW], requested Power from the aplication (positiv = charging, negativ =discharge) 
            -OCVoltage [V], Open circuit Voltage 
            -Vmax [V], maximum allowed Voltage of Cell
            -Vmin [V], minimal allowed Voltage of Cell 
        '''

        #Calculate the Crate

        if self.Capacity != 0:

            self.Crate = Power / self.Capacity

            #Calculate the Current
            self.updated_current = self.Crate * self.Q

            #Calculate the Resistance
            self.act_Resistance = self.SoR * Resistance

            #Voltage Calcultation
            self.Vinst = OCVoltage + (self.act_Resistance * self.updated_current)

        else:
            self.updated_current = 0
            self.Crate = 0

        self.limCheckV = False
        #Upper Limit Voltage Check
        if self.Vinst > Vmax:

            self.limCheckV = True
            limitside = 2

        #Lower Limit Voltage Check
        if self.Vinst < Vmin:

            self.limCheckV = True
            limitside = 1

        #Update Current
        if self.limCheckV == True:
            #Mode1
            if self.lim_Mode == 1:

                self.updated_current = 0
                self.Vinst = OCVoltage

            #Mode 2
            if self.lim_Mode == 2:

                #discharge mode
                if limitside == 1:
                    self.updated_current = (Vmin - OCVoltage) / self.act_Resistance
                    self.Vinst = Vmin

                #Charge mode
                if limitside == 2:
                    self.updated_current = (Vmax - OCVoltage) / self.act_Resistance
                    self.Vinst = Vmax
        else:
            #Update Current
            self.updated_current = self.updated_current

        #Crate update

        if self.Capacity != 0:
            self.Crate = self.updated_current / self.Q
            self.Power_upd = self.Crate * self.Capacity

        else:
            self.Crate = 0
            self.Power_upd = 0

        return

    def CalSoC(self, Power, deltaT, SoC_max, SoC_min):
        '''
        Inputs:
            -Power [kW], requested Power from the aplication (positiv = charging, negativ =discharge) 
            -deltaT [Sec], timestep between measurements 
        '''
        self.SoC_max = SoC_max
        self.SoC_min = SoC_min

        deltaT = deltaT / (60 * 60)  #in hours

        #Calculate the C-Rate
        self.Crate = Power / self.Capacity

        #Calculate the Power
        self.updated_current = self.Crate * self.Q

        #Energy of current step
        self.deltaC = self.updated_current * deltaT

        #Update SoC
        self.SoC = self.SoC + self.deltaC / self.Q

        #Obschon Q zur Berechnung der C-Rate verwendet wird, hat sie keinen Einfluss auf die Berechnung des neuen SoC.

        self.limCheckSoC = False

        #Check SoC boundries
        if self.SoC > self.SoC_max:

            self.limCheckSoC = True
            limitside = 1

        if self.SoC < self.SoC_min:
            limitside = 2
            self.limCheckSoC = True

        #Recalculation when SoC limits are reached
        if self.limCheckSoC == True:
            if self.lim_Mode == 1:

                #Reverse SoC calculation
                self.SoC = self.SoC - self.deltaC / self.Q
                self.Crate = 0
                self.updated_current = 0
                self.deltaC = 0
                self.deltaClost = 0

                self.Power_upd = self.Crate * self.Capacity

            if self.lim_Mode == 2:

                self.deltaSoC = 0
                #Charge Mode limit
                if limitside == 1:
                    #get old SoC
                    self.SoC = self.SoC - self.deltaC / self.Q
                    #delta SoC
                    self.deltaSoC = self.SoC_max - self.SoC
                    self.SoC = self.SoC_max

                #Discharge Mode limit
                if limitside == 2:
                    #get old SoC
                    self.SoC = self.SoC - self.deltaC / self.Q
                    #delta SoC
                    self.deltaSoC = self.SoC_min - self.SoC
                    self.SoC = self.SoC_min

                #Recalculate
                self.deltaC = self.deltaSoC * self.Q
                self.updated_current = self.deltaC / deltaT
                self.Crate = self.updated_current / self.Q

                self.Power_upd = self.Crate * self.Capacity

        self.aSoC = self.SoC * self.Capacity / self.Capacity_ini

        self.act_Energy = self.SoC * self.Capacity
        self.act_Q = self.SoC * self.Q

        return

    def update(self, delta_SoH, delta_SoR):
        '''
        Inputs
            -delta_SoH [0-1]
            -delta_SoR [0-1]
        
        '''

        self.SoH = self.SoH - delta_SoH

        self.SoR = self.SoR + delta_SoR

        if self.SoH <= 0:
            self.SoH = 0

        #Update the Energy and the Capcacity

        self.Capacity = self.Capacity_ini * self.SoH
        self.Q = self.Q_ini * self.SoH

        return
