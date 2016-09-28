# -*- coding:utf8 -*-

import MySQLdb

try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='999999', db='pythonbook', port=3306)
        cur = conn.cursor()
        cur.execute('select * from category')
        for row in cur.fetchall():
                print row


        cur.close()
        conn.close()
except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])



# #coding=utf-8
# import MySQLdb
#
# conn= MySQLdb.connect(
#         host='localhost',
#         port = 3306,
#         user='root',
#         passwd='123456',
#         db ='test',
#         )
# cur = conn.cursor()
#
# #创建数据表
# #cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
#
# #插入一条数据
# #cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
#
#
# #修改查询条件的数据
# #cur.execute("update student set class='3 year 1 class' where name = 'Tom'")
#
# #删除查询条件的数据
# #cur.execute("delete from student where age='9'")
#
# cur.close()
# conn.commit()
# conn.close()