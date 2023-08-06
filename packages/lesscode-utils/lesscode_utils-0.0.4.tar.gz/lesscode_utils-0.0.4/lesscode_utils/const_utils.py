from functools import wraps


def const_wrap(cls):
    @wraps(cls)
    def _setattr(self, name, value):
        raise Exception('const : {} can not be changed'.format(name))

    cls.__setattr__ = _setattr
    return cls


@const_wrap
class ConstDict:
    pass
