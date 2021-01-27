import sys
import random
import matplotlib.pyplot as plt
import myutil

x = [-0.03, 0.78, 2.07, 2.77, 4.10, 5.38, 5.99, 6.84, 8.12, 8.89, 9.43]
y = [0.88, 2.45, 2.43, 4.07, 5.49, 6.46, 7.02, 8.27, 8.70, 10.23, 10.65]


plt.plot(x, y, 'o')
plt.show()

print(myutil.fact(5))
