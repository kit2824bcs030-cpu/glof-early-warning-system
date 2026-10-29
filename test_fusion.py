import pytest
from app.ml.fusion import MultimodalRiskFusionEngine

def test_fusion_normal_conditions():
    engine = MultimodalRiskFusionEngine()
    reading = {
        "water_level_m": 14.0,
        "water_level_rate_m_per_hr": 0.02,
        "rainfall_mm_hr": 1.0,
        "ground_vibration_g": 0.008,
        "moraine_tilt_deg": 0.12,
        "camera_anomaly_score": 0.04,
        "satellite_change_score": 0.02,
    }
    result = engine.evaluate_risk(dnn_risk_score=15.0, reading=reading, sensor_confidence=0.95)
    assert result["final_risk_score"] <= 30.0
    assert result["risk_class"] == "NORMAL"

def test_fusion_critical_conditions():
    engine = MultimodalRiskFusionEngine()
    reading = {
        "water_level_m": 24.5,
        "water_level_rate_m_per_hr": 2.8,
        "rainfall_mm_hr": 85.0,
        "ground_vibration_g": 0.65,
        "moraine_tilt_deg": 4.5,
        "camera_anomaly_score": 0.92,
        "satellite_change_score": 0.85,
    }
    result = engine.evaluate_risk(dnn_risk_score=92.0, reading=reading, sensor_confidence=0.95)
    assert result["final_risk_score"] >= 76.0
    assert result["risk_class"] == "CRITICAL"
    assert result["elevated_modalities_count"] >= 3
