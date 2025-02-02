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

# Generate interpolated points for linear interpolation
num_interpolation_points = 1200
angles_interpolated = np.linspace(x_min, x_max, num_interpolation_points)
open_area_interpolated_origin = np.interp(angles_interpolated, angles, open_area_origin)
open_area_interpolated_horizontal = np.interp(angles_interpolated, angles, open_area_horizontal)
open_area_interpolated_diagonal = np.interp(angles_interpolated, angles, open_area_diagonal)

plt.plot(angles_interpolated, open_area_interpolated_origin, color='b', label='Rotatiom about Origin')
plt.plot(angles_interpolated, open_area_interpolated_horizontal, color='r', label='Horizontal Offset')
plt.plot(angles_interpolated, open_area_interpolated_diagonal, color='g', label='Diagonal Offset')
plt.savefig('plot_all.png', dpi=600)

