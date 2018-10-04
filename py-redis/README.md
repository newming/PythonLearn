# python 操作 redis 数据库

[redis中文网](http://www.redis.cn/)

[安装教程](https://www.jianshu.com/p/6b5eca8d908b)

用途: 数据库、缓存和消息中间件

```bash
# 启动 redis 默认端口 6379
redis-server
# 连接 redis
redis-cli
```

数据类型：

- 字符串(string)
- 散列(hashes)
- 列表(list)
- 集合(sets)
- 有序集合(sorted sets)

```
keys * # 查看所有数据
flushall # 清空所有数据库命令
flushdb # 清空当前数据库
```

## 字符串相关操作

- 设置值 http://www.redis.cn/commands/set.html: set key "value" [EX seconds] [PX milliseconds] [NXIXX]
- 获取: get key
- 追加值: append key 'valew'
- 设置多个键值: mset key1 value1 key2 value2 [key value ...]
- 获取多个键值: mget key1 [key...]
- 删除: del key1 [key...]
- 增加/减少: incr|decr key

## 列表相关操作

- lpush/rpush: 从队列的左/右边入队一个或多个元素 http://www.redis.cn/commands/lpush.html
- lrange: 获取某一节的数据 http://www.redis.cn/commands/lrange.html
- ltrim: 修剪数据 http://www.redis.cn/commands/ltrim.html
- llen: 获取 list 的长度 http://www.redis.cn/commands/llen.html
- lpop/rpop: http://www.redis.cn/commands/lpop.html/http://www.redis.cn/commands/rpop.html 从列表的 左/右 删除一个元素
- lpushx/rpush: 当队列存在时，从队列的左/右边入队一个元素

## 集合 Set 相关操作

- sadd/srem: 添加/删除元素
- sismember: 判断是否为 set 的一个元素
- smembers: 返回该集合的所有成员
- sdiff: 返回一个集合与其他集合的差异
- sinter: 返回几个集合的交集
- sunion: 返回几个集合的并集

## 散列 Hash 相关操作

- hset/hget: 设置/获取散列值
- hmset/hmset: 设置/获取多对散列值
- hsetnx: 如果散列已经存在，则不设置
- hkeys/hvals: 返回所有的 Keys/Values
- hlen: 返回散列包含域 field 的数量(key)
- hdel: 删除散列指定的域(field)
- hexists: 判断是否存在

```
hset news:1 title 'ddd'
hset news:1 content '22ddd'
hget news:1 title
hget news:1 content
hmget news:1 title content
hkeys news:1
hvals news:1
hlen news:1
hdel news:1 title
```

## redis destop manager

[redis 可视化操作工具](http://docs.redisdesktop.com/en/latest/install/#build-from-source)

# python 操作 redis

[文档](https://pypi.org/project/redis/)

[doc](https://redis-py.readthedocs.io/en/latest/)

```bash
pip install redis
```