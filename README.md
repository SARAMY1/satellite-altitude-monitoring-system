# Satellite Altitude Monitoring System 🛰️

[![Python tests](https://github.com/SARAMY1/satellite-altitude-monitoring-system/actions/workflows/python-tests.yml/badge.svg)](https://github.com/SARAMY1/satellite-altitude-monitoring-system/actions/workflows/python-tests.yml)

**Project 1 — Python for Aerospace Engineering | Beginner portfolio project**

A beginner-friendly, fully documented Python project that analyzes **simulated** satellite altitude observations, flags out-of-range measurements, and generates a text report. Built to practise fundamental Python skills while introducing the logic behind spacecraft telemetry monitoring.

> **Important:** All measurements and operational thresholds in this repository are hypothetical. This is a rule-based educational example, **not** an orbit determination, flight safety, or machine-learning system. Actual spacecraft monitoring requires mission-specific requirements and orbital state analysis.

## Objectives

- Load altitude observations from a CSV file.
- Compute the mean, minimum, and maximum altitude.
- Classify measurements as LOW, NORMAL, or HIGH.
- Count out-of-range observations.
- Calculate signed deviation from a 400 km reference altitude.
- Produce and save a human-readable report.
- Plot measurements with upper/lower thresholds and highlight warnings.
- Verify core calculations with automated unit tests.

## Project structure

```text
satellite-altitude-monitoring-system/
├── satellite_altitude_monitor.py   # Main program and reusable functions
├── data/
│   └── altitudes.csv               # Seven simulated observations (km)
├── results/
│   └── sample_report.txt           # Example generated report
├── tests/
│   └── test_monitor.py             # Unit tests
├── .github/
│   └── workflows/
│       └── python-tests.yml        # Automated test workflow
├── requirements.txt                # Matplotlib plotting dependency
├── .gitignore                      # Python-generated files excluded
├── LICENSE                         # MIT License
└── README.md
```

## Getting started

**Requirements:** Python 3.9 or later and Matplotlib for plotting.

1. Clone the repository:

   ```bash
   git clone https://github.com/SARAMY1/satellite-altitude-monitoring-system.git
   cd satellite-altitude-monitoring-system
   ```

2. Install the plotting dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Run the monitoring program:

   ```bash
   python satellite_altitude_monitor.py
   ```

4. Run the tests:

   ```bash
   python -m unittest discover -s tests -v
   ```

The program prints its report, writes `results/sample_report.txt`, and saves a high-resolution graph to `results/altitude_monitoring_graph.png`. On desktop systems, Matplotlib also opens a graph window. If you run in a headless environment, the PNG is still saved.

## Methodology

The assumed acceptable altitude interval is **390–410 km inclusive**. A reading below 390 km is classified as LOW; above 410 km as HIGH; otherwise NORMAL. This is a teaching threshold rather than a physical definition of a safe orbit.

The mean altitude is

```text
mean altitude = sum(altitude measurements) / number of measurements
```

The signed altitude deviation is

```text
deviation = measured altitude - 400 km
```

Positive deviations are above the reference, and negative deviations are below it.

## Sample results

Using the seven simulated measurements `[405, 402, 398, 395, 410, 387, 400]` km:

| Metric | Result |
| --- | ---: |
| Number of measurements | 7 |
| Average altitude | 399.57 km |
| Minimum altitude | 387 km |
| Maximum altitude | 410 km |
| Out-of-range measurements | 1 |
| Overall report status | ATTENTION REQUIRED |

The sixth observation (387 km) is below the assumed lower threshold. The complete per-reading output is available in [the sample report](results/sample_report.txt).

## Python concepts covered

- Variables and lists
- Functions, parameters, and return values
- `for` loops and `if/elif/else` conditions
- Counters, list comprehensions, and built-in functions
- CSV file input, formatted strings, and basic error handling
- Unit testing with Python's `unittest`

## Suggested learning exercises

1. Change the accepted range to 395–405 km.
2. Add three readings: 412, 389, and 403 km.
3. Count LOW and HIGH warnings separately.
4. Extend the CSV with a timestamp column.
5. Create a line plot of altitude against observation time.

## Future extensions

This project can later be extended with NumPy and Pandas for numerical analysis, Matplotlib for visualization, real orbital datasets with documented provenance, and carefully validated anomaly-detection models. A model-based approach must distinguish orbital motion and sensor behavior from arbitrary threshold crossings.

## License

Licensed under the [MIT License](LICENSE). See the license file for permissions and conditions.
