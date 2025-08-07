import pandas as pd
import matplotlib as mpt
import numpy as np

file_name = 'responses.xlsx'

def convertAttendance(attendance):
    Quant_Attendance = np.array(attendance)
    for i in len(attendance):
        phrase = Quant_Attendance[i]
        if phrase == "Always":
            Quant_Attendance[i] = 5
        else if phrase == "Often":
            Quant_Attendance[i] = 4
        else if phrase == "Sometimes":
            Quant_Attendance = 3
        else if phrase == "Rarely":
            Quant_Attendance[i] = 2
        else:
            Quant_Attendance[i] = 1
    return Quant_Attendance


def convertHours(asdf):
    Quant_Hours = np.array(asdf)
    for i in len(attendance):
        phrase = Quant_Hours[i]
        if phrase == "0-4":
            Quant_Hours[i] = 2.5
        else if phrase == "5-8":
            Quant_Hours[i] = 6.5
        else if phrase == "9-12":
            Quant_Hours[i] = 10.5
        else if phrase == "13-16":
            Quant_Hours[i] = 14.5
        else if phrase == "17-20":
            Quant_Hours[i] = 18.5
        else:
            Quant_Hours[i] = 22.5
    return Quant_Hours


def StatFinder(asdf):
    for i in len(asdf):
        sum += asdf[i]
    mean = sum/len(asdf)
    sampleVar = 0
    for i in len(asdf):
        sampleVar += (asdf[i]-mean)*(asdf[i]-mean)
    sampleVar = sampleVar/(len(asdf)-1)
    return mean, sampleVar



    

