#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import ADS1256
import RPi.GPIO as GPIO

import numpy as np

try:
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()

    data = []
    while(1):
        ADC_Value = ADC.ADS1256_GetAll()

        #adc0=ADC_Value[1]*5.0/0x7fffff
        adc1=ADC_Value[1]*5.0/0x7fffff
        adc2=ADC_Value[2]*5.0/0x7fffff
        adc3=ADC_Value[3]*5.0/0x7fffff
        data.append([adc1,adc2,adc3])
        #print(data)


        #print ("0 ADC = %lf"%(ADC_Value[0]*5.0/0x7fffff))
        #print ("1 ADC = %lf"%(ADC_Value[1]*5.0/0x7fffff))
        #print ("2 ADC = %lf"%(ADC_Value[2]*5.0/0x7fffff))
        #print ("3 ADC = %lf"%(ADC_Value[3]*5.0/0x7fffff))
        #print ("4 ADC = %lf"%(ADC_Value[4]*5.0/0x7fffff))
        #print ("5 ADC = %lf"%(ADC_Value[5]*5.0/0x7fffff))
        #print ("6 ADC = %lf"%(ADC_Value[6]*5.0/0x7fffff))
        #print ("7 ADC = %lf"%(ADC_Value[7]*5.0/0x7fffff))
        #print(len(data))
        #print ("\33[9A")

        
except :
    print("data len ",len(data))
    a = np.asarray( data )
    np.savetxt("data.csv", a, delimiter=",")
    with open('data.npy', 'wb') as f:
         np.save(f, a)

    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()
