import numpy as np

with open('01_01_input.txt', 'r') as file:
    numbers = file.readlines()

numbers = np.array([int(number.strip()) for number in numbers])

print(len(numbers))

target = 2020

# Remove all numbers that are larger than the sum of two the smallest numbers
# Those will not be considered

sum_of_smallest_numbers = sum(np.sort(numbers)[0:2])

print(sum_of_smallest_numbers)

numbers_smaller = numbers[numbers <= (target - sum_of_smallest_numbers)]
numbers_smaller_sorted = np.sort(numbers_smaller)

print(numbers_smaller_sorted)

###################### Find the number

final_numbers = []

# Find two and three digit numbers
two_and_three_digit_numbers = []
more_digit_numbers = []

for i in numbers_smaller_sorted:
    if i < 1000 or i > 9:
        two_and_three_digit_numbers.append(i)
    elif i > 1000:
        more_digit_numbers.append(i)

print(two_and_three_digit_numbers)

# Sum all two and three digit numbers
sums = []

for index, i in enumerate(two_and_three_digit_numbers):
    for j in two_and_three_digit_numbers[(index + 1):]:
        sums.append(i + j)


# Find third number
found = False

third_number = 0
sum_of_first_two_numbers = 0

full_numbers = []

for number in sums:
    current_target = target - number

    for j in numbers_smaller_sorted:
        full_numbers.append(j + number)
        if j + number == target:
            found = True

    if found:
        sum_of_first_two_numbers = number
        third_number = current_target
        print(f'Your numbers are {current_target} and {number}. {current_target} + {number} = {current_target + number}.')
        break

final_numbers.append(third_number)

found = False

for number in two_and_three_digit_numbers:
    current_target = sum_of_first_two_numbers - number

    for j in two_and_three_digit_numbers:
        if current_target == j:
            found = True

    if found:
        final_numbers.append(current_target)
        final_numbers.append(number)
        print(f'Your numbers are {current_target} and {number}. {current_target} + {number} = {current_target + number}. Their product is {current_target * number}')
        break

# Print final three numbers!
print(f'Your final three number are: {final_numbers[0:4]}. Their sum is {np.sum(final_numbers)}. Their product is {np.prod(final_numbers)}')
print(f'Their sum is 2020? {np.sum(final_numbers) == 2020}')
