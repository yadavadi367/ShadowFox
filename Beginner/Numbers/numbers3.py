#If you cross a 490 meter long street in 7 minutes, calculate your speed in meters per second. Print the answer without any decimal point in it. Hint: Speed = Distance / Time

distance = 490  # meters
time = 7 * 60   # convert minutes to seconds

speed = distance / time
print(str(int(speed)) + " m/s")