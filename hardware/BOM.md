# Bill of Materials

Budget target: ₹4,000-5,000 (excluding motor)

## Core Electronics
| Item | Qty | Approx ₹ |
|---|---|---|
| ESP32 DevKit (30-pin) | 1 | 450-550 |
| MPU6050 accelerometer module | 2 | 300-400 |
| ACS712 current sensor (5A/20A) | 2 | 300-400 |
| Perfboard, resistors, capacitors, jumper wires | 1 set | 200-300 |
| 5V 2A power adapter + USB cable | 1 | 150-250 |
| Project enclosure box | 1 | 150-250 |

## Motor Test Bench
| Item | Qty | Approx ₹ |
|---|---|---|
| Induction motor (borrowed from lab, or used) | 1 | 0-1,500 |
| Base plate, motor mount, shaft coupling | 1 set | 500-800 |
| Bearings — healthy + faulty (6203/6204) | 3-4 | 300-400 |

## Safety & Power
| Item | Qty | Approx ₹ |
|---|---|---|
| MCB/fuse, switch, terminal blocks, plug | 1 set | 400-600 |

## Software
All free — Arduino IDE/ESP-IDF, Python, NumPy, SciPy, scikit-learn, Flask/Streamlit.

## Notes
- Voltage divider (10k/20k resistors) required between ACS712 output and ESP32 ADC, since ACS712 outputs up to 5V and the ESP32 ADC tolerates only 3.3V.
- Two ACS712 sensors are sufficient for a 3-phase motor; the third phase can be estimated.
- Skip VFD, ADS1115, and split-core CT to stay within budget — use the ESP32's internal ADC with a voltage divider instead.
- Fault bearings can be self-made by scratching the race or drilling a small hole in an old bearing.