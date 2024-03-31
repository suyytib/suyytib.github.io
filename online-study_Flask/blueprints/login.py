import random
from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_mail import Message
from table_config import mail,db
from forms import Login_Form, Register_Form
from model import User
from sqlalchemy import or_
from model import Captcha
from flask import jsonify
from flask import session
# 实例化蓝图对象,该对象用于生成视图函数,这些函数都在蓝图的指定url为基础上绑定各自的url
bp=Blueprint("login",__name__,url_prefix='/login')

@bp.route('/',methods=["GET","POST"]) # 登录视图函数
def login():
    if request.method=="GET":
        return render_template('login/login.html',is_error=False)
    else:
        weqwe=request.form.get("quedin")
        form=Login_Form(request.form)
        if form.validate() and weqwe!='0':
            user=User.query.filter(or_(User.username==form.user_name.data,User.email==form.user_name.data)).all()
            if user and (user[0].password==form.user_passwd.data):
                session["user_id"]=user[0].id
                return render_template('/root.html')
            return redirect(url_for('root.root'))
        else:
            return render_template('login/login.html',is_error=True)
    
@bp.route('/register/', methods=['GET', 'POST'])
def register():   # 注册视图函数
    if request.method == "GET":
        return render_template('/login/register.html')
    else:
        # 将表单传入验证器类进行初始化
        form=Register_Form(request.form)
        # 从数据库中查找验证码
        true_captcha=Captcha.query.filter(or_(Captcha.email==form.email.data)).all()
        # 判断验证是否成功，以及查询对象是否存在
        if form.validate() and true_captcha:
            # 判断查找到的验证码是否匹配
            if request.form.get("captcha")==true_captcha[-1].captcha:
                # 创建用户并同步到数据库
                new_user=User(username=form.username.data , password=form.passwd.data , email=form.email.data)
                db.session.add(new_user)
                db.session.commit()
                # 重定向到登陆界面
                return redirect(url_for("login.login"))
        # 上述验证中出现错误则重定向到错误页面
        return render_template('login/register.html',is_error=True)
    
# 邮箱发送函数
@bp.route('/register/email_send/')
def email_send():
    # 获取get请求参数中的email
    email=request.args.get("email")
    # 生成验证码初始列表
    number_list=[str(i) for i in range(10)]
    captcha=''.join(random.choices(number_list,k=6))
    # 生成邮箱消息
    msg=Message(subject='懒人tool网站验证码发送',body=f'验证码:{captcha},谢谢您注册懒人tool在线学习平台,望您使用开心',
                recipients=[email])
    # 发送邮箱
    mail.send(msg)
    # 将生成的验证码和对应邮箱上传到数据库
    temp=Captcha(email=email,captcha=captcha)
    db.session.add(temp)
    db.session.commit()
    return jsonify({"code":200, "message": "success!", "data": None})