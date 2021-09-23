
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
from datetime import datetime
from random import randint

def galtonboard(levels):
    lanes = [0]*(levels)
    for h in range((levels)**2*100):
        stored = -1
        for j in range(levels):
            stored += randint(0, 1)
        lanes[stored] += 1

    if len(lanes)%2==0:
        X = np.arange(-((len(lanes)/2)-1), (len(lanes)/2)+1)
    else:
        X = np.arange(-((len(lanes)/2)-.5), (len(lanes)/2)+.5)
    #Fixes thread error: https://stackoverflow.com/questions/14694408/runtimeerror-main-thread-is-not-in-main-loop
    plt.switch_backend('agg')

    plt.suptitle('Galton Board')
    plt.bar(X + 0.00, lanes, width=0.25)

    # Deletes older boards images
    files = glob.glob('static/imgs/*.png')
    for f in files:
        os.remove(f)

    #Gives the png a unique name
    name = str(abs(hash(datetime.now())))

    # Checks if the images will be saved where we think
    dir_path=str(os.path.dirname(os.path.realpath(__file__)))
    print("dir_path: "+dir_path)
    route=dir_path+'/../static/imgs/'+str(name)+'.png'
    plt.savefig(route)
    print("route: "+route)
    print("image saved")
    return lanes,route
