from functools import partial, reduce as ft_reduce


def pipe(value, *functions):
    for func in functions:        
        value = func(value)
        if hasattr(pipe, "debug") and pipe.debug:
            print(value)
    return value


def each(selector):
    return partial(map, selector)


def where(selector):
    return partial(filter, selector)


def reduce(selector, initial=0):
    f = lambda func, initial, iterable: ft_reduce(func, iterable, initial)
    return partial(f, selector, initial)