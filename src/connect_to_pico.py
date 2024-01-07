import serial 

# Configure the serial port connection
port = "/dev/ttyACM0"
baudrate = 115200
serial_connection = serial.Serial(port, baudrate)

# Open a file on your computer to write the received data
destination_file = open("/home/anton/Downloads/store_info.txt", "wb")

# Read and write data until the transfer is complete
while True:
    data = serial_connection.read(128)
    if data == b"EOF":
        break
    print(data)
    destination_file.write(data)

# Close the files and serial connection
destination_file.close()
serial_connection.close()

