#just for test
#just for test 2
f= open(r"C:\Users\Kajal\OneDrive\Desktop\project\hello.txt", 'r')
if f:
    print("File is successfully opened")

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 