import random
import string


def get_random_password() -> str:
    password = ""
    key = ""
    for i in range(10):
        key += str(i)
    for i in string.ascii_lowercase:
        key += i
    for i in string.ascii_uppercase:
        key += i
    for char in random.sample(key, 8):
        password += char
    return password


print(get_random_password())
#end
