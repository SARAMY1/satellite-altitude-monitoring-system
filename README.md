# Satellite Altitude Monitoring System 🛰️

[![Python tests](https://github.com/SARAMY1/satellite-altitude-monitoring-system/actions/workflows/python-tests.yml/badge.svg)](https://github.com/SARAMY1/satellite-altitude-monitoring-system/actions/workflows/python-tests.yml)

**Project 1 — Beginner Python for Aerospace Engineering**

This educational project analyzes **simulated** CubeSat altitude measurements, identifies observations outside a simplified acceptable altitude range, generates a text report, and plots a graph.

**No CSV file is required.** The altitude values are stored directly in a Python list in `satellite_altitude_monitor.py`, making this version easier to learn from.

> The simulated measurements and thresholds are hypothetical. This is rule-based monitoring, not orbital state estimation, machine learning, or a real spacecraft safety assessment.

## Objectives

- Practise variables, lists, functions, loops and conditional statements.
- Calculate mean, minimum, maximum and altitude deviations.
- Flag measurements below 390 km or above 410 km (limits inclusive).
- Print and save a satellite health report.
- Generate and save a high-resolution altitude monitoring graph with Matplotlib.

## Setup

Requires Python 3.9+.

```bash
git clone https://github.com/SARAMY1/satellite-altitude-monitoring-system.git
cd satellite-altitude-monitoring-system
python -m pip install -r requirements.txt
python satellite_altitude_monitor.py
```

The graph opens in a desktop plotting window and is also saved as `results/altitude_monitoring_graph.png`. The report is saved as `results/sample_report.txt`.

Run tests with:

```bash
python -m unittest discover -s tests -v
```

## Data

The seven simulated altitude measurements (km) are:

```python
ALTITUDES = [405, 402, 398, 395, 410, 387, 400]
```

The average is **399.57 km**, the minimum is **387 km**, the maximum is **410 km**, and **one measurement** falls outside the assumed limits.

## Project structure

```text
satellite-altitude-monitoring-system/
├── satellite_altitude_monitor.py
├── requirements.txt
├── results/
│   └── sample_report.txt
├── tests/
│   └── test_monitor.py
├── .github/workflows/python-tests.yml
├── LICENSE
└── README.md
```

An earlier version included a `data/altitudes.csv` sample file. That file may remain in the repository for reference, but **the current program does not read or require it**.

## Learning exercises

1. Change the acceptable altitude range to 395–405 km.
2. Add readings 412, 389 and 403 km.
3. Count LOW and HIGH warnings separately.
4. Try changing graph titles and line styles.
5. In a later project, learn to load data from CSV using Pandas.

## License

MIT License — see [LICENSE](LICENSE).
