#coding:utf-8
STATEMENT = 0x01                         #0000,0001
MODIFY_AD = 0x02                         #0000,0010
AUDIT_AD = 0x04                          #0000,0100
CREATE_TOUTIAO_ECPM = 0x08               #0000,1000
CREATE_TOUTIAO_CPT = 0X10                #0001,0000
CREATE_TOUTIAO_SPLASH = 0x20             #0010,0000
CREATE_TOUTIAO_TEXT_LINK = 0x40          #0100,0000
CREATE_ESSAY_FEED_CPT = 0x80                 #1000,0000
CREATE_ESSAY_SPLASH = 0x0100        #0001,0000,0000
CREATE_ESSAY_FEED_ECPM = 0x0200   #0010,0000,0000
CREATE_FEED_EXCHANGE = 0x0400       #0100,0000,0000
CREATE_FEED_MARGIN = 0x0800         #1000,0000,0000
MANAGE_ROLE = 0x1000           #0001,0000,0000,0000
ADVANCED = 0x2000                 #0010,0000,0000,0000   # 高级选项
CREATE_ENTRY_FEED = 0x4000     #0100,0000,0000,0000
CREATE_TOUTIAO_ACTIVITY = 0x8000
CREATE_TOUTIAO_APP_OLD = 1 << 16
# 管理员权限
CREATE_SYSTEM_MSG = 1 << 17  # 发布消息
RECHARGE = 0x1 << 18  # 管理员充值
# 创建频道运营位置
CREATE_CHANNEL_CPT_ARTICLE = 1 << 19
# 新平台表示用户是否可以返回代理商平台
TONGTOU_BACK_TO_AGENT = 1 << 20
# 新平台表示用户是否可以返回管理员平台
TONGTOU_BACK_TO_ADMIN = 1 << 21
CREATE_UNION_AD = 1 << 22  # 开屏联播广告权限
# 只能投放网盟广告
ONLY_DELIVERY_UNION_AD = 1 << 23
# 返回账户管家平台
TONGTOU_BACK_TO_MAJORDOMO = 1 << 24
# 限制媒介权限 拥有此位时，部分功能不对其开放
LIMIT_PERM_FOR_EXECUTIVE = 1 << 25

# 全部权限不该包括的限制性权限
EXCLUDED_FROM_ALL = LIMIT_PERM_FOR_EXECUTIVE

SUPER_ADMIN = 0x1 << 62  # 超级管理员. 默认带所有权限

ALL = 0xffffffffffffffff & ~EXCLUDED_FROM_ALL  # 全部权限

print(0xffffffffffffffff)
print(~EXCLUDED_FROM_ALL)
print(0xffffffffffffffff & (~EXCLUDED_FROM_ALL) & 8)
print(ALL)

# print(18446744073656070143 & 8)
# print(18446744073656070143 & 6)
# print(18446744073656070143 & 3)
# print(6 & 3)
# print(4 & 3)

print((9223372036821217279 & (~(1 << 25))))

camp = ''.strip()
print(camp)
print((False or 0) or 2)

data = {}
print(data.get('a', 1))

thrift_spec = (
    None, # 0
    (1, 'systemOrigin', None, 0, ), # 1
    (2, 'createChannel', None, 1, ), # 2
    (3, 'createChannelUserId', None, "", ), # 3
)

print(thrift_spec[1][3])