r = open('./test.md', 'w+')
r.write('德玛西亚')

r.close()

r = open('./test.md', 'r')
fileStr = r.read()
print(fileStr)