import serial
import csv
import sys

port_number = sys.argv[1]
filename = sys.argv[2]
# Serial port settings
port = '/dev/cu.usbserial-'+str(port_number)  # Change this to your Arduino's serial port
rate = 9600  

csv_file = open(filename+'.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)

ser = serial.Serial(port, rate)

try:

    while True:
        if ser.in_waiting > 0:
            try:
                # Read the data from serial
                line = ser.readline().decode('utf-8').strip()
                
                # Split the data
                data = line.split(' ')

                # Write to CSV file
                if len(data)>3:
                    csv_writer.writerow(data)

                print(data)
            
            except UnicodeDecodeError as e:
                print(f"UnicodeDecodeError: {e}")
                continue  # Skip this line and move on to the next one
        
except KeyboardInterrupt:
    print("Stopping data logging.")
    pass

finally:
    # Close the serial port and CSV file
    ser.close()
    csv_file.close()
