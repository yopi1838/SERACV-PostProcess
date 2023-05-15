import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

def animate(i):
    #erase previous plot
    ax.cla()
    ax.plot(datfile[:i+1,0],datfile[:i+1,1],linestyle="-",color="blue")
    ax.relim()
    ax.autoscale_view()
    ax.ticklabel_format(axis="y",style="sci")
    ax.set_xlabel("dyna time (s)")
    ax.set_ylabel("velocity (m/s)")
    # if datfile[i+1,1] < 0.05 or datfile[i+1,1] > -0.05:
    #     ax.set_ylim(-0.05,0.05)
    # else:
    #     ax.set_ylim(-0.2,0.2)
    
    ax.plot(datfile[i,0],datfile[i,1],marker = 'o', markerfacecolor = 'red', markeredgecolor = 'red',markersize=3)
    ax.set_xlim(0,16)
    

if __name__ == "__main__":
    #Text file data converted into float
    datfile = np.loadtxt("input_vel_trunc.txt",dtype=float,skiprows=1)
    fig,ax = plt.subplots(figsize=(7,5))
    # define the animation
    ani = FuncAnimation(fig = fig, func = animate, frames = len(datfile))
    FFwriter = FFMpegWriter(fps=30)
    ani.save("animate_mscale1e-6_2.mp4",writer=FFwriter)