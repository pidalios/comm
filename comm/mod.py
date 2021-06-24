import numpy as np
import random as rd
import sys

# Get Functions
def getModulator(thelist,modType):
    if modType == 'BPSK' or modType == '2PSK' or modType == 'bpsk':
        return BPSKModulator(thelist)
    elif modType == 'QPSK' or modType == '4PSK' or modType == 'qpsk':
        return QPSKModulator(thelist)
    elif modType == '8PSK' or modType == '8psk':
        return PSK8Modulator(thelist)
    elif modType == '16QAM' or modType == '16qam':
        return QAM16Modulator(thelist)
    else:
        print('The modulation type "{:s}" is not defined.'.format(modType))
        sys.exit(0)



def getDemodulator(thelist,modType):
    if modType == 'BPSK' or modType == '2PSK' or modType == 'bpsk':
        return BPSKDemodulator(thelist)
    elif modType == 'QPSK' or modType == '4PSK' or modType == 'qpsk':
        return QPSKDemodulator(thelist)
    elif modType == '8PSK' or modType == '8psk':
        return PSK8Demodulator(thelist)
    elif modType == '16QAM' or modType == '16qam':
        return QAM16Demodulator(thelist)
    else:
        print('The modulation type "{:s}" is not defined.'.format(modType))
        sys.exit(0)



def getSource(N,modType):
    output = []
    if modType == 'BPSK' or modType == '2PSK' or modType == 'bpsk':
        M = 2
        for i in range(0,N):
                output.append(rd.randint(0,M-1))
        return output
    elif modType == 'QPSK' or modType == '4PSK' or modType == 'qpsk':
        M = 4
        for i in range(0,N):
                output.append(rd.randint(0,M-1))
        return output
    elif modType == '8PSK' or modType == '8psk':
        M = 8
        for i in range(0,N):
                output.append(rd.randint(0,M-1))
        return output
    elif modType == '16QAM' or modType == '16qam':
        M = 16
        for i in range(0,N):
                output.append(rd.randint(0,M-1))
        return output
    else:
        print('The modulation type "{:s}" is not defined.'.format(modType))
        sys.exit(0)
		

# Modulators
def BPSKModulator(thelist):
    output = []
    for i in range(0,len(thelist)):
        if thelist[i] == 0:
            output.append(1)
        elif thelist[i] == 1:
            output.append(-1)
        else:
            print("The symbol range is in [0, 1]. Please try again.")
            sys.exit()
    return output

def BPSKDemodulator(thelist):
    output =[]
    real_part = [x.real for x in thelist]
    for i in range(0,len(thelist)):
        if real_part[i] >= 0:
            output.append(0)
        else:
            output.append(1)
    return output

def QPSKModulator(thelist):
    output = []
    for i in range(0,len(thelist)):
        if thelist[i] == 0:
            output.append(complex(np.cos(np.pi/4),np.sin(np.pi/4)))
        elif thelist[i] == 1:
            output.append(complex(np.cos(3*np.pi/4),np.sin(3*np.pi/4)))
        elif thelist[i] == 2:
            output.append(complex(np.cos(7*np.pi/4),np.sin(7*np.pi/4)))
        elif thelist[i] == 3:
            output.append(complex(np.cos(5*np.pi/4),np.sin(5*np.pi/4)))
        else:
            print("The symbol range is in [0, 3]. Please try again.")
            sys.exit()
    return output

def QPSKDemodulator(thelist):
    output =[]
    real_part = [x.real for x in thelist]
    imag_part = [x.imag for x in thelist]
    for i in range(0,len(thelist)):
        if real_part[i] >= 0 and imag_part[i] >= 0:
            output.append(0)
        elif real_part[i] < 0 and imag_part[i] >= 0:
            output.append(1)
        elif real_part[i] < 0 and imag_part[i] < 0:
            output.append(3)
        elif real_part[i] >= 0 and imag_part[i] < 0:
            output.append(2)
    return output

def PSK8Modulator(thelist):
    output = []
    for i in range(0,len(thelist)):
        if thelist[i] == 0:
            output.append(complex(np.cos(0),np.sin(0)))
        elif thelist[i] == 1:
            output.append(complex(np.cos(2*np.pi/8),np.sin(2*np.pi/8)))
        elif thelist[i] == 3:
            output.append(complex(np.cos(4*np.pi/8),np.sin(4*np.pi/8)))
        elif thelist[i] == 2:
            output.append(complex(np.cos(6*np.pi/8),np.sin(6*np.pi/8)))
        elif thelist[i] == 6:
            output.append(complex(np.cos(8*np.pi/8),np.sin(8*np.pi/8)))
        elif thelist[i] == 7:
            output.append(complex(np.cos(10*np.pi/8),np.sin(10*np.pi/8)))
        elif thelist[i] == 5:
            output.append(complex(np.cos(12*np.pi/8),np.sin(12*np.pi/8)))
        elif thelist[i] == 4:
            output.append(complex(np.cos(14*np.pi/8),np.sin(14*np.pi/8)))
        else:
            print("The symbol range is in [0, 7]. Please try again.")
            sys.exit()
    return output

def PSK8Demodulator(thelist):
    output =[]
    real_part = [x.real for x in thelist]
    imag_part = [x.imag for x in thelist]
    a = np.cos(np.pi/8)
    b = np.sin(np.pi/8)
    for i in range(0,len(thelist)):
        if -b*real_part[i]+a*imag_part[i] < 0 and -b*real_part[i]-a*imag_part[i] < 0:
            output.append(0)
        elif a*real_part[i]-b*imag_part[i] >= 0 and (-b*real_part[i]+a*imag_part[i]) >= 0:
            output.append(1)
        elif (a*real_part[i]+b*imag_part[i]) >= 0 and (a*real_part[i]-b*imag_part[i]) < 0:
            output.append(3)
        elif (a*real_part[i]+b*imag_part[i]) < 0 and (-b*real_part[i]-a*imag_part[i]) < 0:
            output.append(2)
        elif (-b*real_part[i]-a*imag_part[i]) >= 0 and (-b*real_part[i]+a*imag_part[i]) >= 0:
            output.append(6)
        elif (-b*real_part[i]+a*imag_part[i]) < 0 and (a*real_part[i]-b*imag_part[i]) < 0:
            output.append(7)
        elif (a*real_part[i]-b*imag_part[i]) >= 0 and (a*real_part[i]+b*imag_part[i]) < 0:
            output.append(5)
        elif (a*real_part[i]+b*imag_part[i]) >= 0 and (-b*real_part[i]-a*imag_part[i]) >= 0:
            output.append(4)
    return output

def QAM16Modulator(thelist):
    output = []
    for i in range(0,len(thelist)):
        if thelist[i] == 0:
            output.append(complex(1,1))
        elif thelist[i] == 1:
            output.append(complex(3,1))
        elif thelist[i] == 2:
            output.append(complex(1,3))
        elif thelist[i] == 3:
            output.append(complex(3,3))
        elif thelist[i] == 4:
            output.append(complex(-1,1))
        elif thelist[i] == 5:
            output.append(complex(-3,1))
        elif thelist[i] == 6:
            output.append(complex(-1,3))
        elif thelist[i] == 7:
            output.append(complex(-3,3))
        elif thelist[i] == 8:
            output.append(complex(1,-1))
        elif thelist[i] == 9:
            output.append(complex(3,-1))
        elif thelist[i] == 10:
            output.append(complex(1,-3))
        elif thelist[i] == 11:
            output.append(complex(3,-3))
        elif thelist[i] == 12:
            output.append(complex(-1,-1))
        elif thelist[i] == 13:
            output.append(complex(-3,-1))
        elif thelist[i] == 14:
            output.append(complex(-1,-3))
        elif thelist[i] == 15:
            output.append(complex(-3,-3))
        else:
           print("The symbol range is in [0, 15]. Please try again.")
           sys.exit()
    return output

def QAM16Demodulator(thelist):
    output =[]
    real_part = [x.real for x in thelist]
    imag_part = [x.imag for x in thelist]
    for i in range(0,len(thelist)):
        if real_part[i] >= 0 and imag_part[i] >= 0 and real_part[i] < 2 and imag_part[i] < 2:
            output.append(0)
        elif real_part[i] >= 2 and imag_part[i] >= 0 and imag_part[i] < 2:
            output.append(1)
        elif imag_part[i] >= 2 and real_part[i] >= 0 and real_part[i] < 2:
            output.append(2)
        elif real_part[i] >= 2 and imag_part[i] >= 2:
            output.append(3)
        elif real_part[i] < 0 and imag_part[i] >= 0 and real_part[i] >= -2 and imag_part[i] < 2:
            output.append(4)
        elif real_part[i] < -2 and imag_part[i] >= 0 and imag_part[i] < 2:
            output.append(5)
        elif imag_part[i] >= 2 and real_part[i] < 0 and real_part[i] >= -2:
            output.append(6)
        elif real_part[i] < -2 and imag_part[i] >= 2:
            output.append(7)
        elif real_part[i] >= 0 and imag_part[i] < 0 and real_part[i] < 2 and imag_part[i] >= -2:
            output.append(8)
        elif real_part[i] >= 2 and imag_part[i] < 0 and imag_part[i] >= -2:
            output.append(9)
        elif imag_part[i] < -2 and real_part[i] >= 0 and real_part[i] < 2:
            output.append(10)
        elif real_part[i] >= 2 and imag_part[i] < -2:
            output.append(11)
        elif real_part[i] < 0 and imag_part[i] < 0 and real_part[i] >= -2 and imag_part[i] >= -2:
            output.append(12)
        elif real_part[i] < -2 and imag_part[i] < 0 and imag_part[i] >= -2:
            output.append(13)
        elif imag_part[i] < -2 and real_part[i] < 0 and real_part[i] >= -2:
            output.append(14)
        elif real_part[i] < -2 and imag_part[i] < -2:
            output.append(15)
    return output



# Symbol error
def symerr(listA,listB):	
    if len(listA) != len(listB):
        print('Error')
    else:
        count = 0
        for i in range(0,len(listA)):
            if listA[i] != listB[i]:
                count += 1
        return count







