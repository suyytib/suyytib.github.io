from flask import Flask
from blueprints.login import bp as login_bp
from blueprints.root import bp as root_bp
from blueprints.box import bp as box_bp
from table_config import db,migrate,mail
import config
from flask import session
from flask import g
from model import User
# flask默认去templates文件夹下面找渲染的html文件

app = Flask(__name__)
app.register_blueprint(login_bp)
app.register_blueprint(root_bp)
app.register_blueprint(box_bp)
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app,db)
mail.init_app(app)
# 这是获取登录状态函数,用于保持用户登录状态，只要session还在，用户下次进入该网站可以免登录
@app.before_request
def captcha_login():
    temp=session.get("user_id")
    if temp:
        user=User.query.get(temp)
        setattr(g,"user_id",user.id)
    else:
        setattr(g,"user_id",None)
if __name__ == '__main__':
    app.run(debug=True)
