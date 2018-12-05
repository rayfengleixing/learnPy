# Python操作Mysql

[TOC]

## 模块安装

- pip install pymysql

## 创建连接

- conn = pymysql.connection()  

## 获取游标

- cursor = conn.cursor()

## 执行操作
- 执行语句
	- cursor.execute(sql[select])
	- cursor.execute(sql[update, insert, delete]) //使用conn.commit()提交事务，conn.rollback()回滚事务
- 获取并处理数据
	- execute(sql)
	- rowcount() //最后一次执行execute()操作返回或影响的行数
	- fetchone() //得到结果集的下一行
	- fetchmany(3) //得到结果集的下三行
	- fetchall() //得到结果集剩下的所有行
    - executemany(sql, args)
    - lastrowid()
- connection对象支持的方法
    - cursor()
    - commit()
    - rollback()
    - close()
- cursor游标对象支持的方法
    - cursorscroll()
    - cursor.scroll(-1, mode='relative') //相对移动
    - cursor.scroll(0, mode='absolute') //绝对移动，0为下标

## 关闭游标

- cursor.close()

## 关闭连接

- conn.close()
