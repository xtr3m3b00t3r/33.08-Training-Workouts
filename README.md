# Workout Tracker

A web application for tracking workout routines and gym sessions.

## Overview

Workout Tracker is a Flask-based web application that allows users to:
- Access workout routines online
- Track gym sessions and exercises
- Monitor progress over time
- Record weights, sets, and notes for each exercise

The application is designed around the 3/7 Method training routine, which involves performing sets of 3, 4, 5, 6, and 7 reps for each exercise with minimal rest between sets.

## Features

- **Workout Viewing**: Access your workout routines in a clean, formatted view
- **Session Tracking**: Record which exercises you complete during each gym session
- **Progress Monitoring**: View your workout history and track consistency
- **Responsive Design**: Works on both desktop and mobile devices

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the application:
   ```
   python app.py
   ```
6. Access the application at http://127.0.0.1:5000

## Usage

1. **Home Page**: View available workouts and recent sessions
2. **Start Workout**: Select which workout you want to do (A or B)
3. **Track Exercises**: Record each exercise as you complete it
4. **View History**: Review your workout history and progress

## Technical Details

- **Backend**: Flask, SQLAlchemy, SQLite
- **Frontend**: Bootstrap, Chart.js
- **Data Format**: Markdown for workout routines

## Future Enhancements

- User authentication
- Custom workout creation
- Advanced progress analytics
- Export data functionality

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developer

Developed by Benjamin D.W Truman (2025)
