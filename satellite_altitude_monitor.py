"""Educational satellite altitude monitoring with simulated observations.

Run: python satellite_altitude_monitor.py
All altitudes are in kilometres. Limits are illustrative, not flight criteria.
"""
from pathlib import Path
import csv

LOWER_LIMIT_KM = 390.0
UPPER_LIMIT_KM = 410.0
REFERENCE_ALTITUDE_KM = 400.0
DATA_FILE = Path(__file__).resolve().parent / "data" / "altitudes.csv"


def load_altitudes(filename=DATA_FILE):
    """Read altitude observations from CSV and return a list of floats."""
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [float(row["altitude_km"]) for row in reader]


def average_altitude(values):
    """Return the arithmetic mean; reject an empty dataset."""
    if not values:
        raise ValueError("At least one altitude measurement is required.")
    return sum(values) / len(values)


def classify_altitude(altitude, lower=LOWER_LIMIT_KM, upper=UPPER_LIMIT_KM):
    """Classify an altitude; both boundaries count as NORMAL."""
    if lower > upper:
        raise ValueError("Lower limit must not exceed upper limit.")
    if altitude < lower:
        return "LOW"
    elif altitude > upper:
        return "HIGH"
    return "NORMAL"


def count_warnings(values, lower=LOWER_LIMIT_KM, upper=UPPER_LIMIT_KM):
    """Count readings outside the accepted range."""
    return sum(classify_altitude(value, lower, upper) != "NORMAL" for value in values)


def altitude_extremes(values):
    """Return the minimum and maximum altitudes."""
    if not values:
        raise ValueError("At least one altitude measurement is required.")
    return min(values), max(values)


def altitude_deviation(values, reference=REFERENCE_ALTITUDE_KM):
    """Calculate signed differences from a reference altitude."""
    return [altitude - reference for altitude in values]


def build_report(values, satellite_name="CubeSat-01"):
    """Create a printable monitoring report from altitude measurements."""
    average = average_altitude(values)
    minimum, maximum = altitude_extremes(values)
    warnings = count_warnings(values)
    status = "STABLE" if warnings == 0 else "ATTENTION REQUIRED"

    lines = [
        "=" * 46,
        "SATELLITE ALTITUDE MONITORING REPORT",
        "=" * 46,
        f"Satellite: {satellite_name}",
        f"Measurements: {len(values)}",
        f"Average altitude: {average:.2f} km",
        f"Minimum altitude: {minimum:.2f} km",
        f"Maximum altitude: {maximum:.2f} km",
        f"Warning count: {warnings}",
        f"Overall status: {status}",
        "",
        "INDIVIDUAL MEASUREMENTS",
    ]
    for index, altitude in enumerate(values, start=1):
        classification = classify_altitude(altitude)
        deviation = altitude - REFERENCE_ALTITUDE_KM
        lines.append(
            f"{index:02d}. {altitude:.2f} km | {classification:<6} | "
            f"Deviation: {deviation:+.2f} km"
        )
    return "\n".join(lines)


def plot_altitudes(values, output_path, show=True):
    """Plot observations and operational limits; save a 300-DPI PNG.

    The chart uses observation number, not elapsed time, because the
    sample CSV does not include timestamps.
    """
    import matplotlib.pyplot as plt

    if not values:
        raise ValueError("Cannot plot an empty dataset.")

    measurements = list(range(1, len(values) + 1))
    fig, ax = plt.subplots(figsize=(10, 5.5))

    # Join observations in their recorded order.
    ax.plot(measurements, values, marker="o", linewidth=2,
            label="Measured altitude")

    # Horizontal dashed lines show the assumed acceptable range.
    ax.axhline(LOWER_LIMIT_KM, linestyle="--", color="tab:red",
               label=f"Lower limit ({LOWER_LIMIT_KM:g} km)")
    ax.axhline(UPPER_LIMIT_KM, linestyle="--", color="tab:purple",
               label=f"Upper limit ({UPPER_LIMIT_KM:g} km)")

    # Highlight observations outside either threshold.
    warning_x = [i for i, value in zip(measurements, values)
                 if classify_altitude(value) != "NORMAL"]
    warning_y = [values[i - 1] for i in warning_x]
    if warning_x:
        ax.scatter(warning_x, warning_y, color="tab:red", s=100,
                   zorder=5, label="Warning")

    ax.set_title("CubeSat-01: Satellite Altitude Monitoring")
    ax.set_xlabel("Measurement number")
    ax.set_ylabel("Altitude (km)")
    ax.set_xticks(measurements)
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.legend()
    fig.tight_layout()

    # Save before displaying so the file is always available.
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    if show:
        plt.show()
    plt.close(fig)


def main():
    """Load the sample data, generate a report, and save a text copy."""
    values = load_altitudes()
    report = build_report(values)
    print(report)

    # Create the results directory if it does not already exist.
    results_dir = Path(__file__).resolve().parent / "results"
    results_dir.mkdir(exist_ok=True)
    (results_dir / "sample_report.txt").write_text(report + "\n", encoding="utf-8")

    # Save the graph and open a plotting window on desktop systems.
    chart_path = results_dir / "altitude_monitoring_graph.png"
    plot_altitudes(values, chart_path)
    print(f"Graph saved to: {chart_path}")


if __name__ == "__main__":
    main()
