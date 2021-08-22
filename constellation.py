import argparse
import matplotlib.pyplot as plt
from comm import channel, mod

def parse_args():
    parser = argparse.ArgumentParser(description='Constellation diagram.')
    parser.add_argument('-n', '--N', default=10000, type=int, help='Number of symbols.', metavar='')
    parser.add_argument('-s', '--SNR', default=10, type=int, help='Signal-to-noise ratio (SNR).', metavar='')
    parser.add_argument('-m', '--ModType', default='QPSK', type=str.lower, help='Modulation type.', metavar='')
    return parser.parse_args()

def main(args) -> None:
    d = mod.getSource(args.N,args.ModType)				    # Random symbols
    sig = mod.getModulator(d,args.ModType)			        # Modulate random data
    noisySig = channel.awgnChannel(sig,args.SNR)		    # Pass through the AWGN channel
    rx = mod.getDemodulator(noisySig,args.ModType)	        # Demodulate received data
    s = mod.symerr(d,rx)				                	# Calculate symbol error
    print("Symbol error: {:d}/{:d}".format(s,args.N))
    print("Error probability: {:f}".format(s/args.N))

    # Plot the Constellation diagram
    X = [x.real for x in noisySig]
    Y = [x.imag for x in noisySig]
    plt.scatter(X, Y, s = 1, color='red')
    plt.axis('equal')
    plt.title('Constellation Diagram of {:s}'.format(args.ModType.upper()))
    plt.show()

if __name__=='__main__':
    args = parse_args()
    main(args)
