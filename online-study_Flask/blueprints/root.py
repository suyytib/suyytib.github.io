from flask import Blueprint
from model import User
from table_config import db
from flask import render_template

bp=Blueprint("root",__name__,url_prefix="/")

@bp.route('/')
def root():
    return render_template('root.html')