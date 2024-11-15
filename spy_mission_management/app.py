# app.py
from flask import Flask, render_template, redirect, url_for, request, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base, User, Mission, Equipment
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

engine = create_engine('sqlite:///spy_mission.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
db_session = scoped_session(DBSession)

Base.metadata.create_all(engine)

def init_db():
    if not db_session.query(User).first():
        users = [
            User(username='M', password_hash=generate_password_hash('password'), role='M'),
            User(username='Q', password_hash=generate_password_hash('password'), role='Q'),
            User(username='007', password_hash=generate_password_hash('password'), role='Agent'),
            User(username='008', password_hash=generate_password_hash('password'), role='Agent'),
            User(username='analyst1', password_hash=generate_password_hash('password'), role='Analyst')
        ]
        db_session.add_all(users)
        db_session.commit()

        agent_007 = db_session.query(User).filter_by(username='007').first()
        agent_008 = db_session.query(User).filter_by(username='008').first()

        missions = [
            Mission(title='Secret Mission in Monte Carlo', description='Gather intelligence from the casino', assigned_to=agent_007.id),
            Mission(title='Operation in Tokyo', description='Infiltrate the secret organization', assigned_to=agent_008.id)
        ]
        db_session.add_all(missions)

        equipments = [
            Equipment(name='Laser Watch', description='A watch with laser-cutting capabilities', assigned_to=None),
            Equipment(name='Aston Martin Car', description='A car equipped with special gadgets', assigned_to=None)
        ]
        db_session.add_all(equipments)
        db_session.commit()

@app.route('/')
def home():
    return render_template('home.html')

#
@app.route('/login', methods=['GET', 'POST'])
def login():
    #
    pass

@app.route('/register', methods=['GET', 'POST'])
def register():
    #
    pass

#
@app.route('/logout')
def logout():
    #
    pass
#
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    else:
        return redirect(url_for('login'))

#
def require_roles(*roles):
    #
    pass


@app.route('/missions')
def missions_view():
#
    pass

@app.route('/equipments')
def equipments_view():
    #
    pass

#
@app.route('/add_mission', methods=['GET', 'POST'])
def add_mission():
    #
    pass

@app.route('/assign_equipment', methods=['GET', 'POST'])
def assign_equipment():
    #
    pass

# مدیریت Session پایگاه داده
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True)
