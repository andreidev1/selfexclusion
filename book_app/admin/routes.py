from flask import Blueprint, render_template, request
from models.models import Casino
from models.models import Admin

admin = Blueprint('admin', 
                __name__, 
                subdomain = 'admin',
                template_folder='templates', 
                static_folder='static',
                static_url_path='/admin/static'
                )


@admin.route('/', subdomain='admin')
def index():
    if request.method == 'POST':
        pass

    return render_template('admin/index.html')



