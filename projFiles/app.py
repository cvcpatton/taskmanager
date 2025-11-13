# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskmanager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'  # Replace with a real secret key

db.init_app(app)

# Create database if it doesn't exist
with app.app_context():
    db.create_all()


# 🏠 Home - View all tasks
@app.route('/')
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)


# ➕ Add a new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description')
        if not title.strip():
            flash('Title cannot be empty!')
            return redirect(url_for('add_task'))
        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!')
        return redirect(url_for('index'))
    return render_template('add_task.html')


# ✏️ Edit a task
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.status = request.form['status']
        db.session.commit()
        flash('Task updated successfully!')
        return redirect(url_for('index'))
    return render_template('edit_task.html', task=task)


# ❌ Delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

