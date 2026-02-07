# Scientific Orbital Mechanics Library

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.11-8CAAE6.svg)](https://scipy.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26-013243.svg)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade astrodynamics library** for calculating orbital parameters, maneuvers, and trajectories. Built with maximum precision using SciPy constants and numerical integration methods, this library supports mission planning and satellite tracking operations.

## 🚀 Features

- **Keplerian Propagator**: High-precision orbit propagation using Kepler's equations.
- **Hohmann Transfer**: Calculation of delta-v budgets for optimal orbital transfers.
- **Orbital Elements**: Conversion between state vectors (position/velocity) and classical orbital elements.
- **Ground Track**: Projection of satellite orbits onto Earth's surface (latitude/longitude).
- **Perturbation Modeling**: Framework for adding J2 perturbations (Earth oblateness).
- **Type Safety**: Fully typed with Python 3.11+ type hints.

## 📁 Project Structure

```
calc-orbital-mechanics-library/
├── src/
│   ├── physics/      # Core astrodynamics engine
│   ├── api/          # REST API for calculations
│   └── main.py       # CLI Entrypoint
├── tests/            # Numerical validation tests
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/calc-orbital-mechanics-library.git

# Install
pip install -r requirements.txt

# Run CLI
python src/main.py --altitude 400 --eccentricity 0.001
```

## 📄 License

MIT License
