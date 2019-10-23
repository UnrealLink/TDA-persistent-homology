import numpy as np
import matplotlib.pyplot as plt

def plot_barcode(barcode, min_length=0, arrow_size=1, log_scale=False):
    dim1 = [x for x in barcode if x[0] == 0 and (x[2] == -1 or x[2] - x[1] > min_length)]
    dim2 = [x for x in barcode if x[0] == 1 and (x[2] == -1 or x[2] - x[1] > min_length)]
    dim3 = [x for x in barcode if x[0] == 2 and (x[2] == -1 or x[2] - x[1] > min_length)]
    xmax1 = np.max(np.array(dim1)[:,2]) if len(dim1) > 0 else 0
    xmax2 = np.max(np.array(dim2)[:,2]) if len(dim2) > 0 else 0
    xmax3 = np.max(np.array(dim3)[:,2]) if len(dim3) > 0 else 0
    xmax = np.max([xmax1, xmax2, xmax3])
    xmin1 = np.max(np.array(dim1)[:,2]) if len(dim1) > 0 else 0
    xmin2 = np.max(np.array(dim2)[:,2]) if len(dim2) > 0 else 0
    xmin3 = np.max(np.array(dim3)[:,2]) if len(dim3) > 0 else 0
    xmin = np.max([xmin1, xmin2, xmin3])

    ax1 = plt.subplot(311)
    y = 6
    dy = 5/(len(dim1)+1)
    for x in dim1:
        if x[2] == -1:
            ax1.arrow(x[1], y, xmax*0.95+arrow_size-x[1], 0, head_width=0.5, head_length=arrow_size*xmax/20, fc='b', ec='b')
        else:
            ax1.plot([x[1], x[2]], [y, y], 'b.-')
        y-=dy
    ax1.set_xlim(0, xmax+arrow_size)
    ax1.set_ylim(0, 7)

    ax2 = plt.subplot(312, sharex=ax1, sharey=ax1)
    y = 6
    dy = 5/(len(dim2)+1)
    for x in dim2:
        if x[2] == -1:  
            ax2.arrow(x[1], y, xmax*0.95+arrow_size-x[1], 0, head_width=0.5, head_length=arrow_size*xmax/20, fc='b', ec='b')
        else:
            ax2.plot([x[1], x[2]], [y, y], 'b.-')
        y-=dy
    
    ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
    y = 6
    dy = 5/(len(dim3)+1)
    for x in dim3:
        if x[2] == -1:
            ax3.arrow(x[1], y, xmax*0.95+arrow_size-x[1], 0, head_width=0.5, head_length=arrow_size*xmax/20, fc='b', ec='b')
        else:
            ax3.plot([x[1], x[2]], [y, y], 'b.-')
        y-=dy

    plt.tight_layout()
    plt.show()