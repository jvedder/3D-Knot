# Copyright (c) 2026 John Vedder
# MIT License

import matplotlib.pyplot as plt
import numpy as np
from bezier import bezier1, bezier2, bezier3

'''
Point locations in unit cube:
       1-----. 
      /|    /|
     .-----2 |  
     | |   | |      z  y
     | .---|-3      | /
     |/    |/       |/
     0-----.        0---x

     This produces an arch when viewed from the front (x,z),
     a cusp when viewed from the side (y,z), and
     a S-curve when viewed from the top (x,y).
'''

p0 = np.array( [0,0,0], np.float32)
p1 = np.array( [0,1,1], np.float32)
p2 = np.array( [1,0,1], np.float32)
p3 = np.array( [1,1,0], np.float32)

pts = []
for i in range(101):
    t = i / 100.0
#    b1 = bezier1(t, p0, p2)
#    b2 = bezier2(t, p0, p1, p3)
    b3 = bezier3(t, p0, p1, p2, p3)
    pts.append(b3)

xs = [p[0] for p in pts]
ys = [p[1] for p in pts]
zs = [p[2] for p in pts]

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(xs, ys, zs, '-', linewidth=2)

plt.show()
