import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import markdown

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-for-testing')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workouts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Context processor to provide current date to all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# Models
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    sessions = db.relationship('Session', backref='workout', lazy=True)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    notes = db.Column(db.Text)
    completed_exercises = db.relationship('CompletedExercise', backref='session', lazy=True, cascade="all, delete-orphan")

class CompletedExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'), nullable=False)
    exercise_name = db.Column(db.String(100), nullable=False)
    sets_completed = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float)
    notes = db.Column(db.Text)

# Routes
@app.route('/')
def index():
    workouts = Workout.query.all()
    recent_sessions = Session.query.order_by(Session.date.desc()).limit(5).all()
    return render_template('index.html', workouts=workouts, recent_sessions=recent_sessions)

@app.route('/workout/<int:workout_id>')
def view_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    html_content = markdown.markdown(workout.content)
    return render_template('workout.html', workout=workout, html_content=html_content)

@app.route('/start_session', methods=['GET', 'POST'])
def start_session():
    if request.method == 'POST':
        workout_id = request.form.get('workout_id')
        
        if not workout_id:
            flash('Please select a workout', 'danger')
            return redirect(url_for('start_session'))
        
        new_session = Session(
            workout_id=workout_id,
            notes=request.form.get('notes', '')
        )
        
        db.session.add(new_session)
        db.session.commit()
        
        return redirect(url_for('track_session', session_id=new_session.id))
    
    workouts = Workout.query.all()
    return render_template('start_session.html', workouts=workouts)

@app.route('/track_session/<int:session_id>', methods=['GET', 'POST'])
def track_session(session_id):
    session = Session.query.get_or_404(session_id)
    
    if request.method == 'POST':
        exercise_name = request.form.get('exercise_name')
        sets_completed = request.form.get('sets_completed')
        weight = request.form.get('weight')
        notes = request.form.get('notes', '')
        
        if not exercise_name or not sets_completed:
            flash('Please fill in the required fields', 'danger')
            return redirect(url_for('track_session', session_id=session_id))
        
        completed_exercise = CompletedExercise(
            session_id=session_id,
            exercise_name=exercise_name,
            sets_completed=int(sets_completed),
            weight=float(weight) if weight else None,
            notes=notes
        )
        
        db.session.add(completed_exercise)
        db.session.commit()
        
        flash('Exercise recorded successfully!', 'success')
        return redirect(url_for('track_session', session_id=session_id))
    
    return render_template('track_session.html', session=session)

@app.route('/session/<int:session_id>')
def view_session(session_id):
    session = Session.query.get_or_404(session_id)
    return render_template('session.html', session=session)

@app.route('/history')
def history():
    sessions = Session.query.order_by(Session.date.desc()).all()
    return render_template('history.html', sessions=sessions)

@app.route('/complete_session/<int:session_id>')
def complete_session(session_id):
    session = Session.query.get_or_404(session_id)
    return redirect(url_for('history'))

@app.route('/api/exercises/<int:workout_id>')
def get_exercises(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    # Parse markdown to extract exercise names
    import re
    exercises = re.findall(r'### \d+\.\s+(.*?)$', workout.content, re.MULTILINE)
    return jsonify(exercises)

# Initialize the database and load workout data
def init_db():
    with app.app_context():
        db.create_all()
        
        # Check if workouts already exist
        if Workout.query.count() == 0:
            # Load workout A
            with open('workout-a-revised.md', 'r') as f:
                workout_a_content = f.read()
            
            workout_a = Workout(
                name='Workout A: 3/7 Method',
                content=workout_a_content
            )
            
            # Load workout B
            with open('workout-b.md', 'r') as f:
                workout_b_content = f.read()
            
            workout_b = Workout(
                name='Workout B: 3/7 Method',
                content=workout_b_content
            )
            
            db.session.add(workout_a)
            db.session.add(workout_b)
            db.session.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
