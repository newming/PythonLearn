from urllib import request

class Spider():
    url = 'https://www.panda.tv/cate/lol?pdt=1.24.s1.3.7jalfegfh0a'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        pass

    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)
        

spider = Spider()
spider.go()
