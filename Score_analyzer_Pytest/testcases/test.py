import os
import sys
import pytest

# Adjust the path to include the directory of the code file
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../code')))

from scoreAnalyzer import input_student_data, calculate_student_averages, find_highest_average, find_highest_subject_marks

def test_calculate_student_averages():
    students = [
        {"name": "Rohan", "marks": [80, 90]},
        {"name": "Sarthak", "marks": [75, 85, 95]},
    ]

    averages = calculate_student_averages(students)

    assert averages["Rohan"] == 85
    assert averages["Sarthak"] == 85

def test_find_highest_average():
    averages = {"Rohan": 88, "Sarthak": 92, "pondarr": 85}

    highest_student, highest_avg = find_highest_average(averages)

    assert highest_student == "Sarthak"
    assert highest_avg == 92

def test_find_highest_subject_marks():
    students = [
        {"name": "Rohan", "marks": [80, 90, 95]},
        {"name": "Sarthak", "marks": [75, 95, 85]},
        {"name": "pondarr", "marks": [90, 80, 88]},
    ]

    highest_scorers = find_highest_subject_marks(students)

    assert highest_scorers[0] == ["pondarr"]
    assert highest_scorers[1] == ["Sarthak"]
    assert highest_scorers[2] == ["Rohan"]
