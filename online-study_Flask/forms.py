from wtforms import Form, StringField,PasswordField
from wtforms.validators import Length,Email,EqualTo,InputRequired
# 参与注册验证的表单类
class Register_Form(Form):
    username = StringField(validators=[InputRequired(u"用户名不能为空"),Length(min=4,max=20)])
    passwd =PasswordField(validators=[InputRequired(u"密码不能为空"),Length(min=6,max=20)])
    email=StringField(validators=[InputRequired(u"邮件不能为空"),Email()])
    re_password = PasswordField(validators=[InputRequired(u"密码不能为空"),EqualTo("passwd",u"两次密码不一致")])

# 参与登录验证的表单类
class Login_Form(Form):
    user_name = StringField(validators=[InputRequired(u"用户名不能为空"),Length(min=4,max=20)])
    user_passwd =PasswordField(validators=[InputRequired(u"密码不能为空"),Length(min=6,max=20)])