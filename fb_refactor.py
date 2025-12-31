for i in range(1, 16):
    s = ("fizz" * (i % 3 == 0)) + ("buzz" * (i % 5 == 0))
    if s:
        print(s)
    else:
        print(i)

