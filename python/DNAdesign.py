#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

from mpl_toolkits.mplot3d import Axes3D


# GLOBAL VARIABLES
rs = 2
r = 15
adstr = 20  # Distance between the two complementary strands
strNb = -adstr
step = 0.05
rang = 10000
xi = 0

rStr = 600  # The radius of each strand (angstroms)
stStr = 10  # The step of each strand after each rotation (angstroms)


# FUNCTIONS
def x(t):
    for i in range(rang):
        global xi
        nb = np.random.uniform(-r, r)
        if (nb > rs and nb < r):
            xi = nb + rStr * np.sin(t)
            break
    return xi


def y(hi, t):
    for j in range(rang):
        num = np.random.uniform(-r, r)
        d = 0
        rr = 0
        rsrs = 0
        d = num * num + (hi - rStr * np.sin(t)) * (hi - rStr * np.sin(t))
        rr = r * r
        rsrs = rs * rs
        if (d > rsrs and d < rr):
            yi = num + rStr * np.cos(t)
            break
    return yi


def z(t):
    for k in range(rang):
        nm = np.random.uniform(-r, r)
        if nm > rs:
            randZ = nm
            zi = stStr * t + randZ + strNb
            break
    return zi

#REDIRECT STDOUT PRINT TO FILE
curr_path = os.path.dirname(os.path.realpath(__file__))
orig_stdout = sys.stdout
f = open(curr_path+'/printOutput.txt', 'w')
sys.stdout = f

# THE OUTPUT FILE
dir_path1 = os.path.dirname(os.path.realpath(__file__))
outfile = open(dir_path1+'/'+sys.argv[1], 'w+')

# TO VISUALIZE THE DNA WITH MATPLOTLIB
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+'/dnaBasesSequence.dat', 'r') as infile:
    line = infile.readline()
    # outfile.write(line)
    outfile.write('HEADER  DNA \n')  # MUST NEVER CHANGE
    outfile.write('TITLE    DNA DOSIMETER \n')  # YOU CAN CHANGE THE TITLE

    ws = ' '
    cnt = 0

    while line:
        strNb += adstr
        t = 0
        # cnt = 0
        countBase = 0
        if strNb == 0:
            strandID = 'X'
        else:
            strandID = 'Y'
        line = infile.readline()
        print(line)
        for c in line:
            countBase += 1
            t += step
            # print c
            if c == 'A':
                cnt += 1
                outLine = "ATOM" + ws + format(cnt, "6d") + ws + ws + "O5' DA" + ws + ws + strandID + format(countBase,
                                                                                                             "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C5' DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H5' DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H5'' DA" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C4' DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H4' DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O4' DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C3' DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H3' DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O3' DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C2' DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C1' DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H1' DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H2'1 DA" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H2'2 DA" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N9  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C8  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H8  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N7  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C5  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C4  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C6  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N3  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C2  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N1  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H2  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N6  DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H61 DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H62 DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H5T DA" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))

                outfile.write(outLine)

            if c == 'T':
                cnt += 1
                outLine = "ATOM" + ws + format(cnt, "6d") + ws + ws + "P   DT" + ws + ws + strandID + format(countBase,
                                                                                                             "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "P" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "OP1 DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "OP2 DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O5* DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C5* DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H5*1 DT" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H5*2 DT" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C4* DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H4* DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O4* DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C3* DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H3* DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O3* DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C2* DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C1* DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H1* DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H2*1 DT" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H2*2 DT" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N1  DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C2  DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O2  DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N3  DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H3  DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C4  DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O4  DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C5  DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C7  DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H71 DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H72 DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H73 DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C6  DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H6  DT" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))

                outfile.write(outLine)

            if c == 'G':
                cnt += 1
                outLine = "ATOM" + ws + format(cnt, "6d") + ws + ws + "P   DG" + ws + ws + strandID + format(countBase,
                                                                                                             "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "P" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "OP1 DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "OP2 DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O5* DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C5* DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H5*1 DG" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H5*2 DG" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C4* DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H4* DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O4* DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C3* DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H3* DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O3* DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C2* DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C1* DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H1* DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H2*1 DG" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H2*2 DG" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N9  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C8  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H8  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N7  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C5  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C4  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C6  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N3  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C2  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N1  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H1  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N2  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H21 DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H22 DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O6  DG" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))

                outfile.write(outLine)

            if c == 'C':
                cnt += 1
                outLine = "ATOM" + ws + format(cnt, "6d") + ws + ws + "P   DC" + ws + ws + strandID + format(countBase,
                                                                                                             "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "P" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "OP1 DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "OP2 DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O5* DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C5* DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H5*1 DC" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H5*2 DC" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C4* DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H4* DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O4* DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C3* DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H3* DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O3* DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C2* DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C1* DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H1* DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H2*1 DC" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + "H2*2 DC" + ws + ws + strandID + format(countBase,
                                                                                                          "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N1  DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C2  DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "O2  DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "O" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N3  DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C4  DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "N4  DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "N" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H41 DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H42 DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C5  DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H5  DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "C6  DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "C" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))
                cnt += 1
                outLine += "ATOM" + ws + format(cnt, "6d") + ws + ws + "H6  DC" + ws + ws + strandID + format(countBase,
                                                                                                              "4d") + ws + ws + ws + format(
                    x(t), "9.3f") + format(y(xi, t), "9.3f") + format(z(t),
                                                                      "9.3f") + ws + ws + "1.00" + ws + ws + "0.00" + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + ws + "H" + ws + '\n'
                ax.scatter(x(t),y(xi,t),z(t))

                outfile.write(outLine)
        print(countBase, '  base pairs')
        cnt += 1
        outfile.write('TER   \n')  # MUST NEVER CHANGE


outfile.close()
infile.close()
print(outfile, '  has been produced')
sys.stdout = orig_stdout
f.close()
plt.show()
plt.close()

