from enum import IntEnum

# IntEnum 要求值必须是数字
# unique 装饰器要求值不能重复，即无法设置别名
@unique
class VIP(IntEnum):
    YELLOW = 1
    # GREEN = 'str' # 报错