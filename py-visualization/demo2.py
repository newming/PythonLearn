import matplotlib.pyplot as plt

# 绘制一个点
# plt.scatter(2, 4, s=200)

# 绘制一系列点
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=200)

plt.title('Squere Number', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
