# 注意， python 中没有 switch 语句
# day = 2

# switch (day){
#     case 0:
#         dayName = 'Sunday'
#         break
#     case 1:
#         dayName = 'Monday'
#         break
#     case 2:
#         dayName = 'Tuesday'
#         break
#     default:
#         dayName = 'Unknown'
#         break
# }

# 1.用字典代替 switch
switcher = {
    0: 'sunday',
    1: 'monday',
    2: 'tuesday'
}
day = 8

# day_name = switcher[day] # 无法模拟 default 情况
day_name = switcher.get(day, 'Unknow')
print(day_name)

# 2.复杂场景的 switch ，需要用 function
def get_sunday():
    return 'sunday'

def get_monday():
    return 'monday'

def get_tuesday():
    return 'tuesday'

switcher1 = {
    0: get_sunday,
    1: get_monday,
    2: get_tuesday
}

def get_default():
    return 'unknow'

day_name1 = switcher.get(day, get_default)()
print(day_name1)
