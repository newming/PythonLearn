# Python MySQL

## mysql

命令行登录 mysql:

```bash
mysql -u root -p
# 输入密码
# 查看全部数据库
show databases;

# 使用某个数据库
use databasename;

# 查看下边的表
show tables;

# 查看某个表下得数据
select * from tablename
```

### 基础语法

[各种语法名次解释](https://www.cnblogs.com/fan-yuan/p/7879353.html)

- DDL(Data Definition Language): 数据定义语句
  - CREATE TABLE/DATABASE
  - ALTER TABLE/DATABASE
  - DROP TABLE/DATABASE
- DML(Data Manipulation Language): 数据管理语句
  - INSERT: 新增
  - DELETE: 删除
  - UPDATE: 修改
  - SELECT: 查询

```sql
-- 代表注释
-- 关键字（比如 CREATE）一般大写，一条语句结尾有英文分号，加上反引号代表其他字符，例如 id ，加上 反引号就可以和关键字 id 区别了

-- 创建并使用 数据库
CREATE DATABASE `mydatabase`;
USE `mydatabase`;
-- 查看数据库
SHOW databases
```