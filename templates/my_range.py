def my_range(start, stop, f):
    x = start
    while x < stop if stop > start else x > stop:
        yield x
        x = f(x)
