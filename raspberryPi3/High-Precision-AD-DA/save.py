import time
import ADS1256
import DAC8532
import RPi.GPIO as GPIO
import numpy as np

### go to /High-Precision-AD-DA-Board/RaspberryPI/AD-DA/python

try:
    ADC = ADS1256.ADS1256()
    DAC = DAC8532.DAC8532()
    ADC.ADS1256_init()

    DAC.DAC8532_Out_Voltage(0x30, 3)
    DAC.DAC8532_Out_Voltage(0x34, 3)

    data = []
    while(1):
        ADC_Value = ADC.ADS1256_GetAll()
        data.append([ADC_Value[0]*5.0/0x7fffff,time.time()])


except :
    GPIO.cleanup()
    data = np.array(data)
    with open('signal.npy', 'wb') as f:
          np.save(f, data)

    print ("\r\nProgram end     ")
    exit()

