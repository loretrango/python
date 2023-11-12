# ... (previous code)

# Read and plot data
try:
    while True:
        if ser.in_waiting > 0:
            print("Data received")
            data = ser.readline().decode().strip().split('\t')

            # Check if the data has the expected format
            if len(data) == 3 and all(val.replace('-', '').isdigit() for val in data):
                print("Valid data format")
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
                ax.clear()  # Clear the previous plot
                ax.plot(time_list, voltZ_list, label='Volt Z')
                ax.plot(time_list, voltX_list, label='Volt X')
                ax.plot(time_list, voltY_list, label='Volt Y')

                ax.set_xlabel('Time')
                ax.set_ylabel('Voltage')
                ax.set_title('ADC Data Plot')
                ax.legend()

                plt.savefig('real_time_plot.png')  # Save the plot as an image file
                plt.pause(0.01)  # Adjust the pause time as needed
            else:
                print("Invalid data format:", data)

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")
    plt.ioff()  # Turn off interactive mode
    plt.show()
