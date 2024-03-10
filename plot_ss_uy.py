import pandas as pd
import matplotlib.pyplot as plt

# Define your columns upfront for clarity
columns = [
    "x",
    "shearStress_xx",
    "shearStress_xy",
    "shearStress_xz",
    "shearStress_yy",
    "shearStress_yz",
    "shearStress_zz",
    "U_x",
    "U_y",
    "U_z",
]

# Load the data from the file
file_path = "data/line.xy"
data = pd.read_csv(file_path, delim_whitespace=True, comment="#", names=columns)

# Assuming the shear stress and velocity might have negative values and need to be made absolute
data["shearStress_xy"] = abs(data["shearStress_xy"])
data["U_y"] = abs(data["U_y"])

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 6))

# Configuring the primary y-axis (shear stress)
color = "tab:red"
ax1.set_xlabel("Position (m)")
ax1.set_ylabel("Shear Stress (kPa)", color=color)
ax1.plot(data["x"], data["shearStress_xy"], color=color)
ax1.tick_params(axis="y", labelcolor=color)

# Creating a twin axis for flow velocity
ax2 = ax1.twinx()
color = "tab:blue"
ax2.set_ylabel("Flow Velocity (m/s)", color=color)
ax2.plot(data["x"], data["U_y"], color=color)
ax2.tick_params(axis="y", labelcolor=color)

# Additional formatting
ax1.grid(False)  # Remove gridlines as requested
ax2.grid(False)
plt.title(
    f"Shear Stress and Flow Velocity Profile Inside Cylindrical G27 (Alginate I-1G 4% w/v, {file_path.replace('.xy', '').replace('data/', '').replace('uLs', 'uL/s')})"
)
fig.tight_layout()  # Adjust layout

# Save the plot
plt.savefig(file_path.replace(".xy", ".png"), dpi=300)

# Show the plot
plt.show()
