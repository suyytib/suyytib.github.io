from flask import Blueprint, request
from flask import render_template

bp=Blueprint("root",__name__,url_prefix="/")
@bp.route('/')
def root():
    return render_template('root.html')

@bp.route('/choujiang/',methods=["GET","POST"]) 
def choujiang():
    return render_template('/root/choujiang.html')