import random
import string
def generate_password(length):
    password = ''
    characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += ''.join(random.choice(characters))
    else:
        return password
password_length = int(input("Enter desired password length: "))
print("Generated Password:", generate_password(password_length))
