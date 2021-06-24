import numpy as np
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

    X = np.arange(-((len(lanes)/2)-.5), (len(lanes)/2)+.5)
    #Fixes thread error: https://stackoverflow.com/questions/14694408/runtimeerror-main-thread-is-not-in-main-loop
    plt.switch_backend('agg')

    plt.suptitle('Galton Board')
    plt.bar(X + 0.00, lanes, width=0.25)

    #Gives the png a unique name
    route = str(abs(hash(datetime.now())))
    plt.savefig('static/imgs/'+route+'.png')
    return lanes,route