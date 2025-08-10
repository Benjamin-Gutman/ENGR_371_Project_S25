import pandas as pd
import matplotlib as mpt
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

file_name = 'responses2.xlsx'

def convertAttendance(attendance):
    Quant_Attendance = np.array(attendance)
    for i in range(len(attendance)):
        phrase = Quant_Attendance[i]
        if phrase == "Always":
            Quant_Attendance[i] = 5
        elif phrase == "Often":
            Quant_Attendance[i] = 4
        elif phrase == "Sometimes":
            Quant_Attendance[i] = 3
        elif phrase == "Rarely":
            Quant_Attendance[i] = 2
        else:
            Quant_Attendance[i] = 1
    return Quant_Attendance

def convertGpa(gpa):
    Quant_Gpa = np.array(gpa)
    for i in range(len(gpa)):
        phrase = Quant_Gpa[i]
        if phrase == "0-1.99":
            Quant_Gpa[i] = 0
        elif phrase == "2.0-2.29":
            Quant_Gpa[i] = 1
        elif phrase == "2.3-2.69":
            Quant_Gpa[i] = 2
        elif phrase == "2.7-2.99":
            Quant_Gpa[i] = 3
        elif phrase == "3.0-3.29":
            Quant_Gpa[i] = 4
        elif phrase == "3.3-3.69":
            Quant_Gpa[i] = 5
        elif phrase == "3.7-3.99":
            Quant_Gpa[i] = 6
        else:
            Quant_Gpa[i] = 7
    return Quant_Gpa


def convertHours(asdf):
    Quant_Hours = np.array(asdf)
    for i in range(len(asdf)):
        phrase = Quant_Hours[i]
        if phrase == "0-4":
            Quant_Hours[i] = 2.5
        elif phrase == "5-8":
            Quant_Hours[i] = 6.5
        elif phrase == "9-12":
            Quant_Hours[i] = 10.5
        elif phrase == "13-16":
            Quant_Hours[i] = 14.5
        elif phrase == "17-20":
            Quant_Hours[i] = 18.5
        else:
            Quant_Hours[i] = 22.5
    return Quant_Hours




def arraySeparator(array1, array2, limit):
    under1, over1, under2, over2 = [], [], [], []
    for i in range(len(array1)):
        if array1[i] < limit:
            under1.append(array1[i])
            under2.append(array2[i])
        else:
            over1.append(array1[i])
            over2.append(array2[i])
    return under1, under2, over1, over2

def StatFinder(asdf):
    sum = 0
    for i in range(len(asdf)):
        sum += asdf[i]
    mean = sum/len(asdf)
    sampleVar = 0
    for i in range(len(asdf)):
        sampleVar += (asdf[i]-mean)*(asdf[i]-mean)
    sampleVar = sampleVar/(len(asdf)-1)
    return mean, sampleVar


def barGraphCreater(data,xname, yname, graphTitle):
    unique, count = np.unique(data, return_counts = True)
    plt.figure()
    labels = ["0-1.99", "2.0-2.29", "2.3-2.69", "2.7-2.99", "3.0-3.29", "3.3-3.69", "3.7-3.99", "4.0"]
    plt.bar(unique, count, width=0.5)
    plt.title(graphTitle)
    plt.xlabel(xname)
    plt.ylabel(yname)




df = pd.read_excel(file_name)

array = pd.DataFrame.to_numpy(df)

attendance = convertAttendance(array[:,2])
study = convertHours(array[:,3])
gpa = convertGpa(array[:,5])
print(StatFinder(attendance))
print(StatFinder(study))
print(StatFinder(gpa))

jitter_amount = 0.07
x_jittered = attendance + np.random.uniform(-jitter_amount, jitter_amount, len(attendance))
y_jittered = gpa + np.random.uniform(-jitter_amount, jitter_amount, len(gpa))


plt.scatter(x_jittered, y_jittered, alpha = 0.3)
plt.show()


underStudy, underGpa, overStudy, overGpa =arraySeparator(study, gpa, 14.5)

#barGraphCreater(underGpa)

#barGraphCreater(overGpa)

print(StatFinder(underStudy))
print(StatFinder(underGpa))

print(StatFinder(overStudy))
print(StatFinder(overGpa))


underAttendance, underGpa, overAttendance, overGpa =arraySeparator(attendance, gpa, 4)

barGraphCreater(underGpa, "Grade Point Average", "Number of People", "GPA Distribution of Students with Attendance Less Than 'Often'")

#barGraphCreater(overGpa)

print(StatFinder(underAttendance))
print(StatFinder(underGpa))

print(StatFinder(overAttendance))
print(StatFinder(overGpa))