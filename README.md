# Workout Tracker

A web application for tracking workout routines and gym sessions with comprehensive exercise details.

## Overview

Workout Tracker is a Flask-based web application that allows users to:
- Create and access workout routines online
- Track gym sessions and exercises with detailed information
- Monitor progress over time
- Record weights, sets, reps, form cues, and detailed notes for each exercise
- Edit workouts with a live markdown preview

The application supports various training methodologies, including the 3/7 Method training routine, which involves performing sets of 3, 4, 5, 6, and 7 reps for each exercise with minimal rest between sets.

## Features

- **Workout Creation**: Create custom workout routines with a user-friendly interface
- **Detailed Exercise Tracking**: Record comprehensive exercise details including:
  - Machine weights
  - Free weights
  - Sets and reps
  - Custom rep schemes
  - Rest times
  - Form cues
  - Exercise notes
- **Live Markdown Editor**: Edit workout content with real-time preview
- **Real-time Updates**: See your workout content update as you add or modify exercises
- **Workout Viewing**: Access your workout routines in a clean, formatted view
- **Session Tracking**: Record which exercises you complete during each gym session
- **Progress Monitoring**: View your workout history and track consistency
- **Responsive Design**: Works on both desktop and mobile devices
- **Authentication**: Basic authentication to protect your workout data

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
5. Create a `.env` file in the root directory with the following content:
   ```
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///workouts.db
   BASIC_AUTH_USERNAME=your_username
   BASIC_AUTH_PASSWORD=your_secure_password
   ```
6. Run the application:
   ```
   python app.py
   ```
7. Access the application at http://127.0.0.1:5000

## Authentication

This application uses Flask-BasicAuth to protect all routes with password authentication:

1. **Setting Credentials**: 
   - Create a `.env` file as described in the installation section
   - Set your desired username and password using the `BASIC_AUTH_USERNAME` and `BASIC_AUTH_PASSWORD` variables
   - **Important**: Never commit your `.env` file to version control

2. **Accessing the Application**:
   - When you visit the application, you'll be prompted for the username and password
   - Enter the credentials you set in the `.env` file

3. **Changing Credentials**:
   - To change your username or password, update the values in the `.env` file
   - Restart the application for changes to take effect

## Usage

1. **Home Page**: View available workouts and recent sessions
2. **Add Workout**: Create a new workout with detailed exercise information
   - Add exercise name, sets, reps, weights, rest times, and form cues
   - See a live preview of your workout as you build it
   - Edit the markdown directly for advanced customization
3. **Modify Workout**: Update existing workouts with the same detailed interface
4. **Track Exercises**: Record each exercise as you complete it
5. **View History**: Review your workout history and progress

## Exercise Details

The application now supports tracking these details for each exercise:

- **Exercise Name**: The name of the exercise
- **Machine Weight**: Weight used on machine-based exercises
- **Free Weight**: Weight used for free weight exercises
- **Sets**: Number of sets to perform
- **Reps/Rep Scheme**: Either a fixed number of reps or a custom rep scheme (e.g., "3,4,5,6,7")
- **Rest Time**: Rest period between sets
- **Form Cues**: Important form reminders for proper technique
- **Notes**: Additional notes or instructions for the exercise

## Technical Details

- **Backend**: Flask, SQLAlchemy, SQLite
- **Frontend**: Bootstrap, Marked.js for markdown rendering
- **Data Format**: Markdown for workout routines with structured data entry
- **UI Features**: Live preview, dynamic content generation

## Future Enhancements

- User authentication
- Custom workout creation
- Advanced progress analytics
- Export data functionality
- Mobile app integration

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developer

Developed by Benjamin D.W Truman (2025)
