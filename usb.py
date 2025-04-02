import serial

PORT = '/dev/ttyUSB0'
BAUD = 115200  # Match your device's baud rate (e.g., 115200, 57600)

try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
    print(f"Reading from {PORT} at {BAUD} baud. Press Ctrl+C to stop.")

    while True:
        if ser.in_waiting > 0:
            data = ser.readline()
            int_values = [int(b) for b in data]  # List of integers (0-255)
            print(int_values)


except serial.SerialException as e:
    print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nStopped by user.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
