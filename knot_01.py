# Copyright (c) 2026 John Vedder
# MIT License

import matplotlib.pyplot as plt
import numpy as np
from bezier import bezier1, bezier2, bezier3

def plot_pts(ax, pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    zs = [p[2] for p in pts]
    ax.plot(xs, ys, zs, '-', linewidth=2)

def rotate_about_z(point, angle_degrees):
    """
    Rotates a 3D point about the Z axis using a rotation matrix.

    :param point: A 3D vector as a list or numpy array [x, y, z].
    :param angle_degrees: The rotation angle in degrees (counter-clockwise).
    :return: The rotated vector as a numpy array.
    """
    # Convert degrees to radians
    theta = math.radians(angle_degrees)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    # Define the Z-axis rotation matrix
    rotation_matrix = np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta, cos_theta,  0],
        [0,         0,          1]
    ])

    # Apply the rotation using matrix-vector multiplication
    rotated_pt = np.dot(rotation_matrix, point)
    return rotated_pt


p0 = np.array( [0,0,0], np.float32)
p1 = np.array( [0,1,1], np.float32)
p2 = np.array( [1,0,1], np.float32)
p3 = np.array( [1,1,0], np.float32)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

pts = []
for i in range(50):
    t = (i-50)/ 100.0
    b3 = bezier3(t, p0, p1, p2, p3)
    pts.append(b3)
plot_pts(ax, pts)

pts = []
for i in range(101):
    t = (i)/ 100.0
    b3 = bezier3(t, p0, p1, p2, p3)
    pts.append(b3)
plot_pts(ax, pts)

plt.show()
