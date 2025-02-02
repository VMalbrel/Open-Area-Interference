import csv
import matplotlib.pyplot as plt
import numpy as np
import cv2

# File path
data = 'C:\\Users\\Malbr\\Desktop\\Interference Image Recognition\\SW\\Circular\\Data\\Circular - 1-8 by 1-4 & 1-8 by 1-4.csv'

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
open_area_origin = [row[2] for row in rows]
open_area_horizontal = [row[3] for row in rows]
open_area_diagonal = [row[4] for row in rows]

# Create the figure and axis
fig, ax = plt.subplots()

line_origin, = ax.plot([], [], color='b', label='Rotatiom about Origin')
line_horizontal, = ax.plot([], [], color='r', label='Horizontal Offset')
line_diagonal, = ax.plot([], [], color='g', label='Diagonal Offset')

# Set the x and y limits
x_min, x_max = min(angles), max(angles)
y_min, y_max = 0, max(open_area_origin) + 10
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_xlabel('Angle (degrees)')
ax.set_ylabel('Open Area')
ax.set_xticks(np.arange(x_min, x_max + 1, 60))
ax.legend()
ax.set_title('Open Area vs. Angle')
w, h = fig.canvas.get_width_height()

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('animated_plot_all.avi', fourcc, 20.0, (int(w), int(h)))

# Generate interpolated points for linear interpolation
num_interpolation_points = 1200
angles_interpolated = np.linspace(x_min, x_max, num_interpolation_points)
open_area_interpolated_origin = np.interp(angles_interpolated, angles, open_area_origin)
open_area_interpolated_horizontal = np.interp(angles_interpolated, angles, open_area_horizontal)
open_area_interpolated_diagonal = np.interp(angles_interpolated, angles, open_area_diagonal)

# Animate the plot
for i in range(1, num_interpolation_points):
    line_origin.set_data(angles_interpolated[:i+1], open_area_interpolated_origin[:i+1])
    line_horizontal.set_data(angles_interpolated[:i+1], open_area_interpolated_horizontal[:i+1])
    line_diagonal.set_data(angles_interpolated[:i+1], open_area_interpolated_diagonal[:i+1])
    plt.draw()
    plt.pause(0.1)
    
    # Capture the frame using the figure canvas
    buf, (width, height) = fig.canvas.print_to_buffer()
    frame = np.frombuffer(buf, dtype=np.uint8).reshape(height, width, 4)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)

    # Write the frame to the video
    out.write(frame)

# Release video writer and close the plot
out.release()
plt.close()
