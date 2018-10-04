from random import randint
import pygal

class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return randint(1, self.num_sides)

die = Die()

# 开始掷骰子，并将结果存储到一个list中
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

# 100次掷骰子结果
# print(results)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 各个点数出现的次数
# print(frequencies)

# 对结果进行数据可视化
hist = pygal.Bar()

hist.title = 'results of rolling one D6 100 times'

hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
