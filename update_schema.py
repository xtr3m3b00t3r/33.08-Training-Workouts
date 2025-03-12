import sqlite3

# Connect to the database
conn = sqlite3.connect('instance/workouts.db')
cursor = conn.cursor()

# Check if description column exists
cursor.execute("PRAGMA table_info(workout)")
columns = cursor.fetchall()
column_names = [column[1] for column in columns]

# Add description column if it doesn't exist
if 'description' not in column_names:
    cursor.execute("ALTER TABLE workout ADD COLUMN description TEXT")
    print("Added description column to workout table")

# Add exercises column if it doesn't exist
if 'exercises' not in column_names:
    cursor.execute("ALTER TABLE workout ADD COLUMN exercises TEXT")
    print("Added exercises column to workout table")

# Update existing workouts to populate exercises field
if 'exercises' in column_names:
    # Get all workouts
    cursor.execute("SELECT id, content FROM workout")
    workouts = cursor.fetchall()
    
    # Parse exercises from content and update the exercises field
    import re
    for workout_id, content in workouts:
        exercises = re.findall(r'### \d+\.\s+(.*?)$', content, re.MULTILINE)
        exercises_str = ', '.join(exercises)
        cursor.execute("UPDATE workout SET exercises = ? WHERE id = ?", (exercises_str, workout_id))
    
    print(f"Updated exercises field for {len(workouts)} workouts")

# Commit changes and close connection
conn.commit()
conn.close()

print("Database schema update complete")
