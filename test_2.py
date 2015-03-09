#! coding: utf-8
from functools import wraps

def deco(deco_name): # wrap a function outside to provide argument input for real deco;
    print "The decorator name:", deco_name
    def _deco(func): # The real deco, take the func as argument;
        print "The decorator name:", deco_name
        @wraps(func)
        def inner_deco(*args, **kwargs): # The inner_deco is used to provide dynamic argument input for func;
            print "The decorator name:", deco_name
            print "Before the call of function:", func.__name__
            print func(*args, **kwargs)
            print "After the call of function:", func.__name__
        return inner_deco
    return _deco

@deco("first deco first func") # It's calling def deco and return _deco.
# execute myfunc = _deco(myfunc), at last myfunc is inner_deco actually. But as the attribute of closure,
# outer function object (like deco_name) can be accessed and retained in the inner_deco.
def myfunc(x, y):
    """
    :param x: the first param
    :param y: the second param
    :return: the return value
    """
    return x - y

@deco("first deco second func")
def myfunc_2(x, y, z):
    return x + y - z

if __name__ == "__main__":
    print "MARK"
    myfunc(y=10, x=5)
    print "ha", myfunc.__name__
    print myfunc.__doc__
    print myfunc.__module__
    myfunc_2(z=2, x=20, y=10)