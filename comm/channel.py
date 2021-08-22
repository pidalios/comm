import random
import numpy as np

def awgnChannel(thelist,snr):
    # SNR = Es/No
    output = []
    E_avg = sum(np.abs(thelist)**2)/len(thelist)
    SNR_linear = 10**(snr/10)
    sigma = np.sqrt(E_avg/(2*SNR_linear))
    for i in range(0,len(thelist)):
            noise_x = sigma*random.gauss(0,1)
            noise_y = sigma*random.gauss(0,1)
            noisySig = thelist[i] + complex(noise_x,noise_y)
            output.append(noisySig)
    return output
