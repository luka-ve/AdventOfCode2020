import re


def main():
    with open('02_01_input.txt', 'r') as file:
        lines = file.readlines()
        passwords = []

        for line in lines:
            constraint_positions = [int(pos)
                                    for pos in re.findall(r'\d+', line)]
            constraint_letter = re.search(r'[a-z]:', line).group()[:-1]
            password = re.search(r': \w+', line).group()[2:]

            passwords.append(Password(
                password, constraint_letter=constraint_letter, constraint_positions=constraint_positions))

    valid_passwords = [pw.validate() for pw in passwords]

    print(valid_passwords.count(True))


class Password:
    def __init__(self, password, constraint_letter=None, constraint_positions=[]):
        self.password = password
        self.constraint_letter = constraint_letter
        self.constraint_positions = constraint_positions

    def validate(self):
        count = 0

        for pos in self.constraint_positions:
            count = count + (self.password[pos - 1] == self.constraint_letter)

        return count == 1


if __name__ == '__main__':
    main()
