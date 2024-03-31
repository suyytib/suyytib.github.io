from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
db=SQLAlchemy()
migrate=Migrate()
mail = Mail()
# 这些代码属于数据库配置模块,但为了防止循环导入的问题发生,单独放一个文件里