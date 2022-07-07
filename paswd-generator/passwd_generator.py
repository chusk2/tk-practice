#Password Generator Project
"""Generator of random passwords.
Generated passwords are stored in a plain text file.
Don't use it for real purposes."""
import random

# ASCII codes:
# a to z: 97 to 122
# Define letters, numbers and symbols
letters = [chr(i) for i in range(97,123)]
capital_letters = [i.upper() for i in letters]
numbers = [str(i) for i in range(10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_passwd():
    "returns a password"
    # populate password with a random number of elements
    # for each group
    nr_letters = random.randint(5, 7)
    nr_cap_letters = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    # add letters to password list
    password_list.extend(
    [random.choice(letters) for i in range(nr_letters)]
    )
    # add capital letters to password list
    password_list.extend(
    [random.choice(capital_letters) for i in range(nr_cap_letters)]
    )
    # add symbols to password list
    password_list.extend(
    [random.choice(symbols) for i in range(nr_symbols)]
    )
    # add numbers to password list
    password_list.extend(
    [random.choice(numbers) for i in range(nr_numbers)]
    )

    print(password_list)
    random.shuffle(password_list)

    password = ''.join(password_list)

    return password
