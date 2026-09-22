"""Smoke test for calc-orbital-mechanics-library: verifies OrbitalEngine math."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.physics.engine import OrbitalEngine


def main():
    # LEO ~400km altitude: semi-major axis ~= R_earth + 400km
    a_leo = OrbitalEngine.R_EARTH + 400_000
    period = OrbitalEngine.orbital_period(a_leo)
    # ISS orbital period is ~92.9 minutes = ~5574 s; allow 5% tolerance
    assert 5_200 < period < 5_900, f"unexpected LEO period: {period}"

    v = OrbitalEngine.orbital_velocity(a_leo, a_leo)
    # circular LEO velocity ~7.67 km/s
    assert 7_000 < v < 8_500, f"unexpected LEO velocity: {v}"

    dv = OrbitalEngine.hohmann_transfer_delta_v(a_leo, OrbitalEngine.R_EARTH + 35_786_000)
    assert dv["delta_v1"] > 0 and dv["delta_v2"] > 0
    assert abs(dv["total_delta_v"] - (dv["delta_v1"] + dv["delta_v2"])) < 1e-9

    print("smoke OK: orbital_period, orbital_velocity, hohmann_transfer_delta_v")


if __name__ == "__main__":
    main()
