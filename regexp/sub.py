# pylint: skip-file
import re

language = 'PythonC#'


def convert(value):
	print(value)  # <re.Match object; span=(0, 2), match='Py'>
	print(value.group())
	return '德玛西亚' + value.group() + '万岁'


# r = re.sub('Py', 'eeee', language)
r = re.sub('Py', convert, language)

print(r)

testword = 'sf6s57sa9sf'


def convert1(value):
	matched = int(value.group())
	if matched > 6:
		return '9'  # 注意 return 必须是 字符串，因为它只能操作字符串
	else:
		return '0'


result = re.sub('\d', convert1, testword)
print(result)
