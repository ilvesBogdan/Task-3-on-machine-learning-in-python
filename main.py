def question1(i: int) -> str:
    """Решение задания 1"""
    result = ' '.join((
        '' if i % 3 else 'Fizz',
        '' if i % 5 else 'Buzz'
    ))
    # Простите мне этот ужас =)
    return str(i) if ' ' == result else result


def question2(x: int) -> str:
    """Решение задания 2"""
    if x % 2:  return "Плохо"
    if x > 20: return "Отлично"
    if x > 5:  return "Так себе"
    if x > 1:  return "Неплохо"


def question3(x: int) -> str:
    """Решение задания 3"""
    return ''.join(map(str, range(1, x + 1)))


def question4(text: str) -> str:
    """Решение задания 4"""
    return ''.join(filter(lambda c: c.isupper(), text))


def question5(text: str) -> bool:
    """Решение задания 5"""
    for i, word in enumerate(text.split()):
        if word.isnumeric():
            return False
        if 1 < i:
            return True


def question6(*argv: str) -> str:
    """Решение задания 6"""
    return ','.join(map(lambda w: w.replace('right', 'left'), argv))


if __name__ == '__main__':
    print('\n Задание 1:', question1(5))
    print('\n Задание 2:', question2(24))
    print('\n Задание 3:', question3(9))
    print('\n Задание 4:', question4("How are you? Eh, ok. Low or Lower? Ohhh."))
    print('\n Задание 5:', question5("1 2 3 4"))
    print('\n Задание 6:', question6("bright aright", "ok"))
