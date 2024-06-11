import sys
import pytest

# Adjust the sys.path to include the path to the code directory
sys.path.append('/home/rohan/Documents/Desktop/sem4/DASS/assignment2/q3/code')

from q3 import date_month

def test_valid_date():
    assert date_month(2024) == "invalid"

def test_leap_year():
    assert date_month(2020) == "02 02 2020"

def test_invalid_month():
    assert date_month(20247) == "invalid"

def test_invalid_day():
    assert date_month(2000) == "invalid"

def test_less_than_4_digits():
    assert date_month(99) == "invalid"
