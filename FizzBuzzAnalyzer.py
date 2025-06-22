
print(f'Welcome to the FizzBuzz!\nProvide a few numbers and for each one you will get:')
print(f'Fizz if divisible by 3!\nBuzz if divisible by 5!')
print(f'FizzBuzz if divisible by 3 and 5! Have fun!')

def fizzbuzz(num):

    div_by_3 = num % 3 == 0
    div_by_5 = num % 5 == 0

    if div_by_3 and div_by_5:
        return(f'FizzBuzz!')

    elif div_by_3 and not div_by_5:
        return('Fizz!')

    elif not div_by_3 and div_by_5:
        return('Buzz!')

    else:
        return(num)

while True:
    numbers_list = input("Please, provide numbers you want to check(put spaces between them): ").split()
    for num in range(len(numbers_list)):
        numbers_list[num] = int(numbers_list[num])
        print(f"{(numbers_list[num])} → {fizzbuzz(numbers_list[num])}")
    user_cont = input('Do you want to continue and check a number (Type Y or N?) ').lower()
    if not user_cont == 'y':
        print('Goodbye')
        break
    else:
        continue


