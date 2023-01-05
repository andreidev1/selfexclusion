from flask import Blueprint, render_template, request, session, redirect, g, url_for, flash

from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app as app
from db import db
from stopgambling.models.models import Admin
from .forms import AdminLoginForm



admin = Blueprint('admin', 
                __name__, 
                subdomain = 'admin',
                template_folder='templates', 
                static_folder='static',
                static_url_path='/admin/static'
                )




login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin.login'


@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))



@admin.route('/', methods=['GET','POST'], subdomain='admin')
def login():
    # If the User is already logged in, don't allow them to try to log in again
    if current_user.is_authenticated:
        flash('Already logged in!  Redirecting to Admin page...')
        return redirect(url_for('admin.dashboard'))
    
    form = AdminLoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            admin = Admin.query.filter_by(username=form.username.data).first()
            if admin:
                if check_password_hash(admin.password, form.password.data):
                    login_user(admin)
                    flash('Thanks for logging in')
                return redirect(url_for('admin.dashboard'))

        flash('ERROR! Incorrect login credentials.')
    return render_template('admin/index.html', form=form)

        
'''
@admin.route('/register', methods=['GET','POST'], subdomain='admin')
def register():

    # If the User is already logged in, don't allow them to try to register
    if current_user.is_authenticated:
        flash('Already registered!  Redirecting to admin dashboard...')
        return redirect(url_for('admin.dashboard'))

    form = AdminLoginForm()
    hashed_password = generate_password_hash(form.password.data, method='sha256')

    
    if request.method == 'POST' and form.validate_on_submit():
        new_admin = Admin(username=form.username.data, password=hashed_password)

        db.session.add(new_admin)
        db.session.commit()
        login_user(new_admin)
        flash('Thanks for registering')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/register.html', form=form)
'''


@admin.route('/dashboard', subdomain='admin')
@login_required
def dashboard():
    return render_template('admin/dashboard.html', current_user=current_user)


@admin.route('/logout', subdomain='admin')
@login_required
def logout():
    logout_user()
    flash('Goodbye')
    return redirect(url_for('admin.login'))