import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行 api 调用并存储响应 可以通过 https://api.github.com/rate_limit 查看 Github 的请求限制
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# 将响应结果保存到一个变量中
response_dict = r.json()
print('Total repositories:', response_dict['total_count'])

# 处理结果
# print(response_dict.keys())
repo_dicts = response_dict['items']
print('Repositiories returned:', len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print('\nKeys:', len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # 这里做了个 encode 处理，因为 description 中有的包含 表情，在下边 chart.add('', plot_dicts) 中会对 label decode，由于不支持表情，会报错，所以先 encode 一下，另外有的 description 是 null ，需要做一个 try 的兼容
    try:
        label = repo_dict['description'].encode('utf-8')
    except:
        label = 'no description'

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': label,
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15 # x 轴项目名称最长 15 个字符
my_config.show_y_guides = False # 隐藏 y 轴水平线
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts) # 这里 plot_dicts 包含 value 和 label 两个属性，value 是 y 轴数值，label 是鼠标移动上去的提示信息
chart.render_to_file('python_repos1.svg')
