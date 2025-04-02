from matplotlib import pyplot as plt

temperature = [20, 22, 25, 28, 30, 32, 35, 37, 40, 42]
ice_cream_sales = [200, 250, 270, 300, 330, 360, 400, 450, 470, 500]

plt.scatter(temperature, ice_cream_sales)
plt.xlabel('Temperature (°C)')
plt.ylabel('Ice Cream Sales (units)')
plt.title('Relationship Between Temperature and Ice Cream Sales')

plt.show()