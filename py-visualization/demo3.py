import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

"""
c 是点的颜色，edgecolors 为点的轮廓的颜色，即描边
c=(0, 0, 0) 可以使用 rgb 颜色模式自定义颜色，为一个元组，包含三个 0-1 之间的小数值，分别代表 红绿蓝 的分量，值越接近0，颜色越深
"""
# plt.scatter(x_values, y_values, s=40, c='red', edgecolors='none')
# 颜色映射，根据每个点的 y 值来设置颜色
plt.scatter(x_values, y_values, s=40, c=y_values, cmap=plt.cm.Blues, edgecolors='none')

plt.title('Squere Number', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=12)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# plt.show()
# 自动保存图片，第二个参数指定将图表多余的空白区域裁剪掉
plt.savefig('squares_plot.png', bbox_inches='tight')
