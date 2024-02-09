import random

characters = 'abcdefghijklmnopqrstuvwxyz_.'
email_length = random.randint(5, 12)
username_length = random.randint(4, 7)
domain_length = random.randint(2, 3)

def generate_string(length):
    return ''.join(random.choice(characters) for _ in range(length))

def is_valid_username(username):
    return username.count('.') <= 1

def generate_email():
    while True:
        username = generate_string(email_length)
        if is_valid_username(username):
            break

    domain = generate_string(domain_length)

    print(f'Your email has been created\nYour email is: {username}@{domain}.{domain}')

if __name__ == "__main__":
    generate_email()
