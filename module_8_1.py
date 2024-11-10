def add_everything_up(a, b):
    sum = 0
    try:
        sum = a + b

    except TypeError:
        if isinstance(a, str) and (isinstance(b, int) or isinstance(b, float)):
            b = str(b)
            sum = a+b
        elif isinstance(b, str) and (isinstance(a, int) or isinstance(a, float)):
            a = str(a)
            sum = a + b

    return sum

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
