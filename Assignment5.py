# Program Name: Assignment5.py
# Course: IT3883/Section W02
# Student Name: Adam Hutcheson
# Assignment Number: Lab5
# Due Date: 11/16/2025
# Purpose: Create a SQLite database and save data from a text file to it, compute averages and print to console
import sqlite3

# Function to insert
def insert(cursor, day, temp):
    cursor.execute("INSERT INTO avg_temps (day_of_week, temperature_value) VALUES (?, ?)",
                   (day,temp))

# Function to calculate + return average
def average(cursor, day):
    cursor.execute("SELECT AVG(temperature_value) FROM avg_temps WHERE day_of_week = ?",
    (day,) )
    return cursor.fetchone()[0]

# Connect
conn = sqlite3.connect("Assignment5.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS avg_temps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day_of_week TEXT,
    temperature_value REAL
)
""")

# Reading text file and inserting to table using insert function
with open("Assignment5input.txt", "r") as file:
    for line in file:
        line = line.strip()

        split = line.split()
        day = split[0]
        temp = float(split[1])

        insert(cursor, day, temp)

# Saving
conn.commit()

# Printing averages for Sunday and Thursday to console
sunday_avg = average(cursor,'Sunday')
thursday_avg = average(cursor,'Thursday')
print(f"Average Sunday Temp: {sunday_avg:.1f}")
print(f"Average Thursday Temp: {thursday_avg:.1f}")

# Close :)
conn.close()