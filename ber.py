#import channel
#import mod
from comm import channel, mod
import random
import numpy as np
from scipy import special as sp
from scipy import integrate
import matplotlib.pyplot as plt

N = 100000

d1 = mod.getSource(N,'BPSK')
sig1 = mod.getModulator(d1,'BPSK')
x = []
BPSK = []
#theoBPSK =[]
for i in range(0,11):
	x.append(i)
	tx1 = channel.awgnChannel(sig1,i)
	rx1 = mod.BPSKDemodulator(tx1)
	s1 = mod.symerr(d1,rx1)
	ber1 = s1/N
	BPSK.append(ber1)
	'''
	snr_linear = 10**(i/10)
	theoBPSK.append(0.5*sp.erfc(np.sqrt(snr_linear)))
	'''

d2 = mod.getSource(N,'QPSK')
sig2 = mod.getModulator(d2,'QPSK')

QPSK = []
#theoQPSK = []
for i in range(0,11):
	tx2 = channel.awgnChannel(sig2,i)
	rx2 = mod.QPSKDemodulator(tx2)
	s2 = mod.symerr(d2,rx2)
	ber2 = s2/N
	QPSK.append(ber2)
	'''
	snr_linear = 10**(i/10)
	theoQPSK.append(sp.erfc(np.sqrt(snr_linear/2))-(0.5*sp.erfc(np.sqrt(snr_linear/2)))**2)
	'''

d3 = mod.getSource(N,'8PSK')
sig3 = mod.getModulator(d3,'8PSK')

PSK8 = []
theoPSK8 = []
'''
pi = np.pi
def f(x,snr,M):
	a = np.exp(-snr*((np.sin(pi/M)/np.sin(x+pi/M))**2))
	return a/pi
'''
for i in range(0,11):
    tx3 = channel.awgnChannel(sig3,i)
    rx3 = mod.PSK8Demodulator(tx3)
    s3 = mod.symerr(d3,rx3)
    ber3 = s3/N
    PSK8.append(ber3)
    '''
    # theoretical value
    snr_linear = 10**(i/10)
    integ = lambda x: f(x,snr_linear,8)
    inn = integrate.quad(integ, 0, pi-pi/8)
    theoPSK8.append(inn[0])
    snr_linear = 10**(i/10)
    '''

d4 = mod.getSource(N,'16QAM')
sig4 = mod.getModulator(d4,'16QAM')

QAM16 = []
theoQAM16 = []
for i in range(0,11):
    tx4 = channel.awgnChannel(sig4,i)
    rx4 = mod.QAM16Demodulator(tx4)
    s4 = mod.symerr(d4,rx4)
    ber4 = s4/N
    QAM16.append(ber4)
    
    '''
    snr_linear = 10**(i/10)
    P_sc = (3/4)*sp.erfc(np.sqrt((0.1*snr_linear)))
    theoQAM16.append(1-(1-P_sc)**2)
    '''
	

# Plot SER
plt.plot(x, BPSK, marker='o', label='BPSK simulation')
#plt.plot(x,theoBPSK, marker='o', label='BPSK theoretical')
plt.plot(x, QPSK, marker='^', label='QPSK simulation')
#plt.plot(x,theoQPSK, marker='^', label='QPSK theoretical')
plt.plot(x, PSK8, marker='P', label='8PSK simulation')
#plt.plot(x,theoPSK8, marker='P', label='PSK8 theoretical')
plt.plot(x, QAM16, marker='p', label='16QAM simulation')
#plt.plot(x,theoQAM16, marker='p', label='QAM16 theoretical')
plt.legend()
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yscale('log')
plt.grid(True, which="both")
plt.title('SER Comparison of Modulations in AWGN Channel')
plt.xlabel('SNR (dB)')
plt.ylabel('Error Rate')
plt.show()
