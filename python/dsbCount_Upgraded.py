#!/usr/bin/python

# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sys
import os

# Functions
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%d' % int(height),
                ha='center', va='bottom', 
                fontweight='bold')

# Variables
######## DEFINE THESE ##############
nbNucl = 3765 #100                 #
ET = 10                            #
DT = 10                            #
infile = sys.argv[1] 	           #
####################################

#ssb1n = []
#ssb2n = []
ssb1e = []
ssb2e = []
ssb1L = []
ssbx  = []
ssby  = []
ssbx_rep = []
ssby_rep = []
ssb2L = []
ssb1L_rep = []
ssb2L_rep = []
dsb_array = []
dsb_array_rep = []
dsb  = 0
dsb_rep = 0
cds  = 0
ssb1 = 0
ssb2 = 0
ssb1_rep = 0
ssb2_rep = 0
sed1 = 0
sed2 = 0
sed3 = 0
chs_1 = 0
chs_2 = 0
totEdep = 0
xi = 0
yi = 0

# FUNCTIONS
def rep_ssb():
    global xi
    nb = np.random.uniform(1, 100)
    if (nb < 4+1):
        xi = 1
    else:
        xi = 0
    return xi

def rep_dsb():
    global xi
    nb = np.random.uniform(1, 100)
    if (nb < 15+1):
        yi = 1
    else:
        yi = 0
    return yi



#REDIRECT STDOUT PRINT TO FILE
curr_path = os.path.dirname(os.path.realpath(__file__))
orig_stdout = sys.stdout
f = open(curr_path+'/analysisOutput.txt', 'w')
sys.stdout = f

for i in range( nbNucl ):
#    ssb1n.append(i)
#    ssb2n.append(i)
    ssb1e.append(0)
    ssb2e.append(0)


with open (infile, 'r') as fp:
    line = fp.readline()

    while line:
        line = fp.readline()
        spl = line.split()
        if len(spl) == 3:
            if spl[0] == 'A':
                nucl1 = int(spl[1])
                edep1 = float(spl[2])
                totEdep += edep1
                ssb1e[nucl1] += edep1

            elif spl[0] == 'B':
                nucl2 = int(spl[1])
                edep2 = float(spl[2])
                totEdep += edep2
                ssb2e[nucl2] += edep2


for sed1 in ssb1e:
    if sed1 >= ET:
        ssb1 += 1
        ssb1L.append((ssb1e.index(sed1),sed1))
        rep_ssb()
        if (xi > 0):
            ssb1_rep +=1
            ssb1L_rep.append((ssb1e.index(sed1),sed1))

for sed2 in ssb2e:
    if sed2 >= ET:
        ssb2 += 1
        ssb2L.append((ssb2e.index(sed2),sed2))
        rep_ssb()
        if (xi > 0):
            ssb2_rep +=1
            ssb2L_rep.append((ssb2e.index(sed2),sed2))


for sed1 in ssb1e:
    if sed1 >= ET:
        for sed2 in ssb2e:
            if sed2 >= ET:
                dif = abs( ssb1e.index(sed1) - ssb2e.index(sed2) )
                if ( dif <= DT ):
                    print ( "DSB", (ssb1e.index(sed1),sed1), (ssb2e.index(sed2),sed2), dif )
                    dsb += 1
                    dsb_array.append(( ssb1e.index(sed1), ssb2e.index(sed2) ))
                    rep_dsb()
                    if (yi > 0):
                        dsb_rep += 1
                        dsb_array_rep.append(( ssb1e.index(sed1), ssb2e.index(sed2) ))
                        print ( "Unrepaired DSB", (ssb1e.index(sed1),sed1), (ssb2e.index(sed2),sed2), dif )
                    

for sed1 in ssb1e:
    if sed1 >= ET:
        for sed2 in ssb1e:
            if sed2 >= ET:
                dif = abs( ssb1e.index(sed1) - ssb1e.index(sed2) )
                #print (ssb1e.index(sed1), ssb1L_rep)
                if (ssb1e.index(sed1),sed1) not in ssb1L_rep:
                    if ( 0 < dif <= DT ):
                        for sed3 in ssb2e:
                            if sed3 >= ET:
                                dif_1 = abs( ssb1e.index(sed1) - ssb2e.index(sed3) )
                                dif_2 = abs( ssb1e.index(sed2) - ssb2e.index(sed3) )
                                if ( dif_1 <= DT and dif_2 <= DT ):
                                    ssb1L_rep.append((ssb1e.index(sed1),sed1))
                                    ssb1_rep +=1
                                    if (ssb1e.index(sed2),sed2) not in ssb1L_rep:
                                        ssb1L_rep.append((ssb1e.index(sed2),sed2))
                                        ssb1_rep +=1
                                    if (ssb2e.index(sed3),sed3) not in ssb2L_rep:
                                        ssb2L_rep.append((ssb2e.index(sed3),sed3))
                                        ssb2_rep +=1
                                    print ( "CDS", (ssb1e.index(sed1),sed1), (ssb1e.index(sed2),sed2), (ssb2e.index(sed3),sed3), dif, dif_1, dif_2 )
                                    cds += 1 
                                    if (ssb1e.index(sed1),ssb2e.index(sed3)) not in dsb_array_rep:
                                        dsb_array_rep.append(( ssb1e.index(sed1), ssb2e.index(sed3) ))
                                        dsb_rep += 1
                                    if (ssb1e.index(sed2),ssb2e.index(sed3)) not in dsb_array_rep:
                                        dsb_array_rep.append(( ssb1e.index(sed2), ssb2e.index(sed3) ))
                                        dsb_rep += 1


for sed1 in ssb2e:
    if sed1 >= ET:
        for sed2 in ssb2e:
            if sed2 >= ET:
                dif = abs( ssb2e.index(sed1) - ssb2e.index(sed2) )
                #print (ssb2e.index(sed1), ssb2L_rep)
                if (ssb2e.index(sed1),sed1) not in ssb2L_rep:
                    if ( 0 < dif <= DT ):
                        for sed3 in ssb1e:
                            if sed3 >= ET:
                                dif_1 = abs( ssb2e.index(sed1) - ssb1e.index(sed3) )
                                dif_2 = abs( ssb2e.index(sed2) - ssb1e.index(sed3) )
                                if ( dif_1 <= DT and dif_2 <= DT ):
                                    ssb2L_rep.append((ssb2e.index(sed1),sed1))
                                    ssb2_rep +=1
                                    if (ssb2e.index(sed2),sed2) not in ssb2L_rep:
                                        ssb2L_rep.append((ssb2e.index(sed2),sed2))
                                        ssb2_rep +=1
                                    if (ssb1e.index(sed3),sed3) not in ssb1L_rep:
                                        ssb1L_rep.append((ssb1e.index(sed3),sed3))
                                        ssb1_rep +=1  
                                    print ( "CDS", (ssb2e.index(sed1),sed1), (ssb2e.index(sed2),sed2), (ssb1e.index(sed3),sed3), dif, dif_1, dif_2 )
                                    cds += 1    
                                    if (ssb2e.index(sed1),ssb1e.index(sed3)) not in dsb_array_rep:
                                        dsb_array_rep.append(( ssb2e.index(sed1), ssb1e.index(sed3) ))
                                        dsb_rep += 1
                                    if (ssb2e.index(sed2),ssb1e.index(sed3)) not in dsb_array_rep:
                                        dsb_array_rep.append(( ssb2e.index(sed2), ssb1e.index(sed3) ))
                                        dsb_rep += 1







totSSB = ssb1 + ssb2
totSSB_rep = ssb1_rep + ssb2_rep
print ("\nSingle Strand Breaks on strand A:\n" + str(ssb1L) + "\n" )
print ("Unrepaired Single Strand Breaks on strand A:\n" + str(ssb1L_rep) + "\n" )
print ("Single Strand Breaks on strand B:\n" + str(ssb2L) + "\n" )
print ("Unrepaired Single Strand Breaks on strand B:\n" + str(ssb2L_rep) + "\n" )

print ( "\nThe number of SSBs on strand A:" + str(ssb1) + "   strand B:" + str(ssb2) + "   and in total:" + str(totSSB) )
print ( "The number of unrepaired SSBs on strand A:" + str(ssb1_rep) + "   strand B:" + str(ssb2_rep) + "   and in total:" + str(totSSB_rep) )
print ( "The total number of DSBs is: " + str(dsb) + " DSBs." )
print ( "The total number of unrepaired DSBs is: " + str(dsb_rep) + " DSBs." )
print ( "The total number of CDSs is: " + str(cds) + " CDSs." )
print ( "Total Energy Deposited in the Molecule: " + str(totEdep) + " eV\n")

sys.stdout = orig_stdout
f.close()

for i,j in ssb1L:
    ssby.append(i)
    ssbx.append(1)
for i,j in ssb2L:
    ssby.append(i)
    ssbx.append(2)

for i,j in ssb1L_rep:
    ssby_rep.append(i)
    ssbx_rep.append(1)
for i,j in ssb2L_rep:
    ssby_rep.append(i)
    ssbx_rep.append(2)

x = [ 'SSB', 'DSB', 'CDS' ]
y = [ totSSB, dsb, cds ]
y_rep = [ totSSB_rep, dsb_rep, cds ]

fig = plt.figure(figsize=(10, 10)) #tight_layout=True
gs = gridspec.GridSpec(7, 8)

ax = fig.add_subplot(gs[:3, :2])
ax.scatter( ssbx, ssby )
ax.set_ylabel('nucleotide id')
ax.set_xlabel('DNA strand id')
ax.set_xlim(-0.5,3.5)
#ax.set_ylim(0,nbNucl)

ax = fig.add_subplot(gs[:3, 3:8])
barlist = ax.bar( x, y )
barlist[1].set_color('black')
barlist[2].set_color('red')
ax.set_ylabel('amount of damage')
ax.set_xlabel('type of DNA damage')
autolabel(barlist)

ax = fig.add_subplot(gs[4:7, :2])
ax.scatter( ssbx_rep, ssby_rep )
ax.set_ylabel('nucleotide id')
ax.set_xlabel('DNA strand id \nafter the repair procedure')
ax.set_xlim(-0.5,3.5)
#ax.set_ylim(0,nbNucl)

ax = fig.add_subplot(gs[4:7, 3:8])
barlist = ax.bar( x, y_rep )
barlist[1].set_color('black')
barlist[2].set_color('red')
ax.set_ylabel('amount of damage')
ax.set_xlabel('type of DNA damage \nafter the repair procedure')
autolabel(barlist)


plt.show()
