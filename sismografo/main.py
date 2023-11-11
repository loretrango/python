import serial
import matplotlib.pyplot as plt
from time import sleep

# Open the serial port
ser = serial.Serial('ttyACM0', 115200)  # Change 'COM3' to your serial port and 115200 to your baud rate

# Initialize empty lists to store data
time_list = []
voltZ_list = []
voltX_list = []
voltY_list = []

# Read and plot data
try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip().split('\t')

            # Extract data
            voltZ = float(data[0])
            voltX = float(data[1])
            voltY = float(data[2])

            # Append data to lists
            time_list.append(len(time_list) + 1)  # Assuming each line is a new data point
            voltZ_list.append(voltZ)
            voltX_list.append(voltX)
            voltY_list.append(voltY)

            # Plot in real-time
            plt.plot(time_list, voltZ_list, label='Volt Z')
            plt.plot(time_list, voltX_list, label='Volt X')
            plt.plot(time_list, voltY_list, label='Volt Y')

            plt.xlabel('Time')
            plt.ylabel('Voltage')
            plt.title('ADC Data Plot')
            plt.legend()
            plt.draw()
            plt.pause(0.01)  # Adjust the pause time as needed
except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")
    plt.show()