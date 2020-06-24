from functools import update_wrapper


def prototype(func):
    def not_implemented(*args, **kw):
        raise NotImplementedError

    annot = func.__annotations__
    impl = not_implemented

    def register(func=None):
        nonlocal impl
        if func.__annotations__ == annot:
            impl = func
        else:
            raise TypeError(f"expected {annot}, got {func.__annotations__}.")
        return func

    def wrapper(*args, **kw):
        return impl(*args, **kw)

    # funcname = getattr(func, "__name__", "prototype function")
    wrapper.register = register
    update_wrapper(wrapper, func)
    return wrapper


@prototype
def mafonction():
    """A"""


@mafonction.register
def impl() -> int:
    """B"""
    return "youhou"


print(mafonction())
