import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the function to integrate
def f(x):
    return x ** 2

# Integration parameters
a = 0  # Lower bound
b = 2  # Upper bound
n = 10000  # Number of points for the Monte Carlo method

# Monte Carlo method for integral calculation
samples = np.random.uniform(a, b, n)
integral_monte_carlo = (b - a) * np.mean(f(samples))

# Calculate the analytical integral using quad
integral_analytical, error = quad(f, a, b)

# Print results
print("Integral using Monte Carlo:", integral_monte_carlo)
print("Analytical integral:", integral_analytical)
print("Difference:", abs(integral_analytical - integral_monte_carlo))

# Plotting the graph
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Integration graph of f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()
