# 一个sql语句可以单行 或 多行书写, 以 分号; 结尾
SHOW DATABASES;
SHOW
    DATABASES;
SHOW DATABASES;

# 单行注释和多行注释
-- 这是单行注释  -- + 注释内容  ctrl+/
# 这还是单行注释  # + 注释内容  ctrl+/

# 多行注释 /*注释内容*/  ctrl+shift+/
/*
特朗普爱炒股还爱大战,
他是炒股中最会打战的,
还是打战里面最会炒股的
*/

# 代码书写 建议关键字 类型 大写

#########################################################################################

# todo: DDL之数据库操作
# 创建数据库
CREATE DATABASE MY_DB;
# 如果数据库不存在再创建, 存在就忽略
CREATE DATABASE IF NOT EXISTS MY_DB;
# 创建数据库指定编码
CREATE DATABASE IF NOT EXISTS MY_DB2 CHARSET 'utf8';
CREATE DATABASE IF NOT EXISTS MY_DB2 CHARACTER SET 'utf8';

# 删除数据库
DROP DATABASE MY_DB2;
DROP DATABASE IF EXISTS MY_DB2;

# 使用数据库
USE MY_DB;

# 查看所有库
SHOW DATABASES;

# 查看当前库
SELECT DATABASE();

# 查看建库语句
SHOW CREATE DATABASE MY_DB;


##########################################################################################
# todo:2-DDL之表操作
# 操作表的前提: 先创建库,并使用它
# 需求:创建学生表,用于存储学生的姓名,年龄,身高,生日信息
-- 创建表时需要有 列名 类型 [约束]
CREATE TABLE IF NOT EXISTS STU
(
    ID       INT PRIMARY KEY COMMENT '编号',
    NAME     VARCHAR(100) COMMENT '姓名',
    AGE      INT NOT NULL COMMENT '年龄',
    HEIGHT   DOUBLE,
    BIRTHDAY DATE
) COMMENT '学生表';

# 查看所有表
SHOW TABLES;

# 查看表结构
DESC STU;

# 查看建表语句
SHOW CREATE TABLE STU;

# 修改表名
# rename table 原表名 to 新表名;
RENAME TABLE STU TO STUDENT;

# 删除表
DROP TABLE IF EXISTS STUDENT;


#############################################################################
# todo: DML 数据操作语言  表数据的增删改操作
# 插入数据
# insert into 表名(字段名, 字段名, ...) vlaues (), (), ...
# 指定字段插入一条数据
INSERT INTO
    MY_DB.STU(ID, NAME, AGE)
VALUES
    (1, '张三', 18);
# 指定字段插入多条数据
INSERT INTO
    STU(ID, NAME, AGE, HEIGHT) VALUE (2, '李四', 20, 180), (3, '王五', 25, 175);

# 注意:不指定字段本质代表指定所有字段
# 不指定字段插入一条数据
INSERT INTO
    STU
VALUES
    (4, '赵六', 26, 188, '1990-10-01');
# 不指定字段插入多条数据
INSERT INTO
    STU
VALUES
    (5, '孙七', 30, 170, '1995-05-01'),
    (6, '川普', 74, 180, '1968-07-22');


# 修改数据
# UPDATE 表名 SET 字段名 = 新值, 字段名 = 新值 WHERE 条件;
# 修改李四的年龄为28
UPDATE STU
SET
    AGE = 28
WHERE
    NAME = '李四';

# 修改王五和张三的年龄为39, 身高为175
UPDATE STU
SET
    AGE   = 39,
    HEIGHT=175
WHERE
     NAME = '张三'
  OR NAME = '王五';

# 修改张三的id为7,年龄为40
UPDATE STU
SET
    ID  = 7,
    AGE = 40
WHERE
    NAME = '张三';

# 注意: 如果没有加条件,修改的是所有数据(慎用!!!)
# 先报黄, 点击excute强制执行
UPDATE STU
SET
    AGE = 20;


# 删除数据
# delete from 表名 where 删除条件
# 删除id为4的记录
DELETE
FROM
    STU
WHERE
    ID = 4;
# 删除id为2,以及id为3的记录
DELETE
FROM
    STU
WHERE
     ID = 2
  OR ID = 3;

# 注意: 如果不加条件删除的是所有数据(慎用!!!)
DELETE FROM STU;
# 为了演示truncate删除数据,重新插入多条
# truncate也能删除所有数据
TRUNCATE TABLE STU;