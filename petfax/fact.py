from flask import Blueprint, render_template, request, redirect

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('facts/new.html')
    
    return'this is the facts index'