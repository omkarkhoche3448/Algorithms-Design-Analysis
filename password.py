import random

# Function to insert a character at a specified position in a string
def insert(s, pos, ch):
    return s[:pos] + ch + s[pos:]

# Function to add more characters to the string to meet the required conditions
def add_more_char(s, need):
    pos = 0
    low_case = "abcdefghijklmnopqrstuvwxyz"
    for i in range(need):
        pos = random.randint(0, len(s) - 1)
        s = insert(s, pos, low_case[random.randint(0, 25)])
    return s

# Function to suggest a new password by adding missing character types
# This function checks for the missing character types (lowercase, uppercase, digit, special character) in the password and inserts them randomly.  
def suggester(l, u, d, s, st):
    num = '0123456789'
    low_case = "abcdefghijklmnopqrstuvwxyz"
    up_case = low_case.upper()
    spl_char = '@#$_()!'
    pos = 0

    # Add a lowercase letter if missing
    if l == 0:
        pos = random.randint(0, len(st) - 1)
        st = insert(st, pos, low_case[random.randint(0, 25)])

    # Add an uppercase letter if missing
    if u == 0:
        pos = random.randint(0, len(st) - 1)
        st = insert(st, pos, up_case[random.randint(0, 25)])

    # Add a digit if missing
    if d == 0:
        pos = random.randint(0, len(st) - 1)
        st = insert(st, pos, num[random.randint(0, 9)])

    # Add a special character if missing
    if s == 0:
        pos = random.randint(0, len(st) - 1)
        st = insert(st, pos, spl_char[random.randint(0, len(spl_char) - 1)])

    return st

# Function to generate a password that satisfies the strength criteria
def generate_password(n, p):
    l = u = d = s = 0
    need = 0

    # Check if the password contains at least one lowercase, uppercase, digit, and special character
    for i in range(n):
        if p[i].islower():
            l = 1
        elif p[i].isupper():
            u = 1
        elif p[i].isdigit():
            d = 1
        else:
            s = 1

    # If the password contains all required character types, it's strong
    if (l + u + d + s) == 4:
        print("Your Password is Strong")
        return
    else:
        print("Suggested Passwords:")
        for i in range(10):
            suggest = suggester(l, u, d, s, p)
            need = 8 - len(suggest)  # Ensure the password length is at least 8 characters
            if need > 0:
                suggest = add_more_char(suggest, need)
            print(suggest)

if __name__ == '__main__':
    input_string = input("Enter your password: ")
    generate_password(len(input_string), input_string)











# 1: How does slicing work in Python?

# Slicing is used to extract a part of a string. The syntax is string[start:end], where:
# start is the index of the first character to include.
# end is the index of the character to exclude.
# If start or end is omitted, it defaults to the start or end of the string, respectively.
# Q2: What will happen if pos is greater than the length of the string?

# If pos is greater than the length of the string, the slicing operation (s[:pos] and s[pos:]) will not throw an error. Python treats the index as if it is at the end of the string, so the new character will be appended.
# Questions from add_more_char Function
# Q3: Why do we use random.randint(0, len(s) - 1) instead of a fixed position?

# Using a random position ensures that the new characters are distributed unpredictably across the string. A fixed position would lead to predictable additions, reducing the randomness and security of the password.
# Q4: Can this function add characters other than lowercase letters?

# Currently, the function only adds lowercase letters (low_case). To add other types of characters (e.g., digits or special characters), you could modify the function to include them in the pool of possible characters.
# Questions from suggester Function
# Q5: What is the purpose of low_case.upper()?

# The low_case.upper() converts the string of lowercase letters (abcdefghijklmnopqrstuvwxyz) into their uppercase equivalents (ABCDEFGHIJKLMNOPQRSTUVWXYZ). This ensures a pool of uppercase letters is available for insertion.
# Q6: Why do we check if l == 0, if u == 0, etc.?

# These checks ensure that the password is evaluated for missing character types:
# If l == 0, there are no lowercase letters.
# If u == 0, there are no uppercase letters.
# If d == 0, there are no digits.
# If s == 0, there are no special characters.
# Based on these checks, the program decides which characters need to be added to make the password strong.
# Q7: Can this function be extended to add more character types, like emojis?

# Yes, you can extend the function by adding a new pool of emojis (e.g., emoji = "😊😂👍💻🎉"). Then, include a condition to check for their absence and insert them as needed.
# Questions from generate_password Function
# Q8: Why is the minimum length set to 8?

# A minimum length of 8 characters is a widely accepted standard for strong passwords, as recommended by organizations like NIST. Longer passwords are harder to crack through brute force.
# Q9: Can this code handle an empty password? What happens if the user inputs ""?

# If the user inputs an empty string, the program will try to access p[i] in the for loop, which will cause an IndexError because there are no characters in the string. To handle this, you could add a check at the beginning of generate_password to ensure the password is not empty:
# python
# Copy code
# if not p:
#     print("Password cannot be empty")
#     return
# Q10: How would you modify the program to enforce a minimum of two special characters?

# Update the suggester function to check for the count of special characters in the password. If the count is less than 2, add additional special characters:
# python
# Copy code
# if st.count('@#$_()!') < 2:
#     for _ in range(2 - st.count('@#$_()!')):
#         pos = random.randint(0, len(st) - 1)
#         st = insert(st, pos, spl_char[random.randint(0, len(spl_char) - 1)])