from matplotlib import pyplot as plt

categories = ["Rent", "Food", "Transport", "Entertainment", "Savings"]
expenses = [500, 300, 100, 150, 200]

plt.pie(expenses, labels=categories)

plt.show()

