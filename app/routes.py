from flask import render_template, redirect, url_for, request, flash
from app.database import db, Usuario, User
from werkzeug.security import generate_password_hash, check_password_hash

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            role = request.form['role']
            # Cria o usuário
            hashed_password = generate_password_hash(password)
            User.create(username=username, password=hashed_password, role=role)
            flash('Usuário registrado com sucesso!')
            return redirect(url_for('index'))
        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.get_or_none(User.username == username)
            if user and check_password_hash(user.password, password):
                flash(f'Bem-vindo, {user.username}!')
                return redirect(url_for('dashboard'))
            else:
                flash('Nome de usuário ou senha incorretos.')
        return render_template('login.html')

    @app.route('/dashboard')
    def dashboard():
        usuarios = Usuario.select()
        return render_template('dashboard.html', usuarios=usuarios)
