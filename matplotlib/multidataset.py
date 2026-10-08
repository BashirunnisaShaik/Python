import matplotlib.pyplot as plt
class_a = [10, 20, 30, 40, 50]
class_b = [15, 25, 35, 45, 55]
plt.hist(class_a, bins=5, alpha=0.5, label="Class A")
plt.hist(class_b, bins=5, alpha=0.5, label="Class B")
plt.legend()
plt.show()