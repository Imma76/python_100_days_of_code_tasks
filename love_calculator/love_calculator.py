first_name = input("what is your name ?")
second_name = input("what is your lovers name?")

new_name = first_name.lower() + second_name.lower()


t_count = new_name.count('t')
r_count = new_name.count('r')
u_count = new_name.count('u')
e_count = new_name.count('e')

l_count = new_name.count('l')
o_count = new_name.count('o')
v_count = new_name.count('v')
e_count = new_name.count('e')


total_true = t_count + r_count + u_count + e_count
total_love = l_count +  o_count  + v_count + e_count
total_score = int(str(total_love) + str(total_true))
if total_score < 10 or total_score > 90:
    print(f"your love score is {total_score} you go together like coke and mentos")
elif total_score >= 40 and total_love <= 50:
    print(f"your love score is {total_score} you are alright together")
else:
    print(f"your love score is {total_score}")