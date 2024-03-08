def extract_high_average_grades(student_records):
    high_average_grades = {name: avg_grade for name, avg_grade in student_records.items() if avg_grade >= 15}
    return high_average_grades
