import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = "data/uLs.csv"
data = pd.read_csv(file_path)

# Correcting the issue with the markers for shear stress

# Setting up the plot again
fig, ax1 = plt.subplots(figsize=(10, 6))

color = "tab:red"
# First y-axis (pressure) with markers
ax1.set_xlabel("Extrusion Rate (uL/s)")
ax1.set_ylabel("Pressure (kPa)", color=color)
ax1.plot(
    data["flow_rate_uL_per_s"],
    data["pressure_kpa"],
    color=color,
    marker="o",
    linestyle="-",
)
ax1.tick_params(axis="y", labelcolor=color)

# Creating a twin Axes sharing the x-axis
ax2 = ax1.twinx()

color = "tab:blue"
# Second y-axis (shear stress) with correct markers
ax2.set_ylabel("Maximum Shear Stress (kPa)", color=color)
ax2.plot(
    data["flow_rate_uL_per_s"],
    data["shear_stress_kpa"],
    color=color,
    marker="s",
    linestyle="--",
)
ax2.tick_params(axis="y", labelcolor=color)

# Title and layout
plt.title(
    "Pressure and Shear Stress vs. Extrusion Rate (Cylindrical G27, Alginate I-1G 4% w/v)"
)
fig.tight_layout()
fig.savefig(file_path.replace(".csv", ".png"), dpi=300)

plt.show()
