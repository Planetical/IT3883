# Program Name: Assignment2.py
# Course: IT3883/Section W02
# Student Name: Adam Hutcheson
# Assignment Number: Lab2
# Due Date: 9/19/2025
# Purpose: Takes in the input from a text file for the grades of students, calculates average, output average

# Method to read text file
def readfile(name):
    with open(name, "r") as file:
        # Reading each lines
        for line in file:
            # split each line by space
            split = line.split()

            # take the name from list and save
            student_name = split[0]
            # map the rest of list to grades
            grades = list(map(float,split[1:]))

            # average grades
            average = sum(grades) / 6

            # print name and average
            print(f"{student_name} {average:.2f}")
        file.close()

readfile("Assignment2input.txt")
