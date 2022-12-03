from flask import Blueprint, render_template
from models.models import Casino

admin = Blueprint('admin', 
                __name__, 
                subdomain = 'admin',
                template_folder='templates', 
                static_folder='static',
                static_url_path='/admin/static'
                )


@admin.route('/', subdomain='admin')
def index():
    return render_template('admin/index.html')



