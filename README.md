# Python/Flask Task Manager ✅  
A Python Flask app to add, edit, and organize daily tasks in a clean, responsive interface. This project demonstrates backend data management, dynamic HTML rendering, and front-end interaction for task organization and productivity tracking.

## Features
- Add, view, edit, and delete tasks  
- Mark tasks as complete or in progress  
- Store task data in a persistent SQLite database  
- Clean, responsive UI built with HTML, CSS, and Bootstrap  
- Server-side validation and flash messages for user feedback  

## Technologies Used
- Backend: Python 3, Flask, SQLAlchemy  
- Frontend: HTML5, CSS3, Bootstrap 5 (Jinja templates), Render
- Database: SQLite  
- Tools: Git/GitHub, PyCharm  

## Learning Objectives
- Implement full-stack CRUD functionality using Flask routes and SQLAlchemy models  
- Use Flask’s Jinja templating engine for dynamic HTML rendering  
- Manage persistent data storage with SQLite  
- Apply RESTful design principles and modular programming practices  

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/flask-task-manager.git
   cd flask-task-manager
 
2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # for macOS/Linux
venv\Scripts\activate      # for Windows


3. Install dependencies
pip install -r requirements.txt


4. Initialize the database:
flask db init
flask db migrate
flask db upgrade


5. Run the app
flask run


6. Open your browser and navigate to:
http://127.0.0.1:5000/


## Project structure, taskmanager/  
│  
├── app.py  
├── models.py  
… taskmanager.db - SQLite database file (auto-created)  
├── static/  
│   └── styles.css  
├── templates/  
│   ├── base.html  
│   ├── index.html  
│   ├── add_task.html  
│   └── edit_task.html  
├── requirements.txt  
 
## Potential Upgrades
- Add user authentication and login sessions
- Integrate due-date notifications or calendar sync
- Front-end rebuild in React, communicating with Flask through RESTful JSON endpoints (expand to RESTful API endpoints)
- Dockerize the application for deployment 

## License
MIT License, Cathy Patton 2025
