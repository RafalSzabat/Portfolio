
print(f'Welcome to odd/even number checker')

def check_number(num):
    is_even = num % 2 == 0
    div_by_3 = num % 3 == 0
    div_by_5 = num % 5 == 0

    if is_even and not div_by_3 and not div_by_5:
        return('Your number is even. It is not divisible by 3 or 5.')

    elif is_even and div_by_3 and not div_by_5:
        return('Your number is even. It is divisible by 3 but not 5.')

    elif is_even and not div_by_3 and div_by_5:
        return('Your number is even. It is divisible by 5 but not 3.')

    elif div_by_3 and not div_by_5:
        return('Your number is odd. It is divisible by 3 but not 5')

    elif not div_by_3 and div_by_5:
        return('Your number is odd. It is divisible by 5 but not 3')

    elif div_by_3 and div_by_5:
        return('Your number is odd. It is divisible by 3 and 5')

    else:
        return('Your number is odd, it is not divisible by 3 or 5')


while True:
    numbers_list = input(f'Please enter numbers you want to check (use spaces between each one): ').split()
    for num in range(len(numbers_list)):
        numbers_list[num] = int(numbers_list[num])
        print(check_number(numbers_list[num]))

    user_cont = input(f'Do you want to continue and check a number (Type Y or N?) ').lower()
    if not user_cont == 'y':
        print(f'Goodbye')
        break
    else:
        continue


