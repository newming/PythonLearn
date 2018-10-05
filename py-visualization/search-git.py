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

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)

chart.render_to_file('python_repos.svg')
