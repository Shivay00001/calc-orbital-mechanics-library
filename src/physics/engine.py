import numpy as np
from scipy import constants

class OrbitalEngine:
    G = constants.G
    M_EARTH = 5.972e24  # Mass of Earth in kg
    R_EARTH = 6371000   # Radius of Earth in meters

    @classmethod
    def orbital_period(cls, semi_major_axis: float) -> float:
        """Calculates the orbital period using Kepler's Third Law."""
        mu = cls.G * cls.M_EARTH
        return 2 * np.pi * np.sqrt(semi_major_axis**3 / mu)

    @classmethod
    def orbital_velocity(cls, r: float, a: float) -> float:
        """Calculates velocity at a given radius r for an orbit with semi-major axis a (Vis-viva equation)."""
        mu = cls.G * cls.M_EARTH
        return np.sqrt(mu * (2/r - 1/a))

    @classmethod
    def hohmann_transfer_delta_v(cls, r1: float, r2: float) -> dict:
        """Calculates delta-v for a Hohmann transfer orbit."""
        mu = cls.G * cls.M_EARTH
        
        # Velocity in initial orbit
        v1 = np.sqrt(mu / r1)
        
        # Velocity in final orbit
        v2 = np.sqrt(mu / r2)
        
        # Transfer orbit semi-major axis
        at = (r1 + r2) / 2
        
        # Velocity at perigee of transfer orbit
        v_t1 = np.sqrt(mu * (2/r1 - 1/at))
        
        # Velocity at apogee of transfer orbit
        v_t2 = np.sqrt(mu * (2/r2 - 1/at))
        
        delta_v1 = abs(v_t1 - v1)
        delta_v2 = abs(v2 - v_t2)
        
        return {
            "delta_v1": delta_v1,
            "delta_v2": delta_v2,
            "total_delta_v": delta_v1 + delta_v2
        }

    @classmethod
    def state_vector_from_elements(cls, inclination, raan, arg_perigee):
        """Placeholder for full Keplerian to Cartesian conversion."""
        # Implementation of rotation matrices would go here
        return {"x": 0.0, "y": 0.0, "z": 0.0}
