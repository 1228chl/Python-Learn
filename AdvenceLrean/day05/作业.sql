# (1)创建数据库名称为db_student1
create database db_student1;

# (2)创建数据库名称为db_hw1
create database db_hw1;

# (3)切换数据库为db_student1
use db_student1;

# (4)查看当前使用的是哪个数据库；
select database();

# (5)查看所有数据库
show databases ;

# (6)删除数据库db_student1；
drop database db_student1;

# (7)查看当前使用的是哪个数据库；
select database();

# (8)切换数据库到db_hw1。
use db_hw1;

show tables ;

# topic-2
# (1)在数据库db_hw1中创建一个数据student表，有用户sid、姓名name、性别sex、生日birthday；
create table student(
    sid int,
    name varchar(20),
    sex varchar(1) default '男',
    birthday datetime
);

# (2)查看数据表中的字段信息
select * from student;

# (3)查看创建数据表语句；
desc student;

# (4)再次创建一个数据little_student表,只有name一个字段
create table little_student(
    name varchar(20)
);

# (5)查看所有表
show tables ;

# (6)删除little_student表
drop table little_student;

# (7)修改student数据表名为tb_student。
alter table student rename to tb_student;

# (8)再次查看所有表
show tables ;


#topic-3
# （1）使用数据库db_hw1
use db_hw1;

# （2）在该库中创建一个student表，字段有编号、学号、姓名、语文成绩、英语成绩、数学成绩等；
create table student(
    id int,
    stu_id varchar(20),
    name varchar(20),
    language float,
    english float,
    math float
);

# （3）对于这些字段，要求：编号是整型，学号是字符串；


# （4）给student表添加如下10条数据；
insert into student
values
    (1, '20210908001','张王明', 89, 78, 90),
    (2, '20210908002', '李进', 67, 53, 95),
    (3, '20210908003', '王俊', 87, 78, 77),
    (4, '20210908004', '李云云', 80, 98, 92),
    (5, '20210908005', '谢来财', 82, 84, 67),
    (6, '20210908006', '张进宝', 55, 85, 89),
    (7, '20210908007', '黄蓉儿', 79, 86, 90),
    (8, '20210908008', '刘小雪', 71, 90, 91),
    (9, '20210908009', '夏金章', 89, 91, 96),
    (10, '20210908010', '杨洋', 83, 65, 90);

select * from student;

# （5）修改id为4的这条数据的语文成绩为88，删除id为10的这条数据内容；
use db_hw1;
update student set language = 88 where id = 4;
delete from student where id=10;


