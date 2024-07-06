import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import scrolledtext

# Initialize serial connection
ser = serial.Serial('/dev/ttyACM0', baudrate=9600)

# Initialize lists to store data
co2_data = []
voc_data = []
temp_data = []

# Initialize plot
fig, ax = plt.subplots(3, 1)

# Initialize tkinter window
root = tk.Tk()
root.title("Real-time Serial Data")

# Create scrolled text widget
serial_text = scrolledtext.ScrolledText(root, width=50, height=10)
serial_text.pack()

# Function to update plot and serial window
def update(frame):
    line = ser.readline().decode().strip().split('\t')
    if len(line) == 3:
        try:
            co2, voc, temp = map(float, line)
            co2_data.append(co2)
            voc_data.append(voc)
            temp_data.append(temp)
            ax[0].cla()
            ax[0].plot(co2_data, 'r-', label='CO2(ppm)')
            ax[0].legend(loc='upper left')
            ax[1].cla()
            ax[1].plot(voc_data, 'g-', label='VOC(ppb)')
            ax[1].legend(loc='upper left')
            ax[2].cla()
            ax[2].plot(temp_data, 'b-', label='TEMP(c°)')
            ax[2].legend(loc='upper left')
            serial_text.insert(tk.END, f"CO2: {co2}, VOC: {voc}, Temp: {temp}\n")
            serial_text.see(tk.END)
        except ValueError:
            pass

# Start animation
ani = FuncAnimation(fig, update, interval=100)

# Show plot
plt.show()

# Start tkinter main loop
root.mainloop()
