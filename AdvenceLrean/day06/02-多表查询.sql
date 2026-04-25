# 使用库
USE MY_DB;
# 创建商品表
DROP TABLE IF EXISTS PRODUCTS;
CREATE TABLE IF NOT EXISTS PRODUCTS
(
    ID          INT PRIMARY KEY AUTO_INCREMENT, -- 商品ID
    NAME        VARCHAR(24)    NOT NULL,        -- 商品名称
    PRICE       DECIMAL(10, 2) NOT NULL,        -- 商品价格
    SCORE       DECIMAL(5, 2),                  -- 商品评分，可以为空
    IS_SELF     VARCHAR(8),                     -- 是否自营
    CATEGORY_ID INT                             -- 商品类别ID
);

# 创建分类表
DROP TABLE IF EXISTS CATEGORY;
CREATE TABLE IF NOT EXISTS CATEGORY
(
    ID   INT PRIMARY KEY AUTO_INCREMENT, -- 商品类别ID
    NAME VARCHAR(24) NOT NULL            -- 类别名称
);

# 添加分类数据
INSERT INTO
    CATEGORY
VALUES
    (1, '手机'),
    (2, '电脑'),
    (3, '美妆'),
    (4, '家居');
# 添加商品数据
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
    (12, '迪奥996', 330.00, 9.70, '非自营', 3),
    (13, '百草味紫皮腰果', 9, 5.00, NULL, NULL);

################################################################################################################
# todo:1-交叉连接(cross join): 笛卡尔积, 将两个表所有行都进行匹配  行数=A表行数*B表行数  一般很少使用
# 隐式交叉连接格式: select 字段名 from 左表,右表;
SELECT
    C.ID,
    C.NAME,
    P.*
FROM
    CATEGORY C,
    PRODUCTS P;

# 显式交叉连接格式: select 字段名 from 左表 cross join 右表;
SELECT *
FROM
    CATEGORY
        CROSS JOIN PRODUCTS;

SELECT *
FROM
    CATEGORY
        JOIN PRODUCTS
ORDER BY
    CATEGORY.ID;

#######################################################################################################
# todo:2-内连接(innner join): 两表交集, 将两个表中相同的字段进行匹配
# 隐式内连接格式: select 字段名 from 左表,右表 where 条件;
SELECT
    C.ID,
    P.CATEGORY_ID,
    C.NAME,
    P.ID,
    P.NAME,
    P.PRICE,
    P.SCORE,
    P.IS_SELF
FROM
    CATEGORY C,
    PRODUCTS P
WHERE
    C.ID = P.CATEGORY_ID;

# 显式内连接格式: select 字段名 from 左表 inner join 右表 on 条件;
SELECT *
FROM
    CATEGORY C
        INNER JOIN PRODUCTS P ON C.ID = P.CATEGORY_ID;


SELECT *
FROM
    CATEGORY C
        -- 多个关联条件同时成立
        JOIN PRODUCTS P ON C.ID = P.CATEGORY_ID AND C.NAME = P.NAME;

#######################################################################################################
# todo:3-左外连接(left join): 左表所有行, 右表匹配的行, 匹配不上的用NULL填充  最常用
# from后是左表 join后是右表 左连接最常用 右连接可以通过左连接替代实现
# select 字段名 from 左表 left join 右表 on 条件;
SELECT *
FROM
    CATEGORY
        LEFT JOIN PRODUCTS ON CATEGORY.ID = CATEGORY_ID;

#######################################################################################################
# todo:4-右外连接(right join): 右表所有行, 左表匹配的行, 匹配不上的用NULL填充
# select 字段名 from 左表 right join 右表 on 条件;
SELECT
    P.*,
    C.*
FROM
    CATEGORY C
        RIGHT JOIN PRODUCTS P ON P.CATEGORY_ID = C.ID;

# 左连接实现右连接效果
SELECT *
FROM
    PRODUCTS P
        LEFT JOIN CATEGORY C ON P.CATEGORY_ID = C.ID;

#######################################################################################################
# todo:5-全外连接: 左外连接 + 右外连接
-- union -> 上下连接两张表 列要一一对应(列数相同, 列名可以不同) 去重
(SELECT
     C.ID   AS CID,
     C.NAME AS CNAME,
     P.*
 FROM
     CATEGORY C
         LEFT JOIN PRODUCTS P ON C.ID = P.CATEGORY_ID)
UNION
(SELECT
     C.*,
     P.*
 FROM
     CATEGORY C
         RIGHT JOIN PRODUCTS P ON C.ID = P.CATEGORY_ID);

-- union all -> 上下连接两张表 不去重
SELECT
    C.ID   AS CID,
    C.NAME AS CNAME,
    P.*
FROM
    CATEGORY C
        LEFT JOIN PRODUCTS P ON C.ID = P.CATEGORY_ID
UNION ALL
SELECT
    C.*,
    P.*
FROM
    CATEGORY C
        RIGHT JOIN PRODUCTS P ON C.ID = P.CATEGORY_ID;

#######################################################################################################
# todo:6-自连接  用的少
# 自连接: 自己和自己连接  字段中有父子关系 或者 时间差关系(1月 2月 3月)
# 注意点: 一个表与自身连接, 自连接必须添加表别名
-- 查询'江苏省'下所有城市
SELECT *
FROM
    AREAS SHENG
        JOIN AREAS SHI ON SHENG.ID = SHI.PID
WHERE
    SHENG.TITLE = '江苏省';


-- 查询'宿迁市'下所有的区县
SELECT *
FROM
    AREAS SHI
        JOIN AREAS XIAN ON SHI.ID = XIAN.PID
WHERE
    SHI.TITLE = '宿迁市';


-- 查询'安徽省'下所有的市,以及市下面的区县信息
SELECT *
FROM
    AREAS SHENG
        JOIN AREAS SHI ON SHENG.ID = SHI.PID
        JOIN AREAS XIAN ON XIAN.PID = SHI.ID
WHERE
    SHENG.TITLE = '安徽省';

#######################################################################################################
# todo:7-子查询
-- 需求1: 求商品价格大于平均价的商品信息

-- 需求2: 求商品价格最高的商品信息(考虑并列情况)

-- 需求3: 查询'河北省'下所有城市

-- 需求4: 查询'邯郸市'下所有区县

select * from areas where id like '36%';