import string
import random


def random_generate_key(letter_number: int = 32) -> str:
    random_string = ""
    for _ in range(letter_number):
        random_string += str(random.choice(string.ascii_letters + string.digits))
    return random_string
