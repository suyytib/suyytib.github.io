from flask import redirect
from functools import wraps
from flask import g
from flask import url_for
# 这是登录验证装饰器函数,在想要加入登陆验证的是视图函数上方加入@captcha__is_login()即可绑定登陆验证功能
def captcha__is_login(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if g.user_id:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login.login'))
    return inner