students_height = [120, 140, 160, 180, 200]
total_height = 0
for height in students_height:
    total_height = total_height + height

average = total_height / len(students_height)

print(f"the average height of students is {average}")