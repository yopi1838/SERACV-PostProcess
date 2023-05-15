#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 18:20:18 2022

@author: aamehrotra
"""
#import pylustrator
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import savemat 

#fldr = '4%_softening (only 75%)/'
fldr = 'hist_softening_new_20230220/'
ext = ''
sh = 2#+(3*3999) #histories are being appended - adjust accordingly 

# read TIME
time_ = np.genfromtxt(fldr+'TIME'+ext+'.txt',skip_header=sh)
time_ = time_[:,1]

tnstep = min(abs(np.diff(time_))) #Recordings were taken at every 1000 steps
end = len(time_)    #keep as this for all except US-5, where we manually input 38720
print("Timestep : ",tnstep," s. End of line : ",end)

# read shake table acceleration and displacement 
# st_ay = np.genfromtxt(fldr+'SHAKE_ACCy'+ext+'.txt',skip_header=sh)
# st_ay = st_ay[:,1]
st_vy = np.genfromtxt(fldr+'SHAKE-TABLE-VELy'+ext+'.txt',skip_header=sh)
st_vy = st_vy[:,1]
st_dy = np.genfromtxt(fldr+'SHAKE-TABLE-DISPLy'+ext+'.txt',skip_header=sh)
st_dy = st_dy[:,1]

# read accelerations at different monitoring points 
# X DIRECTION (no subtraction since no motion of ST in this direction)
acc2x = np.genfromtxt(fldr+'ACC2-x'+ext+'.txt',skip_header=sh)
acc2x = acc2x[:,1]
acc6x = np.genfromtxt(fldr+'ACC6-x'+ext+'.txt',skip_header=sh)
acc6x = acc6x[:,1]
acc12x = np.genfromtxt(fldr+'ACC12-x'+ext+'.txt',skip_header=sh)
acc12x = acc12x[:,1]
acc14x = np.genfromtxt(fldr+'ACC14-x'+ext+'.txt',skip_header=sh)
acc14x = acc14x[:,1]
acc18x = np.genfromtxt(fldr+'ACC18-x'+ext+'.txt',skip_header=sh)
acc18x = acc18x[:,1]

# Y DIRECTION (subtract acceleration of ST from recorded accelerations)
acc2y = np.genfromtxt(fldr+'ACC2-y'+ext+'.txt',skip_header=sh)
acc2y = acc2y[:,1]
acc6y = np.genfromtxt(fldr+'ACC6-y'+ext+'.txt',skip_header=sh)
acc6y = acc6y[:,1]
acc12y = np.genfromtxt(fldr+'ACC12-y'+ext+'.txt',skip_header=sh)
acc12y = acc12y[:,1]
acc14y = np.genfromtxt(fldr+'ACC14-y'+ext+'.txt',skip_header=sh)
acc14y = acc14y[:,1]
acc18y = np.genfromtxt(fldr+'ACC18-y'+ext+'.txt',skip_header=sh)
acc18y = acc18y[:,1]

# read velocities at different monitoring points 
# X DIRECTION (no subtraction since no motion of ST in this direction)
vel2x = np.genfromtxt(fldr+'VEL2-x'+ext+'.txt',skip_header=sh)
vel2x = vel2x[:,1]
vel6x = np.genfromtxt(fldr+'VEL6-x'+ext+'.txt',skip_header=sh)
vel6x = vel6x[:,1]
vel12x = np.genfromtxt(fldr+'VEL12-x'+ext+'.txt',skip_header=sh)
vel12x = vel12x[:,1]
vel14x = np.genfromtxt(fldr+'VEL14-x'+ext+'.txt',skip_header=sh)
vel14x = vel14x[:,1]
vel18x = np.genfromtxt(fldr+'VEL18-x'+ext+'.txt',skip_header=sh)
vel18x = vel18x[:,1]

# Y DIRECTION (subtract velocity of ST from recorded accelerations)
vel2y = np.genfromtxt(fldr+'VEL2-y'+ext+'.txt',skip_header=sh)
vel2y = vel2y[:,1]
vel6y = np.genfromtxt(fldr+'VEL6-y'+ext+'.txt',skip_header=sh)
vel6y = vel6y[:,1]
vel12y = np.genfromtxt(fldr+'VEL12-y'+ext+'.txt',skip_header=sh)
vel12y = vel12y[:,1]
vel14y = np.genfromtxt(fldr+'VEL14-y'+ext+'.txt',skip_header=sh)
vel14y = vel14y[:,1]
vel18y = np.genfromtxt(fldr+'VEL18-y'+ext+'.txt',skip_header=sh)
vel18y = vel18y[:,1]

# read displacements at different monitoring points 
# X DIRECTION (no subtraction since no motion of ST in this direction)
dis2x = np.genfromtxt(fldr+'DIS2-x'+ext+'.txt',skip_header=sh)
dis2x = dis2x[:,1]
dis6x = np.genfromtxt(fldr+'DIS6-x'+ext+'.txt',skip_header=sh)
dis6x = dis6x[:,1]
dis12x = np.genfromtxt(fldr+'DIS12-x'+ext+'.txt',skip_header=sh)
dis12x = dis12x[:,1]
dis14x = np.genfromtxt(fldr+'DIS14-x'+ext+'.txt',skip_header=sh)
dis14x = dis14x[:,1]
dis18x = np.genfromtxt(fldr+'DIS18-x'+ext+'.txt',skip_header=sh)
dis18x = dis18x[:,1]

# Y DIRECTION (subtract velocity of ST from recorded accelerations)
dis2y = np.genfromtxt(fldr+'DIS2-y'+ext+'.txt',skip_header=sh)
dis2y = dis2y[:,1]
dis6y = np.genfromtxt(fldr+'DIS6-y'+ext+'.txt',skip_header=sh)
dis6y = dis6y[:,1]
dis12y = np.genfromtxt(fldr+'DIS12-y'+ext+'.txt',skip_header=sh)
dis12y = dis12y[:,1]
dis14y = np.genfromtxt(fldr+'DIS14-y'+ext+'.txt',skip_header=sh)
dis14y = dis14y[:,1]
dis18y = np.genfromtxt(fldr+'DIS18-y'+ext+'.txt',skip_header=sh)
dis18y = dis18y[:,1]

# optical camera data 
OC1y = np.genfromtxt(fldr+'OC1-y'+ext+'.txt',skip_header=sh)
OC1y = OC1y[:,1]
OC2x = np.genfromtxt(fldr+'OC2-x'+ext+'.txt',skip_header=sh)
OC2x = OC2x[:,1]
OC2y = np.genfromtxt(fldr+'OC2-y'+ext+'.txt',skip_header=sh)
OC2y = OC2y[:,1]
OC4x = np.genfromtxt(fldr+'OC4-x'+ext+'.txt',skip_header=sh)
OC4x = OC4x[:,1]
OC4y = np.genfromtxt(fldr+'OC4-y'+ext+'.txt',skip_header=sh)
OC4y = OC4y[:,1]


# # read TIME
# time_2 = np.genfromtxt(fldr2+'TIME'+ext+'.txt',skip_header=sh)
# time_2 = time_2[:,1]

# # read shake table acceleration and displacement 
# st_ay2 = np.genfromtxt(fldr2+'SHAKE_ACCy'+ext+'.txt',skip_header=sh)
# st_ay2 = st_ay2[:,1]
# st_vy2 = np.genfromtxt(fldr2+'SHAKE_VELy'+ext+'.txt',skip_header=sh)
# st_vy2 = st_vy2[:,1]
# st_dy2 = np.genfromtxt(fldr2+'SHAKE_DISPLy'+ext+'.txt',skip_header=sh)
# st_dy2 = st_dy2[:,1]

# acc2y2 = np.genfromtxt(fldr2+'ACC2y'+ext+'.txt',skip_header=sh)
# acc2y2 = acc2y2[:,1]-st_ay2

# vel2y2 = np.genfromtxt(fldr2+'VEL2y'+ext+'.txt',skip_header=sh)
# vel2y2 = vel2y2[:,1]-st_vy2

# dis2y2 = np.genfromtxt(fldr2+'DIS2y'+ext+'.txt',skip_header=sh)
# dis2y2 = dis2y2[:,1]-st_dy2

arr_dis = [max(abs(OC1y[0:end])),max(abs(OC2x[0:end])),max(abs(OC2y[0:end])),max(abs(OC4x[0:end])),max(abs(OC4y[0:end]))]

arr_res = [max(abs(acc2x[0:end])),max(abs(acc2y[0:end])),max(abs(acc6x[0:end])),max(abs(acc6y[0:end])),
           max(abs(acc12x[0:end])),max(abs(acc12y[0:end])),max(abs(acc14x[0:end])),max(abs(acc14y[0:end])),
           max(abs(acc18x[0:end])),max(abs(acc18y[0:end]))]
arr_diff = [max(abs(np.diff(vel2x[0:end])/tnstep)),max(abs(np.diff(vel2y[0:end])/tnstep)),
            max(abs(np.diff(vel6x[0:end])/tnstep)),max(abs(np.diff(vel6y[0:end])/tnstep)),
            max(abs(np.diff(vel12x[0:end])/tnstep)),max(abs(np.diff(vel12y[0:end])/tnstep)),
            max(abs(np.diff(vel14x[0:end])/tnstep)),max(abs(np.diff(vel14y[0:end])/tnstep)),
            max(abs(np.diff(vel18x[0:end])/tnstep)),max(abs(np.diff(vel18y[0:end])/tnstep)),]
print(arr_res)
print(arr_diff)

#pylustrator.start()

# # # st_ay2 = np.diff(np.diff(st_dy)/0.001)/0.001

#fig, ax1 = plt.subplots()
#ax1.plot(time_[1:],np.diff(vel2y)/0.001,linewidth=1)
# ax1.plot(time_,vel12x,linestyle='-',linewidth=1)
# #plt.plot(time_2,st_vy2,linewidth=1)
# #plt.plot(time_2,vel2y2,linestyle='-',linewidth=1)
# ax2 = ax1.twinx()
# ax2.plot(time_,OC1y)
# ax2.plot(time_,OC2y)
# ax2.plot(time_,OC4y)
# ax2.plot(time_[1:],np.diff(vel12x)/0.001,linestyle='-',linewidth=0.5)
# ax1.plot(time_,vel18x,linestyle='-',linewidth=1)
# ax2.plot(time_[1:],np.diff(vel18x)/0.001,linestyle='-',linewidth=0.5)
# ax1.plot(time_,vel18y,linestyle='-',linewidth=1)
# ax2.plot(time_[1:],np.diff(vel18y)/0.001,linestyle='-',linewidth=0.5)
# #plt.plot(time_[2:],np.diff(np.diff(dis2y)/0.001)/0.001,linewidth=0.5)
# #% start: automatic generated code from pylustrator
# # plt.figure(1).ax_dict = {ax.get_label(): ax for ax in plt.figure(1).axes}
# # plt.figure(1).axes[0].set_xlim(4.2, 5.0)
# # #plt.figure(1).axes[0].set_ylim(-40, 40)
# # plt.figure(1).axes[0].get_xaxis().get_label().set_text("time (s)")
# # plt.figure(1).axes[0].get_yaxis().get_label().set_text("vel (m/s)")
# #% end: automatic generated code from pylustrator
#plt.show()


# mdic = {'time':time_,'real_acc':st_ay,'diff_acc':st_ay2}
# savemat("/Volumes/GoogleDrive/My Drive/Rhino/Matlab/Matlab_block_EQ/VBP_acc_comp.mat",mdic)


# plt.plot(time_[6316:],OC2x[6316:])
# #plt.figure()
# plt.plot(time_[0:6314],OC2x[0:6314])

# acc2y_temp = np.diff(np.diff(OC4y)/0.001)/0.001

# plt.figure()
# plt.plot(time_,acc2y)
# plt.plot(time_[:-2],acc2y_temp)
# plt.xlabel('time (s)')
# plt.ylabel("ACC2Y (m/s^2)")

# acc2x_temp = np.diff(np.diff(OC4x)/0.001)/0.001

# plt.figure()
# plt.plot(time_,acc2x)
# plt.plot(time_[:-2],acc2x_temp)
# plt.xlabel('time (s)')
# plt.ylabel("ACC2X (m/s^2)")
