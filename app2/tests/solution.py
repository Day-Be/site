import random


chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def create_password():
    password = ''
    for n in range(10):
        password += random.choice(chars)
    return password


if __name__ == '__main__':
    print(create_password())
