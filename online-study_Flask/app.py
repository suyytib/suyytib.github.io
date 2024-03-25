from flask import Flask
from blueprints.login import bp as login_bp
from blueprints.root import bp as root_bp
from table_config import db,migrate,mail
import config
# flask默认去templates文件夹下面找渲染的html文件

app = Flask(__name__)
app.register_blueprint(login_bp)
app.register_blueprint(root_bp)
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app,db)
mail.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
