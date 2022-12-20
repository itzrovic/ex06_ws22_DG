# Danir Garmayev
import random


def generate_lotto_numbers(count_of_num: int, max_num: int) -> list:
    rand_list = []
    for i in range(0, count_of_num):
        randnum = random.randint(1, max_num)
        rand_list.append(randnum)
    return rand_list

# output = generate_lotto_numbers(6, 45)
# print(output) 

print(generate_lotto_numbers(6, 45))
print(generate_lotto_numbers(6, 49))
print(generate_lotto_numbers(4, 50))
print(generate_lotto_numbers(6, 6))