import pytest
import pandas as pd
import numpy as np
from app.ml.preprocessor import GLOFPreprocessor

def test_preprocessor_features():
    prep = GLOFPreprocessor(sequence_length=10)
    data = {
        "water_level_m": [14.0 + i * 0.1 for i in range(20)],
        "water_level_rate_m_per_hr": [0.05] * 20,
        "rainfall_mm_hr": [i * 2.0 for i in range(20)],
        "temperature_c": [3.0] * 20,
        "humidity_percent": [65.0] * 20,
        "pressure_hpa": [580.0] * 20,
        "ground_vibration_g": [0.01] * 20,
        "moraine_tilt_deg": [0.12] * 20,
        "river_discharge_m3_s": [12.0] * 20,
        "lake_area_change_percent": [0.0] * 20,
        "camera_anomaly_score": [0.05] * 20,
        "satellite_change_score": [0.02] * 20,
    }
    df = pd.DataFrame(data)
    df_derived = prep.compute_derived_features(df)
    
    assert "water_level_delta" in df_derived.columns
    assert "rainfall_10min_sum" in df_derived.columns
    assert "combined_environmental_stress" in df_derived.columns

    normalized = prep.normalize(df_derived)
    assert normalized.shape == (20, 12)
    assert (normalized >= 0.0).all() and (normalized <= 1.0).all()

    seq, _ = prep.create_sequences(normalized)
    assert seq.shape[1] == 10
    assert seq.shape[2] == 12
