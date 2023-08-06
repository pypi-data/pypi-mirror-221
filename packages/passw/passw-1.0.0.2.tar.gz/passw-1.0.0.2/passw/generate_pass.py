# random_password_generator.py
import random
import string

def generate_random_password(length):
    while True:
        password = random.choices(string.ascii_lowercase, k=1) + \
                   random.choices(string.ascii_uppercase, k=1) + \
                   random.choices(string.digits, k=1) + \
                   random.choices(string.ascii_letters + string.digits, k=length-3)
        random.shuffle(password)
        password = ''.join(password)

        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password)):
            break

    return password


def gen_pass():
    paas_len = random.randint(6,12)
    passw = generate_random_password(pass_len)
    return passw
   
