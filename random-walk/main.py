import time
import matplotlib.pyplot as plt

from man import Man
from bird import Bird

man = Man()
bird = Bird()

for i in range(0, 10**7):
    man.move()
    bird.move()

print("Man return back: " + str(man.returns[-1]) + " times")
print("Bird return back: " + str(bird.returns[-1]) + " times")

plt.plot(man.returns, "-g", label="man")
plt.plot(bird.returns, "-r", label="bird")
plt.ylabel('Amount of returns')
plt.xlabel('Step')
plt.legend()
plt.show()

plt.plot(man.distances, "-g", label="man")
plt.plot(bird.distances, "-r", label="bird")
plt.ylabel('Distance from origin')
plt.xlabel('Step')
plt.legend()
plt.show()
