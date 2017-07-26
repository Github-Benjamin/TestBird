#coding:utf-8

import time
import web
import captcga
import random

urls = (
    '/','Index',
    '/message','Message',
)

app = web.application(urls,globals())
db = web.database(dbn='mysql',host='127.0.0.1',port=3306,user='root',pw='',db='demo',charset='utf8')
renter = web.template.render('templates')

class Index(object):
    def GET(self):
        return renter.index()
    def POST(self):
        return renter.index()


class Message(object):
    def GET(self):
        global result
        # 初始化一个列表
        li = []
        # 26个字母在ASCII对照表中的编号在65<=i<90范围内
        for i in range(6):
            # random的randrange方法可以定义随机数产生的范围
            r = random.randrange(0, 5)
            if i == r:
                num = random.randrange(0, 10)
                # 由于join方法只能对字符串起作用，因此需要将数字转化为字符串
                li.append(str(num))
            else:
                temp = random.randrange(65, 91)
                # 内建函数的chr方法可以将一个数字转化为ASCII对照表里的对应的字符，比如65代表A，
                n = chr(temp)
                li.append(n)
        result = "".join(li)
        print  result

        return renter.message()
    def POST(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        data = web.input()
        username = data.get('username')
        txt = data.get('txt')
        vcode = data.get('vcode')
        if vcode != result: return '验证码错误 '
        times=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print username,txt,times
        db.insert('drcom', username=username, txt=txt, time=times)
        raise web.seeother('/message')

# class Index(object):
#     def GET(self):
#         return renter.index()
#     def POST(self):
#         web.header("Content-Type","text/html; charset=utf-8")
#         data = web.input()
#         username = data.get('username')
#         password = data.get('password')
#         if not username or not password: return "账号密码不能为空"
#         password = hashlib.sha1(password).hexdigest()
#         da = db.query("select *  from user where username = '%s' and password = '%s'" %(username,password))
#         if not da : return '账号或密码错误，如没有账号请<a href="/reg">点击注册</a>'
#         raise web.seeother('/user')

# class Reg(object):
#     def GET(self):
#         return renter.reg()
#     def POST(self):
#         web.header("Content-Type","text/html; charset=utf-8")
#         data = web.input()
#         username = data.get('username')
#         password = data.get('password')
#         password2 = data.get('password2')
#         if not username or not password or not password2: return "账号密码不能为空"
#         password = hashlib.sha1(password).hexdigest()
#         print password
#         da = db.query("select * from user where username = '%s'"%username)
#         if da:return '账号已被注册，请重新输入'
#         db.insert('user',username=username,password=password,cs=3)
#         return '注册成功'


if __name__ == '__main__':
    app.run()