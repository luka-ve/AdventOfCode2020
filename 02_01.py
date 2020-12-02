import re

with open('02_01_input.txt', 'r') as file:
    lines = file.readlines()

mins = []
maxs = []
letters = []
passwords = []

for line in lines:
    mins.append(int(re.search(r'\d+-', line).group()[:-1]))
    maxs.append(int(re.search(r'-\d+', line).group()[1:]))
    letters.append(re.search(r'[a-z]:', line).group()[:-1])
    passwords.append(re.search(r': \w+', line).group()[2:])

def check_password(password, letter, min, max):
    counts = 0

    for l in password:
        if l == letter:
            counts = counts + 1
    
    if counts >= min and counts <= max:
        return True
    else:
        return False

n_valid_passwords = 0

for i in range(0, len(passwords)):
    n_valid_passwords = n_valid_passwords + check_password(passwords[i], letters[i], mins[i], maxs[i])

print(n_valid_passwords)


