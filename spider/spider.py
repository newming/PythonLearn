from urllib import request
import re


class Spider():
	'''
	爬虫类
	'''
	url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7jalfegfh0a'
	# ? 非贪婪，找到第一个 </div>
	root_pattern = '<div class="video-info">([\s\S]*?)</div>'
	name_pattern = '</i>([\s\S]*?)</span>'
	number_pattern = '<span class="video-number">([\s\S]*?)</span>'

	def __fetch_content(self):
		r = request.urlopen(Spider.url)
		htmls = r.read()
		htmls = str(htmls, encoding='utf-8')
		return htmls

	def __analysis(self, htmls):
		root_html = re.findall(Spider.root_pattern, htmls)

		anchors = []
		for html in root_html:
			name = re.findall(Spider.name_pattern, html)
			number = re.findall(Spider.number_pattern, html)
			anchor = {'name': name, 'number': number}
			anchors.append(anchor)

		return anchors

	# 优化 __analysis 结果
	def __refine(self, anchors):
		# 箭头函数
		l = lambda anchor: {
			'name': anchor['name'][0].strip(),
			'number': anchor['number'][0]
		}
		return map(l, anchors)

	# 排序 key 函数
	def __sort_seed(self, anchor):
		r = re.findall('\d*', anchor['number'])
		number = float(r[0])
		if '万' in anchor['number']:
			number *= 10000
		return number

	# 排序
	def __sort(self, anchors):
		anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
		return anchors

	# 展示
	def __show(self, anchors):
		# for anchor in anchors:
		#     print(anchor['name'] + '----' + anchor['number'])
		# 为了取到下标
		for rank in range(0, len(anchors)):
			print('rank' + str(rank + 1) + ': ' + anchors[rank]['name'] + ': ' + anchors[rank]['number'])

	def go(self):
		htmls = self.__fetch_content()
		anchors = self.__analysis(htmls)
		anchors = list(self.__refine(anchors))
		anchors = self.__sort(anchors)
		self.__show(anchors)
		# print(anchors)


spider = Spider()
spider.go()
