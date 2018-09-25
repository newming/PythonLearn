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

表中数据的常见类型：

- int: 整型
- smallint: 整型，占空间小
- char: 字符 char(200) 两百长度的字符，即使长度不够也会占着
- varchar: 字符，长度根据具体内容设定 varchar(200)，允许200以下的长度字符
- datetime: 日期

```sql
-- 代表注释
-- 关键字（比如 CREATE）一般大写，一条语句结尾有英文分号，加上反引号代表其他字符，例如 id ，加上 反引号就可以和关键字 id 区别了

-- 创建并使用 数据库
CREATE DATABASE `mydatabase`;
USE `mydatabase`;
-- 查看数据库
SHOW databases

-- 建表语句，注意标点，每个表必须有一个主键(唯一)
CREATE TABLE `student`(
	-- 自动增长
	`id` INT NOT NULL AUTO_INCREMRNT PRIMARY KEY,
	`name` VARCHAR(200) NOT NULL
);

-- 插入数据
INSERT INTO `tablename` (`key1`, `key2` ...) VALUE/VALUES ('value1', 'value2' ...)

-- 查询语句
SELECT
	select_expr, ....
FROM table_references
[WHERE where_definition]
[GROUP BY {col_name | expr | position}]
[HAVING where_definition]
[ORDER BY {col_name | expr | position} [ASC | DESC], ...]
[LIMIT {[offset,] row_count}]

-- 修改数据
UPDATE table_references
	SET col_name1=expr1[, col_name2=expr2 ...]
[WHERE where_definition]

-- 删除数据
DELETE FROM tbl_name
[WHERE where_definition]

-- 其他...
-- 新建索引(CREATE INDEX)
-- 修改表(ALTER TABLE)
-- 删除数据库、表、索引、视图等(DROP)
```

## 连接mysql数据库

[安装 mysqlclient](https://pypi.org/project/mysqlclient/)

[docs of mysqlclient](https://mysqlclient.readthedocs.io/user_guide.html#mysqldb)

[解决安装不上的问题，但是2还是安装不上](https://stackoverflow.com/questions/51123044/pip-install-mysql-python)

注意不要用 easy_install pip 去装 pip，就用 官网的方法

/Library/Frameworks/Python.framework/Versions/3.7/bin/pip3 这里是 pip3 的 bin 目录，为了能使用 pip2(pip)，将/Library/Frameworks/Python.framework/Versions/3.7/bin/pip 改为了 /Library/Frameworks/Python.framework/Versions/3.7/bin/pip-backup

> 最终，2 和 3 都装上了 mysqlclient

[连接数据库错误 image not found](https://stackoverflow.com/questions/49194719/authentication-plugin-caching-sha2-password-cannot-be-loaded)
