# 设置初始用户名和密码，如果不设置请注释掉
user_pass = ['admin', '123456']

# 配置数据库
db = [
    '192.168.68.238',  # hostname
    3306,  # port
    'root',  # username
    '123456',  # password
    'mysql'  # database
]

# 记录用户名
show_user = []

# 列的数据
row_data = []

# 学生信息列表
Student_data = []

# 定位序号
select_s = []

# 数据存放
result = []

# 查询数据存放
result_data = []

# 更新数据
re_data = []

# 存储登录的用户名
login_username = ''

# 数据库初始化
# 创建数据库
mysql_create = '''create database student character set utf8;'''
mysql_users = '''
CREATE TABLE `student`.`users`  (
  `name` varchar(255) NULL,
  `passwd` varchar(255) NULL
);'''
mysql_datas = '''
CREATE TABLE `student`.`datas`  (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NULL,
  `class` varchar(255) NULL,
  `yuwen` varchar(255) NULL,
  `math` varchar(255) NULL,
  `english` varchar(255) NULL,
  PRIMARY KEY (`id`)
);'''

# 创建一个空列表，用于存储导入值
cell_values = []

# 查询用户名密码
query_name = '''SELECT count(*) FROM `student`.`users` where name='{}' limit 1;'''
query_pass = '''SELECT * FROM student.users WHERE name = '{}' AND passwd = '{}';'''

# 写入用户名和密码语句
sql_pass = '''INSERT INTO student.users (name, passwd) VALUES ('{}', MD5('{}'));'''

# 写入学生信息语句
insert_date = '''INSERT INTO student.datas (id, name, class, yuwen, math, english) VALUES (%s, %s, %s, %s, %s, %s);'''

# 查询usres表是否有数据
show_user_sql = '''SELECT * FROM student.users;'''

# 判断是否有重复数据
if_insert_data = '''SELECT id, name, class, yuwen, math, english FROM student.datas WHERE id = %s;'''

# 查询数据内容
query_data = '''SELECT id,name,class,yuwen,math,english FROM student.datas;'''

# 刷新数据
redata_sql = '''FLUSH PRIVILEGES;'''

# 删除数据
del_data_sql = '''DELETE FROM student.datas WHERE id = %s AND name = %s AND class =%s AND yuwen = %s AND math = %s AND english = %s;'''

# 更新数据
alter_data_sql = '''UPDATE student.datas SET name=%s, class=%s, yuwen=%s, math=%s, english=%s WHERE id=%s;'''

# 模糊查询数据
vague_query_data_sql = '''SELECT * FROM student.datas WHERE id LIKE %s or name LIKE %s or class LIKE %s or yuwen LIKE %s or math LIKE %s or english LIKE %s;'''

# 导入数据
load_data_sql = '''INSERT INTO student.datas (id, name, class, yuwen, math, english) VALUES (%s, %s, %s, %s, %s, %s)'''

# 修改用户名密码
repass_sql = '''UPDATE student.users SET passwd=%s WHERE name=%s;'''

sql_user_2 = '''INSERT INTO student.users (name, passwd) VALUES ({}, MD5({}));'''

# 删除用户
del_user_sql = '''delete from student.users where name=%s;'''
