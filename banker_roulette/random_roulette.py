import random
names = input('Write down everyones name seperated by a comma')
name_list = names.split(',')
person_to_pay_index = random.randint(0, len(name_list))
print(person_to_pay_index)
print(name_list[person_to_pay_index])