# 新闻 mysql 表

ID: 新闻的唯一标识
types: 新闻的类型
title: 新闻的标题
content: 新闻的内容
created_at: 新闻添加的时间
image: 新闻的缩略图
author: 新闻的作者
view_count: 新闻的浏览量
is_valid: 删除标记

```sql
# 创建新闻数据库
CREATE DATABASE `news`;

# 切换到 news 数据库
USE `news`;

SHOW DATABASES;

-- 创建表
-- ID: 新闻的唯一标识
-- title: 新闻的标题
-- content: 新闻的内容
-- created_at: 新闻添加的时间
-- types: 新闻的类型
-- image: 新闻的缩略图
-- author: 新闻的作者
-- view_count: 新闻的浏览量
-- is_valid: 删除标记
CREATE TABLE `news` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(200) NOT NULL,
	`content` VARCHAR(2000) NOT NULL,
	`created_at` DATETIME NOT NULL,
	`types` VARCHAR(100) NOT NULL,
	`image` VARCHAR(300) NULL,
	`author` VARCHAR(20) NULL,
	`view_count` INT DEFAULT 0,
	-- 默认有效
	`is_valid` SMALLINT DEFAULT 1,
	PRIMARY KEY(`id`)
) DEFAULT CHARSET='utf8';

-- 插入数据
INSERT INTO `news` (`id`, `title`, `content`, `created_at`, `types`, `image`, `author`) VALUE (1, '小李杀人了？？？', '德玛西亚万岁', NOW(), '热点', 'https://www.image.com', 'newming');

-- 查询数据
SELECT * FROM `news`;
```

# teacher

```sql
CREATE DATABASE `school`;

-- 使用数据库
USE `school`;

-- 创建表 最后指定表的编码
CREATE TABLE `student` (
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(20) NOT NULL,
	`nickname` VARCHAR(20) NULL,
	`sex` SMALLINT NOT NULL,
	`in_time` DATETIME NULL
) DEFAULT CHARSET 'utf8';

-- 插入单条数据，不指定 key 值，只写 value 的话需要注意和上边的表的顺序一致
-- INSERT INTO `student` VALUE(2, '张三', '三哥', 0, NOW());
-- 插入单条数据，指定插入的 列 名，这时不插入 id , id 会按照创建表的规则自动生成，自动加一
INSERT INTO `student` (`name`, `nickname`, `sex`, `in_time`) VALUE ('李四', '小李飞刀', 0, NOW());

-- 插入多条数据，可以换行，一行一个，注意 values 的分号
INSERT INTO `student` (`name`, `nickname`, `sex`, `in_time`) VALUES
	('李四', '小李飞刀', 0, NOW()),
	('王五', '小李飞刀2', 0, NOW()),
	('李青', '小李飞刀', 0, NOW())
;

-- 查询语句
-- 查询 student 表里的全部数据
SELECT * FROM `student`;
-- 查询 student 表里的全部数据的 name, sex 字段
SELECT `name`, `sex` FROM `student`;
-- 查询 student 中男生的 id name，并且按照 id 倒序
SELECT `id`, `name` FROM `student` WHERE `sex`=1 ORDER BY `id` DESC;
-- 注意 SELECT, WHERE, ORDER BY 的顺序不能乱
-- LIMIT offset, count 分页查询，其中 offset 代表偏移量，即跳过多少条数据，count 是查询几条
SELECT `id`, `name` FROM `student` WHERE `sex`=0 ORDER BY `id` DESC LIMIT 2, 3;

-- 更新修改数据
-- 将男生的性别改成女
UPDATE `student` SET `sex`=0 WHERE `sex`=1;
-- 将 id 大于 6 的性别改为 男
UPDATE `student` SET `sex`=1 WHERE `id` > 6;

-- 删除数据
-- 将男生删除
DELETE FROM `student` WHERE `sex`=1;
```
