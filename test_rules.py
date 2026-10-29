import pytest
from app.ml.rules import SafetyRuleEngine

def test_rules_multi_sensor_critical():
    engine = SafetyRuleEngine()
    fusion_result = {"final_risk_score": 84.0}
    reading = {
        "water_level_rate_m_per_hr": 2.5,
        "rainfall_mm_hr": 60.0,
        "ground_vibration_g": 0.45,
        "moraine_tilt_deg": 3.2,
        "sensor_health": "HEALTHY",
    }
    is_valid, level, reasons = engine.evaluate_safety_rules(fusion_result, reading, sensor_confidence=0.92)
    assert is_valid is True
    assert level == "CRITICAL"
    assert len(reasons) > 0

def test_rules_degraded_confidence_safeguard():
    engine = SafetyRuleEngine()
    fusion_result = {"final_risk_score": 90.0}
    reading = {
        "water_level_rate_m_per_hr": 3.0,
        "rainfall_mm_hr": 80.0,
        "ground_vibration_g": 0.5,
        "moraine_tilt_deg": 4.0,
        "sensor_health": "FAULTY",
    }
    is_valid, level, reasons = engine.evaluate_safety_rules(fusion_result, reading, sensor_confidence=0.35)
    assert is_valid is False
    assert level == "SENSOR_FAULT_DEGRADED"
