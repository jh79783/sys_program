def add(foo, bar):
    # out = {}
    # for key in foo:
    #     if key in bar:
    #         out[key] = foo[key] + bar[key]
    out = {key: foo[key] + bar[key] for key in foo if key in bar}
    return out


def subtract(foo, bar):
    out = {key: foo[key] - bar[key] for key in foo if key in bar}
    # for key in foo:
    #     if key in bar:
    #         out[key] = foo[key] - bar[key]
    return out


def multiply(foo, bar):
    out = {key: foo[key] * bar[key] for key in foo if key in bar}
    return out


def divide(foo, bar):
    out = {key: foo[key] / bar[key] for key in foo if key in bar}
    # for key in foo:
    #     if key in bar:
    #         out[key] = foo[key] / bar[key]
    return out
