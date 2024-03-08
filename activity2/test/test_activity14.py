from activity2.activity14 import extract_high_average_grades

def test_filter_high_grades_empty_dict():
    result = extract_high_average_grades({})
    assert result == {}

def test_filter_high_grades_no_high_grades():
    students_dict = {"Arjun": 12, "Priya": 14, "Rohan": 13}
    result = extract_high_average_grades(students_dict)
    assert result == {}

def test_filter_high_grades_some_high_grades():
    students_dict = {"Arjun": 17, "Priya": 14, "Rohan": 19}
    result = extract_high_average_grades(students_dict)
    assert result == {"Arjun": 17, "Rohan": 19}

def test_filter_high_grades_all_high_grades():
    students_dict = {"Arjun": 18, "Priya": 20, "Rohan": 15}
    result = extract_high_average_grades(students_dict)
    assert result == {"Arjun": 18, "Priya": 20, "Rohan": 15}
