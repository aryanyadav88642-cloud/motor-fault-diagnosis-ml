# Bill of Materials

## Core Electronics

| Item | Qty | Purpose |
|------|-----|---------|
| ESP32 DevKit | 1 | Main controller, ADC, Wi-Fi |
| ADXL345 accelerometer (GY-291) | 1 | Vibration sensing (I2C/SPI) |
| ACS712 current sensor module | 1 | Motor current signature |
| KY-013 analog temperature sensor | 1 | Motor/bearing temperature |
| Slot-type IR speed sensor (LM393) | 1 | RPM measurement |
| Breadboard, jumper wires, resistors | 1 set | Prototyping, voltage divider |

## Motor Test Bench

| Item | Qty | Purpose |
|------|-----|---------|
| RS-775 DC motor | 1 | Test motor |
| BTS7960 motor driver | 1 | Motor speed/direction control |
| 12V battery | 1 | Motor power supply |

## Software

All free: Arduino IDE, Python, NumPy, SciPy, scikit-learn, Flask/Streamlit.

## Notes

- ACS712 outputs up to 5V, so use a voltage divider (e.g., 10k/15k) before the ESP32 ADC, which tolerates only 3.3V.
- KY-013 is analog, so connect it to an ADC1 pin. ADC2 pins don't work reliably when Wi-Fi is on.
- Power the ADXL345 from 3.3V.
- Connect the ESP32 GND, driver GND, and battery GND together.