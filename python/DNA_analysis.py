#!/usr/bin/python
import uproot
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.signal import savgol_filter
import sys


file = uproot.open(sys.argv[1])
file.allkeys()

s1=0
s2=0
s3=0
s4=0


one = file['1']
#one.show()
for i in range(len(one.values)):
	s1 += one.edges[i] * one.values[i]

two = file['2']
#two.show()
for j in range(len(two.values)):
	s2 += two.edges[j] * two.values[j]

three = file['3']
#three.show()
for k in range(len(three.values)):
	s3 += three.edges[k] * three.values[k]

four = file['4']
#four.show()
for l in range(len(four.values)):
	s4 += four.edges[l] * four.values[l]

#print one.edges  	# x axis
#print four.values	# y axis
#print one.variances	# ????

#ysm = savgol_filter( one.values, 5, 3 )
print  ( '%.3f MeV,   %d SSB,   %d DSB,   %d CDS' % (s1/1e6, s2, s3, s4) )

x = [ 'SSB', 'DSB', 'CDS' ]
y = [ s2, s3, s4 ]


fig = plt.figure(tight_layout=True)
gs = gridspec.GridSpec(3, 5)

ax = fig.add_subplot(gs[:3, :3])
ax.bar( one.edges[1:], one.values , width=1.5)
ax.set_ylabel('number of events')
ax.set_xlabel('energy of events (eV)')

ax = fig.add_subplot(gs[:3, 3:5])
barlist = ax.bar( x, y, )
barlist[0].set_color('black')
barlist[2].set_color('blue')
ax.set_ylabel('amount of damage')
ax.set_xlabel('type of DNA damage')



plt.show()


