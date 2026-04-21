# Visualize the two sets of x and y values as scatter plots and line graphs 

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 3, 3, 3.5, 4]

# Plot these values as a scatter plot
plt.plot(x_values, y_values)
plt.scatter(x_values, y_values, color='red')

plt.show()