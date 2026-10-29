import pytest
from app.services.simulator_service import SensorSimulatorService

def test_simulator_scenarios():
    sim = SensorSimulatorService()
    
    # Test normal
    sim.set_scenario("NORMAL")
    p1 = sim.step()
    assert p1["reading"]["water_level_m"] > 0
    assert p1["prediction"]["final_fusion_score"] <= 55.0

    # Test heavy rain
    sim.set_scenario("HEAVY_RAIN")
    p2 = sim.step()
    assert p2["reading"]["rainfall_mm_hr"] >= 0

    # Test critical pattern increases risk over baseline
    sim.set_scenario("CRITICAL_GLOF_PATTERN")
    for _ in range(5):
        p3 = sim.step()
    assert p3["prediction"]["final_fusion_score"] > p1["prediction"]["final_fusion_score"]
