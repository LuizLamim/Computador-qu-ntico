import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = |sin(x) + cos(x)|
def f(x):
  """
  Calculates the absolute value of sin(x) + cos(x).
  """
  return np.abs(np.sin(x) + np.cos(x))

# Generate a range of x values from -2*pi to 2*pi
x = np.linspace(-2 * np.pi, 2 * np.pi, 500)

# Calculate the corresponding y values
y = f(x)

# Create the plot
plt.figure(figsize=(10, 6))  # Adjust the figure size for better readability
plt.plot(x, y, color='blue', linewidth=2)

# Add labels and a title
plt.title(r'Gráfico da função $f(x) = |\sin(x) + \cos(x)|$', fontsize=16)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)

# Add a grid for better visualization
plt.grid(True, linestyle='--', alpha=0.7)

# Set the x-axis ticks to be multiples of pi
plt.xticks([-2 * np.pi, -1.5 * np.pi, -np.pi, -0.5 * np.pi, 0,
            0.5 * np.pi, np.pi, 1.5 * np.pi, 2 * np.pi],
           [r'$-2\pi$', r'$-1.5\pi$', r'$-\pi$', r'$-0.5\pi$', r'$0$',
            r'$0.5\pi$', r'$\pi$', r'$1.5\pi$', r'$2\pi$'])

# Add a text annotation to the plot
plt.text(-np.pi, 1.2, r'Função periódica', fontsize=10, color='red')

# Display the plot
plt.show()