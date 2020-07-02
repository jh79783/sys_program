def add(foo, bar):
    out = [f + b for f, b in zip(foo, bar)]
    return out


def subtract(foo, bar):
    out = [f - b for f, b in zip(foo, bar)]
    return out


def multiply(foo, bar):
    out = [f * b for f, b in zip(foo, bar)]
    return out


def divide(foo, bar):
    out = [f / b for f, b in zip(foo, bar)]
    return out


spam = [51, 23]
ham = [34, 67]
if __name__ == '__main__':
    eggs = add(spam, ham)

