#!/usr/bin/env python3
"""
GLOFGuard AI - Standalone IoT Sensor Simulator
Simulates multimodal environmental sensor telemetry in the Himalayas.
Can send telemetry to backend WebSocket or print live telemetry to console.
"""

import sys
import os
import time
import json
import random
import datetime

# Add backend directory to sys.path if run directly
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
backend_path = os.path.join(parent_dir, "backend")
if backend_path not in sys.path:
    sys.path.append(backend_path)

from app.services.simulator_service import SensorSimulatorService

def main():
    print("=" * 60)
    print("  GLOFGuard AI - IoT Glacial Lake Sensor Simulator")
    print("=" * 60)
    print("Simulating Himalayan telemetry every 2.0 seconds...")
    print("Scenarios: NORMAL, HEAVY_RAIN, RAPID_MELT, MORAINE_INSTABILITY, LANDSLIDE_EVENT, CRITICAL_GLOF_PATTERN")
    print("Press Ctrl+C to terminate.\n")

    sim = SensorSimulatorService()
    sim.start()

    cycle = 0
    try:
        while True:
            cycle += 1
            packet = sim.step()
            r = packet["reading"]
            p = packet["prediction"]

            ts = r["timestamp"]
            wl = r["water_level_m"]
            rate = r["water_level_rate_m_per_hr"]
            rf = r["rainfall_mm_hr"]
            vib = r["ground_vibration_g"]
            tilt = r["moraine_tilt_deg"]
            risk = p["final_fusion_score"]
            status = p["risk_class"]

            color = "\033[92m" if status == "NORMAL" else "\033[93m" if status == "WATCH" else "\033[38;5;208m" if status == "WARNING" else "\033[91m"
            reset_color = "\033[0m"

            print(
                f"[{ts[:19]}] Cycle #{cycle:04d} | "
                f"WL: {wl:5.2f}m ({rate:+.2f}m/h) | "
                f"Rain: {rf:4.1f}mm/h | "
                f"Vib: {vib:.3f}g | "
                f"Tilt: {tilt:.2f}° | "
                f"{color}Risk: {risk:5.1f}/100 [{status}]{reset_color}"
            )

            time.sleep(2.0)
    except KeyboardInterrupt:
        print("\n[Simulator] Simulator stopped by user.")
        sim.stop()

if __name__ == "__main__":
    main()
