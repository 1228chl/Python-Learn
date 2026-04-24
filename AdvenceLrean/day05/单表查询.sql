# 选择数据库
USE MY_DB;
# 创建商品表
DROP TABLE IF EXISTS PRODUCTS;
CREATE TABLE IF NOT EXISTS PRODUCTS
(
    ID          INT PRIMARY KEY AUTO_INCREMENT COMMENT '商品ID',
    NAME        VARCHAR(24)    NOT NULL COMMENT '商品名称',
    PRICE       DECIMAL(10, 2) NOT NULL COMMENT '商品价格',
    SCORE       DECIMAL(5, 2) COMMENT '商品评分，可以为空',
    IS_SELF     VARCHAR(8) COMMENT '是否自营',
    CATEGORY_ID INT COMMENT '商品类别ID'
) COMMENT ='商品信息表';
# 创建商品类别表
DROP TABLE IF EXISTS CATEGORY;
CREATE TABLE IF NOT EXISTS CATEGORY
(
    ID   INT PRIMARY KEY AUTO_INCREMENT COMMENT '商品类别ID',
    NAME VARCHAR(24) NOT NULL COMMENT '类别名称'
) COMMENT ='商品类别表';
# 插入数据: insert into 表名 (字段名,字段名) values(字段值,字段值),(字段值,字段值);
# 添加测试数据
INSERT INTO
    CATEGORY
VALUES
    (1, '手机'),
    (2, '电脑'),
    (3, '美妆'),
    (4, '家居');

INSERT INTO
    PRODUCTS
VALUES
    (1, '华为Mate50', 5499.00, 9.70, '自营', 1),
    (2, '荣耀80', 2399.00, 9.50, '自营', 1),
    (3, '荣耀80', 2199.00, 9.30, '非自营', 1),
    (4, '红米note 11', 999.00, 9.00, '非自营', 1),
    (5, '联想小新14', 4199.00, 9.20, '自营', 2),
    (6, '惠普战66', 4499.90, 9.30, '自营', 2),
    (7, '苹果Air13', 6198.00, 9.10, '非自营', 2),
    (8, '华为MateBook14', 5599.00, 9.30, '非自营', 2),
    (9, '兰蔻小黑瓶', 1100.00, 9.60, '自营', 3),
    (10, '雅诗兰黛粉底液', 920.00, 9.40, '自营', 3),
    (11, '阿玛尼红管405', 350.00, NULL, '非自营', 3),
    (12, '迪奥996', 330.00, 9.70, '非自营', 3);

######################################################################################
# todo:1-基础查询
# select 字段名1, 字段名2, ... from 表名;
-- 需求1: 查看所有商品
# *: 所有列
SELECT *
FROM
    PRODUCTS;

SELECT
    ID,
    NAME,
    PRICE,
    SCORE,
    IS_SELF,
    CATEGORY_ID
FROM
    PRODUCTS;

-- 需求2: 查看所有商品的名称和价格
SELECT
    NAME,
    PRICE
FROM
    PRODUCTS;

-- 需求3: 查看所有商品的名称和价格,要求给字段名起别名展示
# as(alias): 起别名  对字段 表 都可以起别名  也可以省略as
SELECT
    NAME  AS '商品名称',
    PRICE AS NEW_PRICE
FROM
    PRODUCTS;

-- 需求4: 查看所有商品的名称和价格,要求给表名起别名并使用
SELECT
    P.NAME     '商品名称',
    P.PRICE AS NEW_PRICE
FROM
    PRODUCTS AS P;

-- 需求5: 查看所有的分类编号,要求去重展示
# distinct: 去重  对指定字段进行去重
SELECT DISTINCT
    CATEGORY_ID,
    IS_SELF
FROM
    PRODUCTS;