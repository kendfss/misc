def sqrt(square, steps=100, start=20):
    xn = lambda c, x0: .5 * (x0 + (c / x0))
    while steps - 1:
        start = xn(square, start)
        steps -= 1
    return start