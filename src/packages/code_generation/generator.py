from random import randint, randrange

def Generator() -> str:
    code = ''
    for x in range(2):
        code += str(randint(0,9))
        code += str(randrange(0,9,2))
    return code