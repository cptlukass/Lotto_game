from random import randint


def lotto():
    """Collect 6 numbers from the user, then pick 6 random numbers
    and inform the user how many numbers he guessed.

    :return: user numbers list, randomly picked numbers list, information about user hits.
    """
    str_index = 1
    num_list = []
    while len(num_list) < 6:
        try:
            user_num = input(f"Pick a number no. {str_index}: ")
            input_num = int(user_num)
            if input_num not in num_list and input_num in range(1, 50):
                num_list.append(input_num)
                str_index += 1
            else:
                print("Number repeated or it's out of range!")
        except ValueError:
            print("That's not a number!")
    num_list.sort()
    print(num_list)
    winning_list = []
    for i in range(6):
        bump = randint(1, 49)
        winning_list.append(bump)
    winning_list.sort()
    print(winning_list)
    strike = 0
    for i in range(6):
        if num_list[i] in winning_list:
            strike += 1
        else:
            continue
    return f"You hit {strike} numbers in this lottery!"


print(lotto())
