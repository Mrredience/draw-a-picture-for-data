import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdate
import scipy.stats as stats
def normfun(x, mu, sigma):
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf


is_first_line = True
init = True
line_number = 0
id = []
time = None
timein = []
ele = []
aptime = []
apnumber = []
number = 669
elenumber = 0
max = 0
min = 5000
second = -1
values = []
average = 0
mix = 0
i = 0
while init:
    apnumber.append(number)
    aptime.append(0)
    number += 1
    i += 1
    if i > 937:
        init = False
for row in open("C:/Users/12589/OneDrive/Documents/WeChat Files/id_uv1fn4b413ad11/FileStorage/File/2019-12/onehourdata.csv"):
    # C:/Users/yangjianlei/Desktop/learning/data for an hour.csv
    if is_first_line:
        is_first_line = False
    else:
        values = row.split(",")
        time = values[1]
        newtime = time.split(":")
        mc = newtime[1].split(".")
        # second = (float(newtime[0]) * 60) + float(mc[0]) + (float(mc[1]) * 0.1)
        second += 1
        timein.append(second)
        elenumber = int(values[2])
        ele.append(elenumber)
        mix += elenumber
        i = 0
        if elenumber > max:
            max = elenumber
            maxtime = time
        if elenumber < min:
            min = elenumber
            mintime = time
        while i < len(apnumber):
            if elenumber == apnumber[i]:
                aptime[i] = aptime[i]+1
            i += 1
        if second > 3599:
            break
average = mix / len(ele)
average = round(average, 2)
i = 0
addap = 0
ap = []
print("maxinum = " + str(max))
print("minimum = " + str(min))
print("average = " + str(average))
while i < len(apnumber):
    addap = (float(aptime[i])/3600)
    ap.append(addap)
    i += 1
y = ele
x = timein
while i < len(apnumber):
    if elenumber == apnumber[i]:
        aptime[i] = aptime[i]+1
        i += 1
input = input("which figer you want? ")
if input == "n":
    fig = plt.figure(figsize=(10, 20))
    fig.suptitle("data for an hour")
    plt.ylabel("ele")
    plt.xlabel("time(s)")
    plt.grid()
    plt.plot(x,y)
    plt.show()
if input == "nd":
    fig = plt.figure(figsize=(10, 20))
    plt.title("normal distribution data for an hour")
    plt.ylabel("Probability")
    plt.xlabel("ele")
    eleindata = np.arange(669, 1607)
    probability = ap
    plt.plot(eleindata,probability)
    plt.show()
