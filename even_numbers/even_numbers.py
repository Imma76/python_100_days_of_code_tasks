total = 0
for number in range(1,101):
    if number % 2 == 0:
        print(number)
        total += number

print(f"total of all even numbers are {total}")