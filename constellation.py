import matplotlib.pyplot as plt
from comm import channel, mod

def main() -> None:
    N = int(input('Number of symbols: '))
    SNR = int(input('Signal-to-noise ratio (SNR): '))
    modType = str(input('Modulation type: '))

    d = mod.getSource(N,modType)				# Random symbols
    sig = mod.getModulator(d,modType)			        # Modulate random data
    noisySig = channel.awgnChannel(sig,SNR)		        # Pass through the AWGN channel
    rx = mod.getDemodulator(noisySig,modType)	                # Demodulate received data
    s = mod.symerr(d,rx)					# Caculate symbol error
    print("Symbol error: {:d}/{:d}".format(s,N))
    print("Error probability: {:f}".format(s/N))

    # Plot the Constellation diagram
    X = [x.real for x in noisySig]
    Y = [x.imag for x in noisySig]
    plt.scatter(X, Y, s = 1, color='red')
    plt.axis('equal')
    plt.title('Constellation Diagram of {:s}'.format(modType))
    plt.show()

if __name__=='__main__':
    main()
