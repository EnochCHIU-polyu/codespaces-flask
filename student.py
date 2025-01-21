import json

# 步驟 2：讀取 JSON 檔案
with open('student.json', 'r') as file:
    data = json.load(file)

# 步驟 3：處理 JSON 資料
students = data['students']

for student in students:
    grades = student['grades']
    average_grade = sum(grades.values()) / len(grades)
    print(f"Name: {student['name']}, Average Grade: {average_grade}")
