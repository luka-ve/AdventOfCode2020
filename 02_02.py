import re

with open('02_01_input.txt', 'r') as file:
    lines = file.readlines()

pos_1s = []
pos_2s = []
letters = []
passwords = []

for line in lines:
    pos_1s.append(int(re.search(r'\d+-', line).group()[:-1]))
    pos_2s.append(int(re.search(r'-\d+', line).group()[1:]))
    letters.append(re.search(r'[a-z]:', line).group()[:-1])
    passwords.append(re.search(r': \w+', line).group()[2:])

def check_password(password, letter, pos_1, pos_2):
    return (password[pos_1 - 1] == letter) != (password[pos_2 - 1] == letter)

n_valid_passwords = 0

for i in range(0, len(passwords)):
    n_valid_passwords = n_valid_passwords + check_password(passwords[i], letters[i], pos_1s[i], pos_2s[i])

print(n_valid_passwords)
