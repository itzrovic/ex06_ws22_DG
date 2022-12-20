# Danir Garmayev
# click link to see on GitHub https://github.com/itzrovic/ex06_ws22_DG
import random


def generate_lotto_numbers(count_of_num: int, max_num: int) -> list:
    rand_list = []
    for i in range(0, count_of_num):
        randnum = random.randint(1, max_num)
        if randnum not in rand_list:
            rand_list.append(randnum)
        else:
            while (randnum in rand_list):
                randnum = random.randint(1, max_num)
            rand_list.append(randnum)
    return rand_list

def lotto_probability(numbers: list[int], max_num: int) -> int: # ich habe es nicht hingekriegt zu zählen, wieviele Versuche man insgesamt braucht. Es zählt nur wie viele Versuche man braucht wenn man zufällig zieht bis das gleiche rauskommt
    count_tries = 0
    lottery_ticket = numbers
    count_ticket = []
    rand_ticket = generate_lotto_numbers(6, max_num)
    while (rand_ticket != lottery_ticket):
        rand_ticket = generate_lotto_numbers(6, max_num)
        count_tries += 1
    # for i in range(max_num):
    #     count_ticket.append

    return count_tries

AT = 45
DE = 49
AT_lotto_numbers_list = generate_lotto_numbers(6, 45)
DE_lotto_numbers_list = generate_lotto_numbers(6, 49)

tries = lotto_probability(AT_lotto_numbers_list, AT)
print(tries)

# print(generate_lotto_numbers(6, 45))
# print(generate_lotto_numbers(6, 49))
# print(generate_lotto_numbers(4, 50))
# print(generate_lotto_numbers(6, 6))