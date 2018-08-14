password = '123456'

print('input your password')
user_password = input() # 字符串

# print(int(user_password))
print(user_password)

if user_password == password:
  print('登陆成功')
  if False:
    print('dsdsfd')
elif user_password == 'root':
  print('超级用户')
else:
  print('失败')

n = 1
while n <= 10:
  print(n)
  n += 1
else:
  print('while done', n)