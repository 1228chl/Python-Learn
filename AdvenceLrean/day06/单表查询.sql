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

##################################################################################
# todo:2-条件查询
# where 限制行数据   select...from 之间是添加字段, 限制列数据
-- 比较运算符: =  >  <  >=  <=  !=  <>
-- 需求1: 查询所有'自营'的商品
SELECT *
FROM
    PRODUCTS
WHERE
    IS_SELF = '自营';

-- 需求2: 查询评分在'9.50'(不含)以上的商品
SELECT *
FROM
    PRODUCTS
WHERE
    SCORE > 9.5;

-- 需求3: 查询评分在'9.50'(含)以上的商品
SELECT *
FROM
    PRODUCTS
WHERE
    SCORE >= 9.50;

-- 需求4: 查询价格在999(不含)以下的商品
SELECT
    NAME,
    P.PRICE
FROM
    PRODUCTS P
WHERE
    P.PRICE < 999;

-- 需求5: 查询价格在999(含)以下的商品
SELECT *
FROM
    PRODUCTS P
WHERE
    P.PRICE <= 999;

-- 需求6: 查询评分不等于9.30的商品
SELECT *
FROM
    PRODUCTS
WHERE
    SCORE != 9.30;

# <> : 不等于
SELECT *
FROM
    PRODUCTS
WHERE
    SCORE <> 9.30;

# todo:3-逻辑查询
-- and:并且  or:或者  not:取反
-- 需求1: 查询 自营商品 中所有 价格大于2000 的商品信息
SELECT *
FROM
    PRODUCTS
WHERE
      IS_SELF = '自营'
  AND PRICE > 2000;

-- 需求2: 查询 商品评分 在9.0(含)-9.5(含)之间的商品信息
SELECT *
FROM
    PRODUCTS
WHERE
      SCORE >= 9.0
  AND SCORE <= 9.5;

-- 需求3: 查询 商品价格 在1000(含)到3000(含)之间的商品信息
SELECT *
FROM
    PRODUCTS
WHERE
      PRICE >= 1000
  AND PRICE <= 3000;

-- 需求4: 查询 价格 是999 或者 2199 或者 2399的商品
SELECT *
FROM
    PRODUCTS
WHERE
     PRICE = 999
  OR PRICE = 2199
  OR PRICE = 2399;

-- 需求5: 查询 商品名称 是'华为Mate50' 或者 '荣耀80'的商品
SELECT *
FROM
    PRODUCTS P
WHERE
     P.NAME = '华为Mate50'
  OR P.NAME = '荣耀80';

-- 需求6: 查询商品 不是 自营 的商品
SELECT *
FROM
    PRODUCTS
WHERE
    NOT (IS_SELF = '自营');

-- 需求7: 查询 商品价格 不在 1000(不含)到3000(不含)之间的商品
SELECT *
FROM
    PRODUCTS
WHERE
    NOT (PRICE > 1000 AND PRICE < 3000);

SELECT *
FROM
    PRODUCTS
WHERE
     PRICE <= 1000
  OR PRICE >= 3000;

# todo:4-范围查询
# [NOT] BETWEEN ... AND ...:默认包含起始和结束(左闭右闭)  连续的范围
# [NOT] IN (值1, 值2, ...): 不连续的值   ※※※
-- 需求1: 查询商品价格在1000(含)到3000(含)之间的商品信息
SELECT *
FROM
    PRODUCTS
WHERE
    PRICE BETWEEN 1100 AND 2399;

SELECT *
FROM
    PRODUCTS
WHERE
      PRICE >= 1000
  AND PRICE <= 3000;

-- 需求2: 查询商品不在1000(包含)到3000(包含)之间的商品
SELECT *
FROM
    PRODUCTS
WHERE
    PRICE NOT BETWEEN 1000 AND 3000;

-- 需求3: 查询价格是999或者2199或者2399的商品
SELECT *
FROM
    PRODUCTS
WHERE
    PRICE IN (999, 2199, 2399);

SELECT *
FROM
    PRODUCTS
WHERE
    PRICE NOT IN (999, 2199, 2399);

-- 需求4: 查询商品名称是'华为Mate50'或者'荣耀80'的商品
SELECT *
FROM
    PRODUCTS
WHERE
    NAME IN ('华为Mate50', '荣耀80');

# 查询商品名称是'华为Mate50'或者'荣耀80'并且 价格大于2500 的商品
SELECT *
FROM
    PRODUCTS
WHERE
      NAME IN ('华为Mate50', '荣耀80')
  AND PRICE > 2500;

# todo:5-模糊查询
-- 关键字: [NOT] like   符号 %:任意多个(包含0或1)字符  _:任意1个字符
-- 需求1: 查询 商品名称 以 '华'开头 的商品信息
SELECT *
FROM
    PRODUCTS
WHERE
    NAME LIKE '华%';

-- 不以 '华'开头
SELECT *
FROM
    PRODUCTS
WHERE
    NAME NOT LIKE '华%';

-- 需求2: 查询商品名称以'华'开头并且8个字符的商品信息
SELECT *
FROM
    PRODUCTS
WHERE
    NAME LIKE '华_______';

-- 需求3: 查询商品名称以'66'结尾商品信息
SELECT *
FROM
    PRODUCTS
WHERE
    NAME LIKE '%66';

-- 需求4: 查询商品名称中包含'兰'字的商品信息
SELECT *
FROM
    PRODUCTS
WHERE
    NAME LIKE '%兰%';

-- 需求5: 查询商品名称中第3个字是'兰'字的商品信息
SELECT *
FROM
    PRODUCTS
WHERE
    NAME LIKE '__兰%';