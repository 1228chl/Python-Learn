# topic-1
# 请说一说数据库语言有哪几个分类，并阐述下该分类下常用的SQL关键字。
/*
ddl 定义语句
create、drop、alter、show
dcl 控制语句
grant、revoke
dml 管理语句
insert into、delete、update set、drop
dql 查询语句
select from、where、like、between、join、group by、order by、having、distinct、limit
*/

# topic-2
# 数据表中<null>是什么意思？请说说你的理解。
/*
代表空值，相当于一个占位符，可以等待值来补充，而不是不存在
*/

# topic-3
# 请简述where和having的区别
/*
where是条件判断的关键字，而having是在group by分组后过滤使用的关键字，其中将having放在where前面使用，最好配合group by一起使用
 */

# topic-4
drop table student;
create table student
(
    id      int primary key auto_increment not null,
    stuno   varchar(20),
    name    varchar(20),
    chinese double,
    english double,
    math    double
);



INSERT INTO student(id, stuno, name, chinese, english, math)
VALUES (1, '20210908001', '张王明', 89, 78, 90),
       (2, '20210908002', '李进', 67, 53, 95),
       (3, '20210908003', '王俊', 87, 78, 77),
       (4, '20210908004', '李云云', 80, 98, 92),
       (5, '20210908005', '谢来财', 82, 84, 67),
       (6, '20210908006', '张进宝', 55, 85, 89),
       (7, '20210908007', '黄蓉儿', 79, 86, 90),
       (8, '20210908008', '刘小雪', 71, 90, 91),
       (9, '20210908009', '夏金章', 89, 91, 96),
       (10, '20210908010', '杨洋', 83, 65, 90);

# （1）查询表中所有学生的信息；
select *
from student;

# （2）查询表中所有学生的姓名和对应的英语成绩；
select english
from student;

# （3）过滤数据表中，语文成绩值的重复数据；
select distinct chinese
from student;

# （4）统计每个学生的总分；
select id, chinese + english + math total
from student;

# （5）在所有学生总分数上加10分特长分；
select id, chinese + english + math + 10 total
from student;

# （6）查询英语成绩大于90分的同学；
select *
from student
where english > 90;

# （7）查询总分大于200分的所有同学；
select *
from student
where chinese + english + math > 200;

# （8）查询英语分数在 80－90之间的同学；
select *
from student
where english >= 80
  and english <= 90;

# （9）查询英语分数不在 80－90之间的同学；
select *
from student
where not english >= 80
   or not english <= 90;

# （10）查询数学分数为89,90,91的同学；
select *
from student
where english in (89, 90, 91);

# （11）查询所有姓李的学生英语成绩；
select name, english
from student
where name like '李%';

# （12）查询数学分80并且语文分80的同学；
select name
from student
where math = 80
  and chinese = 80;

# （13）查询英语80或者总分200的同学。
select *
from student
where english = 80
   or chinese + english + math = 200;


# topic-5
create table students
(
    studentNo int primary key auto_increment,
    name      varchar(100),
    sex       varchar(100),
    hometown  varchar(100),
    age       int,
    class_id  int,
    card      varchar(100)
);

insert into students(name, sex, hometown, age, class_id, card)
values ('王昭君', '女', '北京', 20, 1, '340322199001247654'),
       ('诸葛亮', '男', '上海', 18, 2, '340322199002242354'),
       ('张飞', '男', '南京', 24, 3, '340322199003247654'),
       ('白起', '男', '安徽', 22, 4, '340322199005247654'),
       ('大乔', '女', '天津', 19, 3, '340322199004247654'),
       ('孙尚香', '女', '河北', 18, 1, '340322199006247654'),
       ('百里玄策', '男', '山西', 20, 2, '340322199007247654'),
       ('小乔', '女', '河南', 15, 3, null),
       ('百里守约', '男', '湖南', 21, 1, ''),
       ('妲己', '女', '广东', 26, 2, '340322199607247654'),
       ('李白', '男', '北京', 30, 4, '340322199005267754'),
       ('孙膑', '男', '新疆', 26, 3, '340322199000297655');

# 1. 查询学生"百里守约"的基本信息
select *
from students
where name = '百里守约';

# 2. 查询学生"百里守约"或”百里玄策”的基本信息
select *
from students
where name = '百里守约'
   or name = '百里玄策';

# 3. 查询姓"张"学生的姓名，年龄，班级
select name, age, students.class_id
from students
where name like '张%';

# 4. 查询姓名中含有"约"字的学生的基本信息
select *
from students
where name like '%约%';

# 5. 查询姓名长度为三个字，姓“孙”的学生的学号，姓名，年龄，班级，身份证号
select students.studentNo, name, age, students.class_id, students.card
from students
where name like '孙__';

# 6. 查询姓"百"或者姓”孙”的学生的基本信息
select *
from students
where name like '百%'
   or name like '孙%';

# 7. 查询姓"百"并且家乡是"山西"的学生信息
select *
from students
where name like '百%'
  and hometown = '山西';

# 8. 查询家乡是"北京"、"新疆"、"山东"、"上海"的学生的信息
select *
from students
where hometown in ('北京', '新疆', '山东', '上海');

# 9. 查询姓"孙"，但是家乡不是"河北"的学生信息
select *
from students
where name like '孙%'
  and not hometown = '河北';

# 10. 查询家乡不是"北京"、"新疆"、"山东"、"上海"的学生的信息
select *
from students
where hometown not in ('北京', '新疆', '山东', '上海');

# 11. 查询全部学生信息，并按照“性别”排序
select *
from students
order by sex;

# 12. 查询所有男生，并按年龄升序排序
select *
from students
where sex = '男'
order by age;

# 13. 统计共有多少个学生
select count(1)
from students;

# 14. 统计年龄大于20岁的学生有多少个
select count(1)
from students
where age > 20;

# 15. 统计男生的平均年龄
select avg(students.age)
from students
where sex = '男';

# 16. 查询1班学生中的最大年龄是多少
select max(students.age)
from students
where class_id = 1;

# 17. 统计2班男女生各有多少人
select count(1), sex
from students
where students.class_id = 2
group by sex;

# 18. 查询年龄最小的学生的全部信息
select *
from students
where age = (select min(age) from students);

# topic-6
CREATE TABLE emp
(
    empno    INT,
    ename    VARCHAR(50),
    job      VARCHAR(50),
    mgr      INT, -- 上级领导编号
    hiredate DATE,-- 入职日期
    sal      INT,
    comm     INT, -- 奖金
    deptno   INT  --  部门编号
);

INSERT INTO emp
VALUES (7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800, NULL, 20),
       (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600, 300, 30),
       (7521, 'WARD', 'SALESMAN', 7698, '1981-02-22', 1250, 500, 30),
       (7566, 'JONES', 'MANAGER', 7839, '1981-04-02', 2975, NULL, 20),
       (7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28', 1250, 1400, 30),
       (7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01', 2850, NULL, 30),
       (7782, 'CLARK', 'MANAGER', 7839, '1981-06-09', 2450, NULL, 10),
       (7788, 'SCOTT', 'ANALYST', 7566, '1987-04-19', 3000, NULL, 20),
       (7839, 'KING', 'PRESIDENT', NULL, '1981-11-17', 5000, NULL, 10),
       (7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08', 1500, 0, 30),
       (7876, 'ADAMS', 'CLERK', 7788, '1987-05-23', 1100, NULL, 20),
       (7900, 'JAMES', 'CLERK', 7698, '1981-12-03_四大激活函数', 950, NULL, 30),
       (7902, 'FORD', 'ANALYST', 7566, '1981-12-03_四大激活函数', 3000, NULL, 20),
       (7934, 'MILLER', 'CLERK', 7782, '1982-01-23', 1300, NULL, 10);

-- 1、按员工编号升序排列不在10号部门工作的员工信息
select * from emp where not deptno = 10 order by empno;

-- 2、查询姓名第二个字母不是”A”且薪水大于800元的员工信息，按年薪降序排列
select * from emp where ename not like '_A%' and sal > 800 order by (sal *12)+ifnull(comm,0) desc ;

# 注意: 此处需要将空值做判空处理 IFNULL(EXP1,EXP2) , exp1不为空就是 exp1，否则是exp2

-- 3、求每个部门的平均薪水
select deptno,avg(emp.sal) from emp group by deptno;

-- 4、求各个部门的最高薪水
select emp.deptno,max(emp.sal) from emp group by deptno;

-- 5、求每个部门每个岗位的最高薪水
select emp.job,max(emp.sal) from emp group by job;

-- 6、求平均薪水大于2000的部门编号
select emp.deptno from emp group by deptno having avg(sal)>2000;

-- 7、将部门平均薪水大于1500的部门编号列出来，按部门平均薪水降序排列
select emp.deptno,avg(sal) from emp group by deptno having avg(sal)>1500 order by avg(sal) desc ;

