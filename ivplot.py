from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import math

# Arrays for sensor data
current = []
voltage = []
power = []

x_val = []

index = count() # counter

# Interval (ms)
intervalValue = 500

fig, axs = plt.subplots(3)
fig.suptitle('Drone Control')


# Function to be run on every frame
def updateValues(i):
    # Generate random values
    x_val.append(next(index))
    current.append(random.uniform(1, 45))
    voltage.append(random.uniform(11, 22))
    power.append(current[-1]*voltage[-1])

    # Plot the lines
    axs[0].clear()
    axs[1].clear()
    axs[2].clear()
    axs[0].plot(x_val, current)
    axs[1].plot(x_val, voltage, color="red")
    axs[2].plot(x_val, power, color="green")


    # Configure axis labels
    axs[0].set_xlabel("Time (s)")
    axs[1].set_xlabel("Time (s)")
    axs[2].set_xlabel("Time(s)")
    axs[0].set_ylabel("Amperes")
    axs[1].set_ylabel("Voltage")
    axs[2].set_ylabel("Power")

    # Display current data
    axs[0].legend([f'Current: {round(current[-1], 2)}A'], loc='upper left')
    axs[1].legend([f'Voltage: {round(voltage[-1], 2)}V'], loc='upper left')
    axs[2].legend([f'Power: {round(power[-1], 2)} W'], loc="upper left")

    # Set x-axis limits to show only the last 10 seconds of data
    if len(x_val) > 10:
        axs[0].set_xlim([x_val[-10], x_val[-1]])
        axs[1].set_xlim([x_val[-10], x_val[-1]])
        axs[2].set_xlim([x_val[-10], x_val[-1]])

    plt.tight_layout()

ani = FuncAnimation(fig, updateValues, interval=intervalValue)
plt.show()
