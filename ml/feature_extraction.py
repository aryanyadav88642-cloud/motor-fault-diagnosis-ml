"""
Feature Extraction for Motor Fault Diagnosis
Sensor Fusion: Vibration (MPU6050) + Current (ACS712)

Works on simulated data until real sensor logs are available.
Replace simulate_signal() calls with pd.read_csv() on real data later.
"""

import numpy as np
from scipy.fft import fft
from scipy.stats import kurtosis
import pandas as pd

SAMPLE_RATE = 2000  # Hz, matches firmware's 2kHz sampling
WINDOW_SIZE = 1024   # samples per feature window


def simulate_signal(fault_type="healthy", duration_s=1.0, fs=SAMPLE_RATE):
    """Generate a synthetic vibration+current signal for pipeline testing."""
    t = np.linspace(0, duration_s, int(fs * duration_s))
    base_freq = 50  # motor line frequency (Hz)

    vibration = 0.5 * np.sin(2 * np.pi * base_freq * t)
    current = 2.0 * np.sin(2 * np.pi * base_freq * t)

    if fault_type == "bearing":
        # bearing faults add high-frequency impulses
        fault_freq = 157  # example BPFO-like frequency
        vibration += 0.3 * np.sin(2 * np.pi * fault_freq * t)
    elif fault_type == "imbalance":
        # imbalance shows at 1x running speed, larger amplitude
        vibration += 0.8 * np.sin(2 * np.pi * base_freq * t)
    elif fault_type == "misalignment":
        # misalignment shows at 2x running speed
        vibration += 0.4 * np.sin(2 * np.pi * 2 * base_freq * t)

    noise_v = np.random.normal(0, 0.05, len(t))
    noise_c = np.random.normal(0, 0.05, len(t))

    return vibration + noise_v, current + noise_c


def extract_features(signal, fs=SAMPLE_RATE):
    """Extract time- and frequency-domain features from one signal window."""
    rms = np.sqrt(np.mean(signal ** 2))
    peak = np.max(np.abs(signal))
    kurt = kurtosis(signal)
    crest_factor = peak / rms if rms > 0 else 0

    fft_vals = np.abs(fft(signal))[:len(signal) // 2]
    freqs = np.fft.fftfreq(len(signal), 1 / fs)[:len(signal) // 2]
    dominant_freq = freqs[np.argmax(fft_vals)]
    dominant_amp = np.max(fft_vals)

    return {
        "rms": rms,
        "peak": peak,
        "kurtosis": kurt,
        "crest_factor": crest_factor,
        "dominant_freq": dominant_freq,
        "dominant_amp": dominant_amp,
    }


def build_fused_feature_vector(vibration_signal, current_signal):
    """Fuse vibration + current features into one labeled dict."""
    v_feats = {f"vib_{k}": v for k, v in extract_features(vibration_signal).items()}
    c_feats = {f"cur_{k}": v for k, v in extract_features(current_signal).items()}
    return {**v_feats, **c_feats}


def build_dataset(n_samples_per_class=50):
    """Build a simulated labeled dataset for pipeline testing."""
    fault_types = ["healthy", "bearing", "imbalance", "misalignment"]
    rows = []

    for fault in fault_types:
        for _ in range(n_samples_per_class):
            vib, cur = simulate_signal(fault_type=fault)
            features = build_fused_feature_vector(vib, cur)
            features["label"] = fault
            rows.append(features)

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = build_dataset()
    df.to_csv("data/processed/simulated_features.csv", index=False)
    print(f"Generated {len(df)} samples with {df.shape[1]-1} features.")
    print(df.head())