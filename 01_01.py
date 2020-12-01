with open('01_01_input.txt', 'r') as file:
    numbers = file.readlines()

numbers = [int(number.strip()) for number in numbers]

print(len(numbers))

target = 2020

found = False

for number in numbers:
    current_target = target - number

    for j in numbers:
        if current_target == j:
            found = True

    if found:
        print(f'Your numbers are {current_target} and {number}. {current_target} + {number} = {current_target + number}. Their product is {current_target * number}')
        break
