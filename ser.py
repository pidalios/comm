import argparse
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
    plt.title('{:s} Simulation and Theoritical SER Comparison'.format(rxList.modType))
    plt.xlabel('SNR (dB)')
    plt.ylabel('Error Rate')
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
    plt.title('SER Comparison of Modulations in AWGN Channel')
    plt.xlabel('SNR (dB)')
    plt.ylabel('Error Rate')
    plt.show()

def parse_args():
    parser = argparse.ArgumentParser(description='SER performance comparison.')
    parser.add_argument("-n", "--N", default=10000, type=int, help='Number of symbols.', metavar='')
    parser.add_argument('-m', '--ModType', default='QPSK', type=str.lower, help='Modulation type.', metavar='')
    return parser.parse_args()

def main(args) -> None:
    ModList = rxList()
    if args.ModType=='bpsk':
        BPSKBlock(args.N, ModList)
        plotSER(ModList)
    elif args.ModType=='qpsk':
        QPSKBlock(args.N, ModList)
        plotSER(ModList)
    elif args.ModType=='8psk':
        PSK8Block(args.N, ModList)
        plotSER(ModList)
    elif args.ModType=='16qam':
        QAM16Block(args.N, ModList)
        plotSER(ModList)
    elif args.ModType=='all':
        BPSK = rxList()
        QPSK = rxList()
        PSK8 = rxList()
        QAM16 = rxList()
        BPSKBlock(args.N, BPSK)
        QPSKBlock(args.N, QPSK)
        PSK8Block(args.N, PSK8)
        QAM16Block(args.N, QAM16)
        plotAll(BPSK, QPSK, PSK8, QAM16)
    else:
        print('Error')
        sys.exit(0)

if __name__=='__main__':
    args = parse_args()
    main(args)
