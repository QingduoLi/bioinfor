from celluloid import Camera
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2)
camera = Camera(fig)
t = np.linspace(0, 5 * np.pi, 128, endpoint=False)
t2 = np.linspace(0, 1 * np.pi, 128, endpoint=False)
for i in t2:
    axes[0].plot(t, np.cos(t / 2 + i), color='b')
    axes[1].plot(t2, np.sin(t2 - i), color='b')
    camera.snap()

animation = camera.animate()
animation.save('celluloid_example.gif', writer='imagemagick')