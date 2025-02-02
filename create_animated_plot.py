import csv
import matplotlib.pyplot as plt
import numpy as np
import cv2

# File path
data = 'C:\\Users\\Malbr\\Desktop\\Interference Image Recognition\\SW\\Circular\\Data\\Circular - 1-8 by 1-4 & 1-8 by 1-4 - Origin.csv'

# Read data
rows = []
with open(data, newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        rows.append([float(value) for value in row[1:]])

# Extract columns
time = [row[0] for row in rows]
angles = [row[1] for row in rows]
open_area = [row[2] for row in rows]

# Create the figure and axis
fig, ax = plt.subplots()

# Set the x and y limits
x_min, x_max = min(angles), max(angles)
y_min, y_max = 0, max(open_area) + 10
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_xlabel('Angle')
ax.set_ylabel('Open Area')
ax.set_xticks(np.arange(x_min, x_max + 1, 60))

line, = ax.plot([], [], color='b')
w, h = fig.canvas.get_width_height()

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('animated_plot.avi', fourcc, 20.0, (int(w), int(h)))

# Generate interpolated points for linear interpolation
num_interpolation_points = 1200
angles_interpolated = np.linspace(x_min, x_max, num_interpolation_points)
open_area_interpolated = np.interp(angles_interpolated, angles, open_area)

# Animate the plot
for i in range(1, num_interpolation_points):
    line.set_data(angles_interpolated[:i+1], open_area_interpolated[:i+1])
    plt.draw()
    plt.pause(0.1)
    
    # Capture the frame using the figure canvas
    buf = fig.canvas.print_to_buffer()
    frame = np.frombuffer(buf[0], dtype=np.uint8).reshape(h, w, 4)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

    # Write the frame to the video
    out.write(frame)

# Release video writer and close the plot
out.release()
plt.close()
