# core/views.py

from flask import render_template,request,Blueprint
from earthblog.models import BlogPost

core = Blueprint('core',__name__)

@core.route('/')
def index():
    page = request.args.get('page',1,type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=
    page,per_page=5)
    return render_template('home.html',blog_posts=blog_posts)

@core.route('/activism')
def info():
    return render_template('activism.html')
