import os
from pathlib import Path
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import argparse

def multiFigureAcc(loadlevel,STR,inc):
    data_folder="hist_softening_new_{}percent_mass_4percent".format(str(loadlevel))
    # data_folder="prediction-model"
    target_folder = "expcomparison_new_{}percent_mass_4percent_cumvsno".format(str(loadlevel))
    direct_datafolder = "hist_softening_4percent_mass"
    X_direct = np.genfromtxt(fname=os.path.join(direct_datafolder,"TIME.txt"),skip_header=2)
    X_direct = X_direct[:,1]
    isExist = os.path.exists(target_folder)
    tnstep = 1.25e-3
    tnstep_direct = 1e-2
    time_slice = None
    if not isExist:
        os.makedirs(target_folder)
    count=0
    print(tnstep*inc)
    exp_folder = "expresult_{}_{}".format(STR,str(loadlevel))
    acc=["ACC2-x","ACC6-x","ACC12-x","ACC14-x","ACC2-y","ACC6-y","ACC12-y","ACC14-y","ACC18-x","ACC18-y"]
    vel=["VEL2-x","VEL6-x","VEL12-x","VEL14-x","VEL2-y","VEL6-y","VEL12-y","VEL14-y","VEL18-x","VEL18-y"]
    X = np.genfromtxt(fname=os.path.join(data_folder,"TIME.txt"),skip_header=2)
    X = X[:,1]

    rows=3
    cols=4
    f = plt.figure(figsize=(10,8))
    gs = gridspec.GridSpec(3,4,figure=f)
    axs = []
    plt.rcParams['axes.titley'] = 1.0    # y is in axes-relative coordinates.
    plt.rcParams['axes.titlepad'] = -14
    n=0
    for i in range(rows):
        for j in range(cols):
            if i==2:
                if j%2!=0:
                    continue
            findFlag=False
            file = os.path.join(exp_folder,"{}.txt".format(acc[n]))
            if loadLevel==75:
                exp_OC1 = np.loadtxt(fname=file,delimiter="\t",skiprows=1)
                exp_OC1[:,1] -= exp_OC1[3,1]
            else:
                exp_OC1 = np.loadtxt(fname=file,delimiter=" ",skiprows=1)
                exp_OC1[:,1] -= exp_OC1[3,1]
            num_data = os.path.join(data_folder,"{}.txt".format(vel[n]))
            vel18y= np.genfromtxt(fname=num_data,skip_header=2)
            num_data_direct = os.path.join(direct_datafolder,"{}.txt".format(vel[n]))
            vel18y_direct = np.genfromtxt(fname=num_data_direct,skip_header=2)
            index_time = len(X)
            index_time_direct = len(X_direct)
            num_OC1 = np.stack((X[:], vel18y[:,1]), axis=1)
            num_OC1_direct = np.stack((X_direct[:], vel18y_direct[:,1]), axis=1)
            if inc ==1:
                acc18y = [(num_OC1[i,1]-num_OC1[i-inc,1])/(tnstep*inc) for i in range(1,len(num_OC1))]
                acc18y = [(num_OC1_direct[i,1]-num_OC1_direct[i-inc,1])/(tnstep_direct*inc) for i in range(1,len(num_OC1_direct))]
                new_time = X[0:index_time:inc]
                acc18y.insert(0,0)
            else:
                acc18y = np.diff(vel18y[:index_time:inc,1])/(tnstep*inc)
                acc18y_direct = np.diff(vel18y_direct[:index_time_direct:inc,1])/(tnstep_direct*inc*0.35)
                acc18y = np.insert(acc18y,0,0,axis=0)
                acc18y_direct = np.insert(acc18y_direct,0,0,axis=0)
                new_time = X[0:index_time:inc]
                new_time_direct = X_direct[0:index_time_direct:inc]
            Y = np.stack((new_time[:], acc18y[:]*-1), axis=1)
            Y_direct = np.stack((new_time_direct[:], acc18y_direct[:]*-1), axis=1)
            title =  Path(file).stem
            if n ==8:
                axs.append(f.add_subplot(gs[2,:2]))
            elif n ==9:
                axs.append(f.add_subplot(gs[2,2:]))
            else:
                axs.append(f.add_subplot(gs[i,j]))
            axs[-1].plot(exp_OC1[:,0],exp_OC1[:,1],linestyle="dashed",linewidth=0.5,color="blue")
            axs[-1].plot(Y[:,0],Y[:,1],linewidth=1,color="red")
            axs[-1].plot(Y_direct[:,0],Y_direct[:,1],linewidth=1.25,linestyle="dashdot",color="green")
            axs[-1].grid(linestyle='dotted')
            if i ==1:
                axs[-1].set_xlabel("time (s)")
            if j == 0:
                axs[-1].set_ylabel("Acceleration ($m/s^2$)")
            if i ==2:
                if j == 0:
                    axs[-1].set_ylabel("Acceleration ($m/s^2$)")
                axs[-1].set_xlabel("time (s)")
            axs[-1].set_xlim([0,16])
            axs[-1].set_ylim([-8,8])
            axs[-1].set_xticks(np.arange(0,17,2))
            axs[-1].set_title(title,fontsize=11)
            axs[-1].legend(["EXP_{}{}".format(STR,loadlevel),"3DEC_CUM","3DEC_DIR"],loc="lower right",prop={'size': 8}) 

            n+=1
    f.tight_layout()
    plt.show()
    pass

def multiFigureDisp(loadlevel,STR,inc):
    data_folder="hist_softening_new_{}percent_mass_4percent".format(str(loadlevel))
    ### if you used the POSTdiction model, don't forget to change the np array to two dimensional.
    #data_folder="prediction-model"
    target_folder = "expcomparison_new_{}percent_mass_4percent_cumvsno".format(str(loadlevel))
    isExist = os.path.exists(target_folder)
    tnstep = 1.25e-3
    time_slice = None
    if not isExist:
        os.makedirs(target_folder)
    count=0
    print(tnstep*inc)
    exp_folder = "expresult_{}_{}".format(STR,str(loadlevel))
    acc=["OC1-y","OC2-x","OC2-y","OC4-x","OC4-y"]
    vel=["OC1-y","OC2-x","OC2-y","OC4-x","OC4-y"]
    X = np.genfromtxt(fname=os.path.join(data_folder,"TIME.txt"),skip_header=2)
    X = X[:,1]
    rows=3
    cols=2
    f, axs = plt.subplots(  nrows=rows,ncols=cols,\
                            sharex=True,
                            figsize=(8,8),\
                            subplot_kw=dict(adjustable='box'))
    plt.rcParams['axes.titley'] = 1.0    # y is in axes-relative coordinates.
    #plt.rcParams['axes.titlepad'] = -14
    n=0
    for i in range(rows):
        for j in range(cols):
            if j ==1 and i ==0:
                break
            findFlag=False
            file = os.path.join(exp_folder,"{}.txt".format(vel[n]))
            if loadLevel==75:
                exp_OC1 = np.loadtxt(fname=file,delimiter="\t",skiprows=2)
                exp_OC1[:,1] -= exp_OC1[3,1]
            else:
                exp_OC1 = np.loadtxt(fname=file,delimiter=" ",skiprows=2)
                exp_OC1[:,1] -= exp_OC1[3,1]
            title =  Path(file).stem
            num_data = os.path.join(data_folder,"{}.txt".format(vel[n]))
            dispData = np.genfromtxt(fname=num_data,skip_header=2)
            Y = [yi * 1000 for yi in dispData[:,1]]
            axs[i,j].plot(exp_OC1[:,0],exp_OC1[:,1],linestyle="dashed",linewidth=0.5,color="blue")
            axs[i,j].plot(X,Y,linewidth=1,color="red") 
            axs[i,j].grid(linestyle='dotted')
            axs[i,j].set_ylabel("Displacement (mm)")
            if i ==2:
                axs[i,j].set_xlabel("dyna time (s)")
            elif i ==1 and j ==1 :
                axs[i,j].set_xlabel("dyna time (s)")
            axs[i,j].set_xlim([0,16])
            axs[i,j].set_title(title,fontsize=11)
            if n == 1:
                axs[i,j].legend(["EXP_{}{}".format(STR,loadlevel),"3DEC_mass_4%_PRE"],loc="lower left",prop={'size': 8})  
            else:
                axs[i,j].legend(["EXP_{}{}".format(STR,loadlevel),"3DEC_mass_4%_PRE"],loc="lower right",prop={'size': 8}) 
            n+=1
            
            if n>4:
                findFlag=True
                break
        if findFlag:
            break
    plt.delaxes(axs[0,1])
    f.tight_layout()
    plt.show()
    pass

def multfigure_dep(loadlevel,STR,inc):
    data_folder="hist_softening_new_{}percent_mass_4percent".format(str(loadlevel))
    ##Uncomment this line if you want to plot the direct displacement
    direct_datafolder = "hist_softening_75percent_mass_3percent"
    X_direct = np.genfromtxt(fname=os.path.join(direct_datafolder,"TIME.txt"),skip_header=2)
    X_direct = X_direct[:,1]
    target_folder = "expcomparison_new_{}percent_mass_4percent_cumvsno".format(str(loadlevel))
    isExist = os.path.exists(target_folder)
    tnstep = 1.25e-3
    if not isExist:
        os.makedirs(target_folder)
    print(tnstep*inc)
    exp_folder = "expresult_{}_{}".format(STR,str(loadlevel))
    acc=["OC1-y","OC2-x","OC2-y","OC4-x","OC4-y"]
    vel=["OC1-y","OC2-x","OC2-y","OC4-x","OC4-y"]
    X = np.genfromtxt(fname=os.path.join(data_folder,"TIME.txt"),skip_header=2)
    X = X[:,1]
    f = plt.figure(figsize=(8,8))
    gs = gridspec.GridSpec(3, 2,figure=f)
    axs = []
    plt.rcParams['axes.titley'] = 1.0    # y is in axes-relative coordinates.
    plt.rcParams['axes.titlepad'] = -14
    n = 0
    findFlag = False
    for i in range(3):
        for j in range(2):
            if i == 0 and j ==1:
                continue
            file = os.path.join(exp_folder,"{}.txt".format(vel[n]))
            if loadLevel==75:
                exp_OC1 = np.loadtxt(fname=file,delimiter="\t",skiprows=1)
                exp_OC1[:,1] -= exp_OC1[3,1]
            else:
                exp_OC1 = np.loadtxt(fname=file,delimiter=" ",skiprows=1)
                exp_OC1[:,1] -= exp_OC1[3,1]
            title =  Path(file).stem
            num_data = os.path.join(data_folder,"{}.txt".format(vel[n]))
            dispData = np.genfromtxt(fname=num_data,skip_header=2)
            Y = [yi * 1000 for yi in dispData[:,1]]
            num_data_direct = os.path.join(direct_datafolder,"{}.txt".format(vel[n]))
            dispData_direct = np.genfromtxt(fname=num_data_direct,skip_header=2) 
            dispData_direct[:,1] -= dispData_direct[300,1]
            Y_direct = [yi * 1000 for yi in dispData_direct[:,1]]
            if n == 0:
                axs.append(f.add_subplot(gs[0,:]))
            else:
                axs.append(f.add_subplot(gs[i,j])) 
            axs[-1].plot(exp_OC1[:,0],exp_OC1[:,1],linestyle="dashed",linewidth=0.5,color="blue")
            axs[-1].plot(X,Y,linewidth=1,color="red")
            axs[-1].plot(X_direct,Y_direct,linewidth=1.25,linestyle="dashdot",color="green")
            axs[-1].grid(linestyle='dotted')
            if j == 0:
                axs[-1].set_ylabel("Displacement (mm)")
            if i ==2 or i == 0:
                axs[-1].set_xlabel("time (s)")
            axs[-1].set_xlim([0,16])
            if n==1:
                axs[-1].set_ylim([-6,6])
            axs[-1].set_title(title,fontsize=13)
            if n == 1:
                axs[-1].legend(["EXP_{}{}".format(STR,loadlevel),"3DEC_Incremental","3DEC_Direct"],loc="lower left",prop={'size': 8})  
            else:
                axs[-1].legend(["EXP_{}{}".format(STR,loadlevel),"3DEC_Incremental","3DEC_Direct"],loc="lower right",prop={'size': 8}) 
            n +=1
            if n>4:
                findFlag=True
                break
        if findFlag:
            break
    f.tight_layout()
    plt.show()

def differentiate(loadlevel,STR,inc):
    ##MassProp 4 percent C_residual = 0
    data_folder="hist_softening_new_{}percent_mass_4percent".format(str(loadlevel))
    target_folder = "expcomparison_new_{}percent_mass_4percent_cumvsno".format(str(loadlevel))
    print(target_folder)
    isExist = os.path.exists(target_folder)
    tnstep = 1.25e-3
    time_slice = None
    if not isExist:
        os.makedirs(target_folder)
    time =np.genfromtxt(fname=os.path.join(data_folder,"TIME.txt"),skip_header=2)
    count=0
    print(tnstep*inc)
    exp_folder = "expresult_{}_{}".format(STR,str(loadlevel))
    acc=["ACC18-x","ACC18-y","ACC14-x","ACC14-y","ACC12-x","ACC12-y","ACC6-x","ACC6-y","ACC2-x","ACC2-y","OC1-y","OC2-x","OC2-y","OC4-x","OC4-y"]
    vel=["VEL18-x","VEL18-y","VEL14-x","VEL14-y","VEL12-x","VEL12-y","VEL6-x","VEL6-y","VEL2-x","VEL2-y","OC1-y","OC2-x","OC2-y","OC4-x","OC4-y"]
    count = 0
    for a in acc:
        file = os.path.join(exp_folder,"{}.txt".format(a))
        if loadLevel==75:
            exp_OC1 = np.loadtxt(fname=file,delimiter="\t",skiprows=1)
            exp_OC1[:,1] -= exp_OC1[3,1]
        else:
            exp_OC1 = np.loadtxt(fname=file,delimiter=" ",skiprows=1)
            exp_OC1[:,1] -= exp_OC1[3,1]
        title =  Path(file).stem
        print(title)
        if a.startswith("ACC"):
            num_data = os.path.join(data_folder,"{}.txt".format(vel[count]))
            vel18y= np.genfromtxt(fname=num_data,skip_header=2)
            if (time_slice):
                slicedTime = time[time[:,1] <= time_slice]
                index_time = len(slicedTime)
                num_OC1 = np.stack((slicedTime[:,1],vel18y[:index_time,1]),axis=1)
                exp_OC1_sliced = exp_OC1[exp_OC1[:,0] <= time_slice]
                index_exp_OC1_sliced = len(exp_OC1_sliced[:,0])
            else:
                index_time = len(time)
                num_OC1 = np.stack((time[:,1], vel18y[:,1]), axis=1)
                index_exp_OC1_sliced = len(exp_OC1[:,0])
            if inc ==1:
                acc18y = [(num_OC1[i,1]-num_OC1[i-inc,1])/(tnstep*inc) for i in range(1,len(num_OC1))]
                new_time = time[0:index_time:inc]
                acc18y.insert(0,0)
            else:
                acc18y = np.diff(vel18y[:index_time:inc,1])/(tnstep*inc)
                acc18y = np.insert(acc18y,0,0,axis=0)
                new_time = time[0:index_time:inc]
            acc18y_array = np.stack((new_time[:,1], acc18y[:]), axis=1)
            mult=1
        else:
            num_data = os.path.join(data_folder,"{}.txt".format(vel[count]))
            vel18y= np.genfromtxt(fname=num_data,skip_header=2)
            if (time_slice):
                slicedTime = time[time[:,1] <= time_slice]
                index_time = len(slicedTime)
                num_OC1 = np.stack((slicedTime[:,1],vel18y[:index_time,1]),axis=1)
                exp_OC1_sliced = exp_OC1[exp_OC1[:,0] <= time_slice]
                index_exp_OC1_sliced = len(exp_OC1_sliced[:,0])
            else:
                index_exp_OC1_sliced = len(exp_OC1[:,0])
                index_time = len(time)
                num_OC1 = np.stack((time[:,1], vel18y[:,1]), axis=1)
                index_exp_OC1_sliced = len(exp_OC1[:,0])
            acc18y_array = np.stack((time[:index_time,1], vel18y[:index_time,1]), axis=1)
            mult=1000
        fig, ax1 = plt.subplots()
        ax1.set_title(title)  
        #get maximum data points
        max_point = max(acc18y_array[:,1])
        min_point = min(acc18y_array[:,1])
        index_max = np.where(acc18y_array[:,1]==max_point)
        index_max_c = index_max[0][0]
        index_min = np.where(acc18y_array[:,1]==min_point)
        index_min_c = index_min[0][0]

        #get max data points exp
        max_point_exp = max(exp_OC1[:index_exp_OC1_sliced,1])
        min_point_exp = min(exp_OC1[:index_exp_OC1_sliced,1])
        index_max_exp = np.where(exp_OC1[:index_exp_OC1_sliced,1]==max_point_exp)
        index_max_exp_c = index_max_exp[0][0]
        index_min_exp = np.where(exp_OC1[:index_exp_OC1_sliced,1]==min_point_exp)
        index_min_exp_c = index_min_exp[0][0]

        ####annotate num model
        ax1.annotate("{}".format(str(round(max_point*mult,3))),xytext=(acc18y_array[index_max_c,0]+1.5,acc18y_array[index_max_c,1]*mult*0.75),xy=(acc18y_array[index_max_c,0],acc18y_array[index_max_c,1]*mult),arrowprops=dict(arrowstyle="->",color="red"),textcoords="data")
        ax1.annotate("{}".format(str(round(min_point*mult,3))),xytext=(acc18y_array[index_min_c,0]+1.5,acc18y_array[index_min_c,1]*mult*0.75),xy=(acc18y_array[index_min_c,0],acc18y_array[index_min_c,1]*mult),arrowprops=dict(arrowstyle="->",color="red"),textcoords="data")
        ax1.annotate("{}".format(str(round(max_point_exp,3))),xytext=(exp_OC1[index_max_exp_c,0]+1,exp_OC1[index_max_exp_c,1]),xy=(exp_OC1[index_max_exp_c,0],exp_OC1[index_max_exp_c,1]),arrowprops=dict(arrowstyle="->",color="blue"),textcoords="data")
        ax1.annotate("{}".format(str(round(min_point_exp,3))),xytext=(exp_OC1[index_min_exp_c,0]+1,exp_OC1[index_min_exp_c,1]),xy=(exp_OC1[index_min_exp_c,0],exp_OC1[index_min_exp_c,1]),arrowprops=dict(arrowstyle="->",color="blue"),textcoords="data")
        ax1.plot(acc18y_array[:,0],acc18y_array[:,1]*mult,linewidth=1,color="red")
        if (time_slice):
            ax1.plot(exp_OC1[:index_exp_OC1_sliced,0],exp_OC1[:index_exp_OC1_sliced,1],linewidth=1,color="blue")
        else:
            ax1.plot(exp_OC1[:,0],exp_OC1[:,1],linestyle="dashed",linewidth=0.5,color="blue")
        
        
        ax1.legend(["3DEC_POST","EXP_{}{}".format(STR,loadlevel)],loc="lower right",prop={'size': 9})
        
        if a.startswith("ACC"):
            ax1.set_ylabel("Acceleration (m/s2)")
        else:
            ax1.set_ylabel("Displacement (mm)")
        ax1.set_xlabel("dyna time (s)")
        
        if time_slice:
            ax1.set_xlim([0,time_slice])
        else:
            ax1.set_xlim([0,16])
            ax1.grid(linestyle='dotted')
        count+=1
        
        plt.savefig("{}/{}.png".format(target_folder,title))
    pass

def differentiate_blind(loadlevel,STR,inc):
    ##MassProp 4 percent C_residual = 0
    data_folder="prediction-model-UNS".format(str(loadlevel))
    target_folder = "expcomparison_new_{}percent_mass_6percent_blind".format(str(loadlevel))
    print(target_folder)
    isExist = os.path.exists(target_folder)
    tnstep = 7.5e-4
    time_slice = None
    time_slice_min = None
    if not isExist:
        os.makedirs(target_folder)
    time =np.genfromtxt(fname=os.path.join(data_folder,"TIME_{}.txt".format(loadLevel)),skip_header=8000)
    count=0
    print(tnstep*inc)
    exp_folder = "expresult_{}_{}".format(STR,str(loadlevel))
    acc=["ACC18-x","ACC18-y","ACC14-x","ACC14-y","ACC12-x","ACC12-y","ACC6-x","ACC6-y","ACC2-x","ACC2-y","OC1-y","OC2-x","OC2-y","OC4-x","OC4-y"]
    vel=["VEL18x_{}".format(loadLevel),"VEL18y_{}".format(loadLevel),"VEL14x_{}".format(loadLevel),"VEL14y_{}".format(loadLevel),"VEL12x_{}".format(loadLevel),"VEL12y_{}".format(loadLevel),"VEL6x_{}".format(loadLevel),"VEL6y_{}".format(loadLevel),"VEL2x_{}".format(loadLevel),"VEL2y_{}".format(loadLevel),"OC1y_{}".format(loadLevel),"OC2x_{}".format(loadLevel),"OC2y_{}".format(loadLevel),"OC4x_{}".format(loadLevel),"OC4y_{}".format(loadLevel)]
    count = 0
    for a in acc:
        file = os.path.join(exp_folder,"{}.txt".format(a))
        if loadLevel==75:
            exp_OC1 = np.loadtxt(fname=file,delimiter="\t",skiprows=1)
            exp_OC1[:,1] -= exp_OC1[3,1]
        else:
            exp_OC1 = np.loadtxt(fname=file,delimiter=" ",skiprows=1)
            exp_OC1[:,1] -= exp_OC1[3,1]
        title =  Path(file).stem
        print(title)
        if a.startswith("ACC"):
            num_data = os.path.join(data_folder,"{}.txt".format(vel[count]))
            vel18y= np.genfromtxt(fname=num_data,skip_header=8000)
            vel18y[:,1] -= vel18y[0,1]
            if (time_slice):
                slicedTime = time[time[:,1] <= time_slice]
                index_time = len(slicedTime)
                num_OC1 = np.stack((slicedTime[:,1],vel18y[:index_time,1]),axis=1)
                exp_OC1_sliced = exp_OC1[np.logical_and(exp_OC1[:,0] <= time_slice,exp_OC1[:,0] >= time_slice_min)]
                exp_OC1_sliced[:,0] -= exp_OC1_sliced[0,0]
                exp_OC1_sliced[:,1] -= exp_OC1_sliced[0,1]
                index_exp_OC1_sliced = len(exp_OC1_sliced[:,0])
            else:
                index_time = len(time)
                num_OC1 = np.stack((time[:,1], vel18y[:,1]), axis=1)
                index_exp_OC1_sliced = len(exp_OC1[:,0])
            if inc ==1:
                acc18y = [(num_OC1[i,1]-num_OC1[i-inc,1])/(tnstep*inc) for i in range(1,len(num_OC1))]
                new_time = time[0:index_time:inc]
                acc18y.insert(0,0)
            else:
                acc18y = np.diff(vel18y[:index_time:inc,1])/(tnstep*inc)
                acc18y = np.insert(acc18y,0,0,axis=0)
                new_time = time[0:index_time:inc]
            acc18y_array = np.stack((new_time[:,1], acc18y[:]), axis=1)
            mult=1
        else:
            num_data = os.path.join(data_folder,"{}.txt".format(vel[count]))
            vel18y= np.genfromtxt(fname=num_data,skip_header=8000)
            vel18y[:,1] -= vel18y[0,1]
            if (time_slice):
                slicedTime = time[time[:,1] <= time_slice]
                index_time = len(slicedTime)
                num_OC1 = np.stack((slicedTime[:,1],vel18y[:index_time,1]),axis=1)
                exp_OC1_sliced = exp_OC1[np.logical_and(exp_OC1[:,0] <= time_slice,exp_OC1[:,0] >= time_slice_min)]
                exp_OC1_sliced[:,0] -= exp_OC1_sliced[0,0]
                exp_OC1_sliced[:,1] -= exp_OC1_sliced[0,1]
                index_exp_OC1_sliced = len(exp_OC1_sliced[:,0])
            else:
                index_exp_OC1_sliced = len(exp_OC1[:,0])
                index_time = len(time)
                num_OC1 = np.stack((time[:,1], vel18y[:,1]), axis=1)
                index_exp_OC1_sliced = len(exp_OC1[:,0])
            acc18y_array = np.stack((time[:index_time,1], vel18y[:index_time,1]), axis=1)
            mult=1000
        fig, ax1 = plt.subplots()
        ax1.set_title(title)  
        #get maximum data points
        max_point = max(acc18y_array[:,1])
        min_point = min(acc18y_array[:,1])
        index_max = np.where(acc18y_array[:,1]==max_point)
        index_max_c = index_max[0][0]
        index_min = np.where(acc18y_array[:,1]==min_point)
        index_min_c = index_min[0][0]

        #get max data points exp
        if(time_slice):
            max_point_exp = max(exp_OC1_sliced[:,1])
            min_point_exp = min(exp_OC1_sliced[:,1])
            index_max_exp = np.where(exp_OC1_sliced[:,1]==max_point_exp)
            index_max_exp_c = index_max_exp[0][0]
            index_min_exp = np.where(exp_OC1_sliced[:,1]==min_point_exp)
            index_min_exp_c = index_min_exp[0][0]
        else:
            max_point_exp = max(exp_OC1[:index_exp_OC1_sliced,1])
            min_point_exp = min(exp_OC1[:index_exp_OC1_sliced,1])
            index_max_exp = np.where(exp_OC1[:index_exp_OC1_sliced,1]==max_point_exp)
            index_max_exp_c = index_max_exp[0][0]
            index_min_exp = np.where(exp_OC1[:index_exp_OC1_sliced,1]==min_point_exp)
            index_min_exp_c = index_min_exp[0][0]

        ####annotate num model
        ax1.annotate("{}".format(str(round(max_point*mult*-1,3))),xytext=(acc18y_array[index_max_c,0]+1.5,acc18y_array[index_max_c,1]*mult*-1),xy=(acc18y_array[index_max_c,0],acc18y_array[index_max_c,1]*mult*-1),arrowprops=dict(arrowstyle="->",color="red"),textcoords="data")
        ax1.annotate("{}".format(str(round(min_point*mult*-1,3))),xytext=(acc18y_array[index_min_c,0]+1.5,acc18y_array[index_min_c,1]*mult*-1),xy=(acc18y_array[index_min_c,0],acc18y_array[index_min_c,1]*mult*-1),arrowprops=dict(arrowstyle="->",color="red"),textcoords="data")
        if(time_slice):
            ax1.annotate("{}".format(str(round(max_point_exp,3))),xytext=(exp_OC1_sliced[index_max_exp_c,0]+1,exp_OC1_sliced[index_max_exp_c,1]),xy=(exp_OC1_sliced[index_max_exp_c,0],exp_OC1_sliced[index_max_exp_c,1]),arrowprops=dict(arrowstyle="->",color="blue"),textcoords="data")
            ax1.annotate("{}".format(str(round(min_point_exp,3))),xytext=(exp_OC1_sliced[index_min_exp_c,0]+1,exp_OC1_sliced[index_min_exp_c,1]),xy=(exp_OC1_sliced[index_min_exp_c,0],exp_OC1_sliced[index_min_exp_c,1]),arrowprops=dict(arrowstyle="->",color="blue"),textcoords="data")
        else:
            ax1.annotate("{}".format(str(round(max_point_exp,3))),xytext=(exp_OC1[index_max_exp_c,0]+1,exp_OC1[index_max_exp_c,1]),xy=(exp_OC1[index_max_exp_c,0],exp_OC1[index_max_exp_c,1]),arrowprops=dict(arrowstyle="->",color="blue"),textcoords="data")
            ax1.annotate("{}".format(str(round(min_point_exp,3))),xytext=(exp_OC1[index_min_exp_c,0]+1,exp_OC1[index_min_exp_c,1]),xy=(exp_OC1[index_min_exp_c,0],exp_OC1[index_min_exp_c,1]),arrowprops=dict(arrowstyle="->",color="blue"),textcoords="data")
        ax1.plot(acc18y_array[:,0],acc18y_array[:,1]*mult*-1,linewidth=1,color="red")
        if (time_slice):
            ax1.plot(exp_OC1_sliced[:,0],exp_OC1_sliced[:,1],linewidth=1,color="blue")
        else:
            ax1.plot(exp_OC1[:,0],exp_OC1[:,1],linestyle="dashed",linewidth=0.5,color="blue")
        
        
        ax1.legend(["3DEC_PRE","EXP_{}{}".format(STR,loadlevel)],loc="lower right",prop={'size': 9})
        
        if a.startswith("ACC"):
            ax1.set_ylabel("Acceleration (m/s2)")
        else:
            ax1.set_ylabel("Displacement (mm)")
        ax1.set_xlabel("dyna time (s)")
        
        if time_slice:
            ax1.set_xlim([0,time_slice])
        else:
            ax1.set_xlim([0,16])
            ax1.grid(linestyle='dotted')
        count+=1
        
        plt.savefig("{}/{}.png".format(target_folder,title))
    pass

def damping_ratio_bar(loadlevel,STR,inc):
    data_folder_1="hist_softening_new_{}percent_mass_4percent".format(str(loadlevel))
    ##Uncomment this line if you want to plot the direct displacement
    data_folder_2 = "hist_softening_75percent_mass_3percent"
    pass

if __name__ == "__main__":
    #maxwell_check()
    parser = argparse.ArgumentParser(description="python file to plot the displacement and acceleration response")
    parser.add_argument("-l","--load_level", help="Input your load level",required=True,type=int)
    parser.add_argument("-s","--strength", help="Input STR/UNS for strengthened/unstrengthened",required=True,type=str)
    parser.add_argument("-i","--inc", help="Input increment level for velocity differentiation",required=True,type=int)
    args = parser.parse_args()
    loadLevel = args.load_level
    _str = args.strength
    inc = args.inc
    #differentiate(loadlevel=loadLevel,STR=_str,inc=inc)
    #differentiate_blind(loadlevel=loadLevel,STR=_str,inc=inc)
    multfigure_dep(loadlevel=loadLevel,STR=_str,inc=inc)
    #multiFigureDisp(loadlevel=loadLevel,STR=_str,inc=inc)
    #multiFigureAcc(loadlevel=loadLevel,STR=_str,inc=inc)
