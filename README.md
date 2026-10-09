# Motor Fault Diagnosis using Sensor Fusion (ML)

**Machine Learning-Based Fault Diagnosis in Electric Drive Motors Using Sensor Fusion of Vibration and Current Signatures**

Cornerstone project — B.Tech Electrical Engineering, 3rd Year
MITS Gwalior

## Overview
This project detects and classifies induction motor faults (bearing defects, rotor imbalance, misalignment) by fusing vibration data (MPU6050) and motor current signature data (ACS712) on an ESP32, then classifying faults using a machine learning model.

## Problem Statement
Unplanned motor failures cause costly downtime in industrial systems. Vibration analysis and Motor Current Signature Analysis (MCSA) each catch different fault types individually; fusing them improves detection accuracy and robustness.

## Approach
1. Acquire vibration (accelerometer) and current (Hall-effect) signals simultaneously from the ESP32
2. Extract time- and frequency-domain features (RMS, kurtosis, FFT peaks, sideband amplitudes) from both signals
3. Fuse the features into a single input vector
4. Train a classifier (SVM / Random Forest) to detect and classify fault type
5. Display live predictions on a dashboard

## Hardware
| Component | Qty |
|---|---|
| ESP32 DevKit | 1 |
| MPU6050 | 2 |
| ACS712 current sensor | 2 |
| Induction motor (test bench) | 1 |
| Bearings (healthy + faulty) | 3-4 |
| Supporting electronics (resistors, caps, perfboard, enclosure) | - |

Full BOM: [`/hardware/BOM.md`](hardware/BOM.md)

## Repository Structure
