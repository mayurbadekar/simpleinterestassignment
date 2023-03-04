def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)
    s = (p * t * r) / 100

    print(f"The Simple Interest is {s}")
    return s

simple_interest(6, 6, 3)