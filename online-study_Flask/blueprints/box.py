from flask import Blueprint
bp=Blueprint("box",__name__,url_prefix="/box")
@bp.route('/')
def box_root():
    return "这是工具网页"