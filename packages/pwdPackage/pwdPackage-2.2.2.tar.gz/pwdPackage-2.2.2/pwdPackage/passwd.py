"""
Password Generator Module

This module contains functions to generate a random password that meets certain requirements.
The password will have a length between 6 and 12 characters, containing at least one lowercase letter,
one uppercase letter, and one digit. The generated password will not include any values present in
the provided CSV files ('names.csv' and 'places.csv').

Functions:
    exclude_csv(path): Reads data from a CSV file and returns a set of values from the first column.
    generate_pass(exclusions): Generates a password that meets certain requirements.
    gen_pass(): Generates a password that excludes names and places from the provided CSV files.
"""


import random
import string
import csv

def exclude_csv(path):
    """
    Reads data from a CSV file and returns a set of values from the first column.

    Parameters:
        path (str): The path to the CSV file.

    Returns:
        set: A set containing values from the first column of the CSV file.
    """
    with open(path, newline='',encoding='utf-8') as csvfile:
        reader=csv.reader(csvfile)
        return set(row[0] for row in reader)

def generate_pass(exclusions):
    """
    Generates a password that meets certain requirements.

    The password will have a length between 6 and 12 characters,
    containing at least one lowercase letter, one uppercase letter, and one digit.
    The generated password will not be in the exclusions set.

    Parameters:
        exclusions (set): A set of passwords to be excluded from the generated password.

    Returns:
        str: The generated password.
    """
    # using string to generate characters
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    num=string.digits

    while True:
        # using random for range
        len_password=random.randint(6, 12)
        # to select at least one lower, one upper, one number
        passwd=random.choice(lower)+random.choice(upper)+random.choice(num)
        # filling password with remaining length
        passwd+=''.join(random.choices(lower+upper+num,k=len_password-3))

        if len(passwd)>=6 and passwd not in exclusions:
            break

    # shuffling the password by creating a list
    password_list=list(passwd)
    random.shuffle(password_list)
    passwd=''.join(password_list)
    return passwd

# calling exclude_csv function to collect all names from names.csv
excluded_names=exclude_csv("names.csv")

# calling exclude_csv function to collect all names from places.csv
excluded_places=exclude_csv("places.csv")

# gathering all names and places which shouldn't be included in password
all_exclusions=excluded_names.union(excluded_places)

def gen_pass():
    """
    Generates a password that excludes the provided names and places.

    Returns:
        str: The generated password.
    """
    passwd=generate_pass(all_exclusions)
    return passwd

# generating password by calling function
password=gen_pass()
print(password)
