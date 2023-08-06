import string
import random


def integer(start, end):
    return random.randint(start, end)


def float(start, end):
    return random.uniform(start, end)


def choice(seq):
    return random.choice(seq)


def code(length, uppercase=True, lowercase=True, rep=True):
    letters = ""
    codec = []
    if uppercase:
        letters += string.ascii_uppercase
    if lowercase:
        letters += string.ascii_lowercase
    for i in range(length):
        letters = list(letters)
        codec.append(random.choice(letters))
        if not rep:
            letters.remove(codec[-1])
    codec = ''.join(codec)
    return codec


def letter():
    return random.choice(string.ascii_letters)


def password(length, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def boolean():
    return random.choice([True, False])


def element(text):
    return random.choice(text)


def sample(lst, k):
    return random.sample(lst, k)


def shuffle(lst):
    random.shuffle(lst)
    return lst


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

