# Drone Sensor Data Visualization
This project visualizes sensor data 
from a drone in real-time on linear graphs. 
The data includes current, voltage, and 
power measurements.

## How to Install and Run the Project
To run the project, make sure you have Python 3 
and the following packages installed:
- pandas
- matplotlib

You can install these packages using pip: <br>
`pip install pandas matplotlib`<br>
Once the packages are installed, run the following 
command in your terminal: <br>
`python ivplot.py`

## How to Use the Project
To use the project, you need to input your current values to the `current` array and voltage
values to the `voltage` array in the `updateValues` function in
**ivplot.py**. Your values can be entries in a .csv file or can be derived
from APIs of your choice. <br>
```python
def updateValues(_, axs, x_val, index, current, voltage, power, data_size=10):
# Here's where you can input your sensor values
 x_val.append(next(index))
 current.append(<input your current values here>)
 voltage.append(<input your voltage values here>)
 power.append(current[-1]*voltage[-1])
 # ...
```

You can also customize the time interval between each update by changing the
`intervalValue` variable at the top of the file (in milliseconds). The code will neatly display
the current and voltage in dynamic linear laterally-scrolling plots. <br>

```python
intervalValue = 500 # Change the interval here
```
A correct implementation of appending actual values to the appropriate **current** and **voltage** arrays is shown in `redis_ivplot.py` as depicted below:
```python
# IMPORTING ACTUAL VALUES FROM REDIS DATABASE
telemetry_data = r.hgetall('telemetry')

new_current = telemetry_data.get('Battery current', 0)
new_current = float(new_current[:len(new_current)-1])

new_voltage = telemetry_data.get('Battery voltage', 0)
new_voltage = float(new_voltage[:len(new_voltage)-1])
# APPEND VALUES TO THEIR RESPECTIVE ARRAYS

current.append(new_current)
voltage.append(new_voltage)
power.append(current[-1] * voltage[-1])
```

## License
This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details. 
You have the right to use, copy, modify, distribute the software and use, either for commercial or non-commercial purposes

## Credits
This project was created by **Aamir Mohamed Thahir Ali** [@aamiral1](https://www.github.com/aamiral1). Special thanks to **Kush
Makkapati** [@1Blademaster](https://github.com/1Blademaster/) for their guidance.
