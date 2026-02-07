import argparse
from src.physics.engine import OrbitalEngine

def main():
    parser = argparse.ArgumentParser(description="Orbital Mechanics Calculator")
    parser.add_argument("--altitude", type=float, default=400.0, help="Altitude in km")
    parser.add_argument("--target_altitude", type=float, default=35786.0, help="Target Altitude for Hohmann Transfer (km)")
    
    args = parser.parse_args()
    
    # Convert km to meters
    r1 = OrbitalEngine.R_EARTH + (args.altitude * 1000)
    r2 = OrbitalEngine.R_EARTH + (args.target_altitude * 1000)
    
    print(f"--- Orbital Parameters ---")
    print(f"Initial Radius: {r1/1000:.2f} km")
    print(f"Target Radius:  {r2/1000:.2f} km")
    
    # Calculate Period
    period = OrbitalEngine.orbital_period(r1)
    print(f"Orbital Period at {args.altitude} km: {period/60:.2f} minutes")
    
    # Calculate Velocity
    v = OrbitalEngine.orbital_velocity(r1, r1) # Circular orbit assumption
    print(f"Orbital Velocity: {v:.2f} m/s")
    
    # Hohmann Transfer
    transfer = OrbitalEngine.hohmann_transfer_delta_v(r1, r2)
    print(f"\n--- Hohmann Transfer ---")
    print(f"Delta V1 (Burn 1): {transfer['delta_v1']:.2f} m/s")
    print(f"Delta V2 (Burn 2): {transfer['delta_v2']:.2f} m/s")
    print(f"Total Delta V:     {transfer['total_delta_v']:.2f} m/s")

if __name__ == "__main__":
    main()
