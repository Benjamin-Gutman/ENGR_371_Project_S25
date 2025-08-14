import pandas as pd
import matplotlib as mpt
import matplotlib.pyplot as plt
import math
from scipy import stats
import numpy as np



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
            Quant_Gpa[i] = 0.995
        elif phrase == "2.0-2.29":
            Quant_Gpa[i] = 2.145
        elif phrase == "2.3-2.69":
            Quant_Gpa[i] = 2.495
        elif phrase == "2.7-2.99":
            Quant_Gpa[i] = 2.845
        elif phrase == "3.0-3.29":
            Quant_Gpa[i] = 3.145
        elif phrase == "3.3-3.69":
            Quant_Gpa[i] = 3.495
        elif phrase == "3.7-3.99":
            Quant_Gpa[i] = 3.845
        else:
            Quant_Gpa[i] = 4.15
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
    labels = ["2.3-2.69", "2.7-2.99", "3.0-3.29", "3.3-3.69", "3.7-3.99", "4.0+"]
    plt.bar(unique, count, width=0.15)
    plt.title(graphTitle)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.xticks(unique, labels)

def f_test(var1,var2,pop1,pop2):
    if var1>var2:
        f_stat = var1/var2
        bigger = pop1-1
        smaller = pop2-1
    else:
        f_stat = var2/var1
        bigger = pop2-1
        smaller = pop1-1
    p_value = 2*(1- stats.f.cdf(f_stat, bigger, smaller))
    return f_stat, p_value


def poolVariance(var1,var2, n1,n2):
    varPool = ((n1-1)*var1+(n2-1)*var2)/(n1+n2-2)
    return varPool

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

barGraphCreater(underGpa, "Grade Point Average", "Number of People", "GPA Distribution of Students with Hours Studied Under '13-16'")

barGraphCreater(overGpa, "Grade Point Average", "Number of People", "GPA Distribution of Students with Hours Studied Over '13-16'")

print(StatFinder(underStudy))
print(StatFinder(underGpa))

print(StatFinder(overStudy))
print(StatFinder(overGpa))

uGPA, uVar = StatFinder(underGpa)

oGPA, oVar = StatFinder(overGpa)


print(f_test(uVar,oVar, len(underGpa), len(overGpa)))


var = poolVariance(uVar, oVar, len(underGpa), len(overGpa))
print(len(underGpa))

print(var)

print((stats.ttest_ind(underGpa, overGpa, equal_var=True)))





underAttendance, underGpa, overAttendance, overGpa =arraySeparator(attendance, gpa, 4)

barGraphCreater(underGpa, "Grade Point Average", "Number of People", "GPA Distribution of Students with Attendance Less Than 'Often'")

barGraphCreater(overGpa, "Grade Point Average", "Number of People", "GPA Distribution of Students with Attendance More Than 'Often'")

print(StatFinder(underAttendance))
print(StatFinder(underGpa))

print(StatFinder(overAttendance))
print(StatFinder(overGpa))

uGPA, uVar = StatFinder(underGpa)

oGPA, oVar = StatFinder(overGpa)



print(f_test(uVar,oVar, len(underGpa), len(overGpa)))


var = poolVariance(uVar, oVar, len(underGpa), len(overGpa))

print(len(underGpa))

print(var)
print((stats.ttest_ind(underGpa, overGpa, equal_var=True)))


