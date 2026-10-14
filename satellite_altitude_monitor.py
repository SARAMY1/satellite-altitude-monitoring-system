"""Project 1: Satellite Altitude Monitoring System.

Beginner Python project using simulated altitude measurements stored in a list.
Run: python satellite_altitude_monitor.py
Requires Matplotlib (see requirements.txt).
"""

from pathlib import Path

# SECTION 1: SATELLITE DATA AND SIMPLIFIED MONITORING LIMITS
SATELLITE_NAME = "CubeSat-01"
ALTITUDES = [405, 402, 398, 395, 410, 387, 400]  # kilometres
LOWER_LIMIT_KM = 390
UPPER_LIMIT_KM = 410
REFERENCE_ALTITUDE_KM = 400

# Save outputs next to this script, regardless of the working directory.
RESULTS_FOLDER = Path(__file__).resolve().parent / "results"


# SECTION 2: CALCULATE THE AVERAGE ALTITUDE
def average_altitude(values):
    """Return the arithmetic mean of the measurements."""
    if not values:
        raise ValueError("The altitude list cannot be empty.")
    return sum(values) / len(values)


# SECTION 3: CLASSIFY ONE MEASUREMENT
def classify_altitude(altitude):
    """Return LOW, HIGH or NORMAL; the boundary values are NORMAL."""
    if altitude < LOWER_LIMIT_KM:
        return "LOW"
    elif altitude > UPPER_LIMIT_KM:
        return "HIGH"
    else:
        return "NORMAL"


# SECTION 4: COUNT ALL OUT-OF-RANGE MEASUREMENTS
def count_warnings(values):
    """Count how many measurements are outside the assumed limits."""
    warning_count = 0

    for altitude in values:
        if classify_altitude(altitude) != "NORMAL":
            warning_count += 1

    return warning_count


# SECTION 5: FIND THE MINIMUM AND MAXIMUM
def altitude_extremes(values):
    """Return the minimum and maximum measured altitudes."""
    if not values:
        raise ValueError("The altitude list cannot be empty.")
    return min(values), max(values)


# SECTION 6: CALCULATE SIGNED DEVIATIONS FROM 400 KM
def altitude_deviation(values):
    """Return each altitude minus the reference altitude."""
    deviations = []

    for altitude in values:
        deviation = altitude - REFERENCE_ALTITUDE_KM
        deviations.append(deviation)

    return deviations


# SECTION 7: CREATE THE SATELLITE HEALTH REPORT
def build_report(values):
    """Create a readable report containing statistics and classifications."""
    average = average_altitude(values)
    minimum, maximum = altitude_extremes(values)
    warnings = count_warnings(values)
    deviations = altitude_deviation(values)

    # These are educational threshold warnings, not flight safety decisions.
    overall_status = "STABLE" if warnings == 0 else "ATTENTION REQUIRED"

    lines = [
        "=" * 50,
        "        SATELLITE ALTITUDE HEALTH REPORT",
        "=" * 50,
        f"Satellite Name: {SATELLITE_NAME}",
        f"Total Measurements: {len(values)}",
        f"Average Altitude: {average:.2f} km",
        f"Minimum Altitude: {minimum:.2f} km",
        f"Maximum Altitude: {maximum:.2f} km",
        f"Total Altitude Warnings: {warnings}",
        f"Overall Status: {overall_status}",
        "",
        "INDIVIDUAL ALTITUDE MEASUREMENTS",
        "-" * 50,
    ]

    # zip() pairs each altitude with its corresponding deviation.
    for number, (altitude, deviation) in enumerate(
        zip(values, deviations), start=1
    ):
        status = classify_altitude(altitude)
        lines.append(
            f"Measurement {number}: {altitude:.2f} km | "
            f"{status} | Deviation: {deviation:+.2f} km"
        )

    return "\n".join(lines)


# SECTION 8: PLOT AND SAVE THE ALTITUDE GRAPH
def plot_altitudes(values, output_file, show=True):
    """Plot altitude measurements, limits and out-of-range warnings."""
    import matplotlib.pyplot as plt

    if not values:
        raise ValueError("Cannot plot an empty altitude list.")

    # Measurement numbers 1, 2, 3, ... are the x-axis values.
    measurement_numbers = list(range(1, len(values) + 1))

    # Create a figure and axes to draw on.
    fig, ax = plt.subplots(figsize=(10, 6))

    # Draw the measured altitude line.
    ax.plot(
        measurement_numbers, values,
        color="tab:blue", marker="o", linewidth=2,
        label="Measured Altitude"
    )

    # Show the assumed upper and lower monitoring limits.
    ax.axhline(
        LOWER_LIMIT_KM, color="tab:red", linestyle="--",
        label=f"Lower Limit ({LOWER_LIMIT_KM} km)"
    )
    ax.axhline(
        UPPER_LIMIT_KM, color="tab:purple", linestyle="--",
        label=f"Upper Limit ({UPPER_LIMIT_KM} km)"
    )

    # Highlight measurements that violate either limit.
    for number, altitude in zip(measurement_numbers, values):
        if classify_altitude(altitude) != "NORMAL":
            ax.scatter(number, altitude, color="red", s=110, zorder=5)
            ax.annotate(
                "WARNING", (number, altitude),
                xytext=(0, -20), textcoords="offset points",
                ha="center", color="red", fontweight="bold"
            )

    # Add labels, grid lines, and legend.
    ax.set_title(f"{SATELLITE_NAME}: Altitude Monitoring")
    ax.set_xlabel("Measurement Number")
    ax.set_ylabel("Altitude (km)")
    ax.set_xticks(measurement_numbers)
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.legend()
    fig.tight_layout()

    # Save a high-resolution PNG before displaying the graph.
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_file, dpi=300, bbox_inches="tight")

    # Show the graph window when running on a desktop.
    if show:
        plt.show()

    # Release the plotting resources.
    plt.close(fig)


# SECTION 9: RUN THE COMPLETE PROJECT
def main():
    """Generate the report and graph from the Python list above."""
    report = build_report(ALTITUDES)
    print(report)

    # Create the results folder automatically if it is missing.
    RESULTS_FOLDER.mkdir(parents=True, exist_ok=True)

    # Save the report in a text file.
    report_file = RESULTS_FOLDER / "sample_report.txt"
    report_file.write_text(report + "\n", encoding="utf-8")
    print(f"\nReport saved to: {report_file}")

    # Generate, save, and display the graph.
    graph_file = RESULTS_FOLDER / "altitude_monitoring_graph.png"
    plot_altitudes(ALTITUDES, graph_file)
    print(f"Graph saved to: {graph_file}")


# SECTION 10: ONLY RUN main() WHEN THIS FILE IS EXECUTED DIRECTLY
if __name__ == "__main__":
    main()
