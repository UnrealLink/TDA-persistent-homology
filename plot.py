import numpy as np
import matplotlib.pyplot as plt

def plot_barcode(barcode):
    dim1 = [x for x in barcode if x[0] == 0]
    dim2 = [x for x in barcode if x[0] == 1]
    dim3 = [x for x in barcode if x[0] == 2]
    xmax = np.max(np.array(barcode)[:,2])

    ax1 = plt.subplot(311)
    y = 1
    dy = 5/len(dim1)
    for x in dim1:
        if x[2] == -1:
            ax1.arrow(x[1], y, xmax*0.95+1-x[1], 0, head_width=0.5, head_length=xmax/20, fc='b', ec='b')
        else:
            ax1.plot([x[1], x[2]], [y, y], 'b-')
        y+=dy
    ax1.set_xlim(0, xmax+1)
    ax1.set_ylim(0, 6)

    ax2 = plt.subplot(312, sharex=ax1, sharey=ax1)
    y = 1
    dy = 5/len(dim2)
    for x in dim2:
        if x[2] == -1:  
            ax2.arrow(x[1], y, xmax*0.95+1-x[1], 0, head_width=0.5, head_length=xmax/20, fc='b', ec='b')
        else:
            ax2.plot([x[1], x[2]], [y, y], 'b-')
        y+=dy
    
    ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
    y = 1
    dy = 5/len(dim3)
    for x in dim3:
        if x[2] == -1:
            ax3.arrow(x[1], y, xmax*0.95+1-x[1], 0, head_width=0.5, head_length=xmax/20, fc='b', ec='b')
        else:
            ax3.plot([x[1], x[2]], [y, y], 'b-')
        y+=dy

    plt.tight_layout()
    plt.show()