# Constellation diagram and SER comparison in AWGN channel with different Modulation technique.
## Introduction
This program contain two communication experiments.<br>
### Constellation diagram
* **File name:**`constellation.py`<br>

This file gives constellation diagram of modulation types below:<br>
`['BPSK', 'QPSK', '8PSK', '16QAM']`<br>

You can choose one of them and select a proper channel SNR to observe the constellation of received signal through AWGN channel.<br>

The following figure is a constellation diagram with parameters:                        
* Modulation type: QPSK
* Number of symbols: 4096
* SNR (dB): 10

<img src='https://user-images.githubusercontent.com/38156969/123224547-7d144d00-d504-11eb-946f-3edcad5be51a.png' alt='Figure_1' width=600 align=center>

### SER comparison
* **File name:** `ber.py`

This file gives symbol-error rate (SER) comparison with different modulation technique listed below:<br>
`['BPSK', 'QPSK', '8PSK', '16QAM']`<br>

The following figure is the result with 100000 symbols.
<img src='https://user-images.githubusercontent.com/38156969/123234799-d92f9f00-d50d-11eb-9b2c-d87c415bb729.png' alt='Figure_2' width=600>

## Requirement
>It works on python@3.9

Required modules:
* matplotlib
* scipy
* numpy


