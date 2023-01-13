
import random as random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initial Starting Point
x = [0]
y = [0]

# Plot Initial Points
fig, ax = plt.subplots()
ax.plot(x, y, 'ro')
ax.grid('on')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# All Possible Moves
moves = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}

n = random.randint(0, 3)
x_new = np.add([moves[n][0]], x).tolist()
y_new = np.add([moves[n][1]], y).tolist()


def animate(i):
    x.append((i+1) * (moves[n][0]/10) + x[i])
    print(y[i])
    y.append((i+1) * (moves[n][1]/10) + y[i])
    # print(y[i])
    plt.cla()
    ax.plot(x[i+1], y[i+1], 'ro')


ani = FuncAnimation(fig=fig, func=animate,
                    frames=10, interval=100, repeat=False)

plt.show()
# print(y)
# print(n)
# print(y_new)
# print(moves[n][1]/10)
