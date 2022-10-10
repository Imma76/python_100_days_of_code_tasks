students_score = input("enter a list of students score seperated by a comma").split(",")
high_score = 0
for score in students_score:
    if int(score) > high_score:
        high_score = int(score)

print(f"the highest score in the class is: {high_score}")