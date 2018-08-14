# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
def test ():
  return 'i am module1 -> test'

if __name__ == '__main__':
  print('someone call me') # 直接执行才会进来，别人导入的不会