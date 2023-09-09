import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta

# Replace 'COMX' with the actual COM port of your Arduino
ser = serial.Serial('/dev/ttyACM0', baudrate=9600)

# Initialize empty lists to store data and timestamps
co2_data = []
voc_data = []
temp_data = []
timestamps = []

# Create a figure and axis for plotting
fig, ax = plt.subplots(3, 1, figsize=(8, 6))

# Define initial y-axis limits for CO2
co2_ylim = (400, 1000)

# Define a function to update the plot and save data to a file in real-time
def animate(i):
    line = ser.readline().decode('utf-8').rstrip().split('\t')
    
    if len(line) == 3:
        co2, voc, temp = map(float, line)
        timestamp = datetime.now()
        
        co2_data.append(co2)
        voc_data.append(voc)
        temp_data.append(temp)
        timestamps.append(timestamp)
        
        # Only keep the data points from the last 50 seconds
        cutoff_time = timestamp - timedelta(seconds=3600)
        while timestamps[0] < cutoff_time:
            co2_data.pop(0)
            voc_data.pop(0)
            temp_data.pop(0)
            timestamps.pop(0)
        
        # Clear the previous plot and update with new data
        ax[0].clear()
        ax[1].clear()
        ax[2].clear()
        
        # Set the y-axis limits for CO2 to the initial values
        ax[0].set_ylim(co2_ylim)
        
        ax[0].plot(timestamps, co2_data, label='CO2(ppm)')
        ax[1].plot(timestamps, voc_data, label='VOC(ppb)')
        ax[2].plot(timestamps, temp_data, label='TEMP(c°)')
        
        ax[0].set_ylabel('CO2(ppm)')
        ax[1].set_ylabel('VOC(ppb)')
        ax[2].set_ylabel('TEMP(c°)')
        
        ax[0].legend()
        ax[1].legend()
        ax[2].legend()
        
        # Save the data to a text file
        with open('sensor_data.txt', 'a') as file:
            file.write(f'{timestamp}\t{co2}\t{voc}\t{temp}\n')

# Create an animation that calls the 'animate' function every 1000 milliseconds (1 second)
ani = FuncAnimation(fig, animate, interval=1000)

# Show the plot
plt.tight_layout()
plt.show()

# Close the serial connection when done
ser.close()
