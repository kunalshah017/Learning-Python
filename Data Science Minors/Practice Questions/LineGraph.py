from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [10000, 12000, 15000, 17000, 16000, 18000]

plt.plot(months, sales, marker = 'o')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales')

plt.show()