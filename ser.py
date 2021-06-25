from comm import channel, mod
import random
import numpy as np
from scipy import integrate, special as sp
import matplotlib.pyplot as plt
import sys

class rxList():
    def __init__(self):
        rxList.modType = ''
        rxList.simulation = []
        rxList.theoretical = []
        
def BPSKBlock(N, rxList) -> None:
    data = mod.getSource(N, 'BPSK')
    modSig = mod.getModulator(data, 'BPSK')
    serList = []
    theoSER = []
    for i in range(0, 11):
        chSig = channel.awgnChannel(modSig, i)
        deSig = mod.BPSKDemodulator(chSig)
        NumSymbolError = mod.symerr(data, deSig)
        ser = NumSymbolError/N
        serList.append(ser)

        # Theorical SER value
        snrLinear = 10**(i/10)
        theoSER.append(0.5*sp.erfc(np.sqrt(snrLinear)))

    rxList.modType = 'BPSK'
    rxList.simulation = serList
    rxList.theoretical = theoSER
    
def QPSKBlock(N, rxList) -> None:
    data = mod.getSource(N, 'QPSK')
    modSig = mod.getModulator(data, 'QPSK')
    serList = []
    theoSER = []
    for i in range(0, 11):
        chSig = channel.awgnChannel(modSig, i)
        deSig = mod.QPSKDemodulator(chSig)
        NumSymbolError = mod.symerr(data, deSig)
        ser = NumSymbolError/N
        serList.append(ser)

        # Theorical SER value
        snrLinear = 10**(i/10)
        theoSER.append(sp.erfc(np.sqrt(snrLinear/2))-(0.5*sp.erfc(np.sqrt(snrLinear/2)))**2)

    rxList.modType = 'QPSK'
    rxList.simulation = serList
    rxList.theoretical = theoSER

def PSK8Block(N, rxList) -> None:
    data = mod.getSource(N, '8PSK')
    modSig = mod.getModulator(data, '8PSK')
    serList = []
    theoSER = []
    for i in range(0, 11):
        chSig = channel.awgnChannel(modSig, i)
        deSig = mod.PSK8Demodulator(chSig)
        NumSymbolError = mod.symerr(data, deSig)
        ser = NumSymbolError/N
        serList.append(ser)

        # Theorical SER value
        pi = np.pi
        snrLinear = 10**(i/10)
        f = lambda x: (1/pi)*np.exp(-snrLinear*((np.sin(pi/8)/np.sin(x+pi/8))**2))
        serTheo = integrate.quad(f, 0, pi-pi/8)
        theoSER.append(serTheo[0])

    rxList.modType = '8PSK'
    rxList.simulation = serList
    rxList.theoretical = theoSER

def QAM16Block(N, rxList) -> None:
    data = mod.getSource(N, '16QAM')
    modSig = mod.getModulator(data, '16QAM')
    serList = []
    theoSER = []
    for i in range(0, 11):
        chSig = channel.awgnChannel(modSig, i)
        deSig = mod.QAM16Demodulator(chSig)
        NumSymbolError = mod.symerr(data, deSig)
        ser = NumSymbolError/N
        serList.append(ser)

        # Theorical SER value
        snrLinear = 10**(i/10)
        P_sc = (3/4)*sp.erfc(np.sqrt((0.1*snrLinear)))
        theoSER.append(1-(1-P_sc)**2)

    rxList.modType = '16QAM'
    rxList.simulation = serList
    rxList.theoretical = theoSER

def plotSER(rxList) -> None:
    x = np.arange(0, 11, 1)
    plt.plot(x, rxList.simulation, marker='o', label=rxList.modType+' simulation')
    plt.plot(x, rxList.theoretical, marker='^', label=rxList.modType+' theoretical')
    plt.legend()
    plt.xticks(x)
    plt.yscale('log')
    plt.grid(True, which='both')
    plt.title('{:s} SER'.format(rxList.modType))
    plt.xlabel('SNR (dB)')
    plt.ylabel('SER')
    plt.show()

def plotAll(list1, list2, list3, list4) -> None:
    x = np.arange(0, 11, 1)
    plt.plot(x, list1.simulation, marker='o', label=list1.modType+' simulation')
    plt.plot(x, list2.simulation, marker='^', label=list2.modType+' simulation')
    plt.plot(x, list3.simulation, marker='p', label=list3.modType+' simulation')
    plt.plot(x, list4.simulation, marker='P', label=list4.modType+' simulation')
    plt.legend()
    plt.xticks(x)
    plt.yscale('log')
    plt.grid(True, which='both')
    plt.title('SER comparison')
    plt.xlabel('SNR (dB)')
    plt.ylabel('SER')
    plt.show()

def interface() -> None:
    N = int(input('Input number of symbols: '))
    flag = input('Input modulation type: ')
    ModList = rxList()
    if flag=='BPSK' or flag=='bpsk':
        BPSKBlock(N, ModList)
        plotSER(ModList)
    elif flag=='QPSK' or flag=='qpsk':
        QPSKBlock(N, ModList)
        plotSER(ModList)
    elif flag=='8PSK' or flag=='8psk':
        PSK8Block(N, ModList)
        plotSER(ModList)
    elif flag=='16QAM' or flag=='16qam':
        QAM16Block(N, ModList)
        plotSER(ModList)
    elif flag=='ALL' or flag=='all':
        BPSK = rxList()
        QPSK = rxList()
        PSK8 = rxList()
        QAM16 = rxList()
        BPSKBlock(N, BPSK)
        QPSKBlock(N, QPSK)
        PSK8Block(N, PSK8)
        QAM16Block(N, QAM16)
        plotAll(BPSK, QPSK, PSK8, QAM16)
    else:
        print('Error')
        sys.exit(0)

def main() -> None:
    interface()

if __name__=='__main__':
    main()
