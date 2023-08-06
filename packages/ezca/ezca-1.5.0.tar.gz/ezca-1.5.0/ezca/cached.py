import weakref

# Python Cookbook 9.13: Using a Metaclass to Control Instance Creation
class Cached(type):
    def __init__(self, *args, **kwargs):
        super(Cached, self).__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        kwargs_list = tuple(kwargs.items())

        # convert any lists in args to tuples
        args = list(args)
        for i, arg in enumerate(args):
            if isinstance(arg, list):
                args[i] = tuple(arg)
        for key, value in kwargs_list:
            if isinstance(value, list):
                kwargs[key] = tuple(value)
        args = tuple(args)

        # FIXME: the following should be used >=2.7
        #key = (args, tuple(kwargs.viewitems()))
        key = (args, kwargs_list)
        if key in cls.__cache:
            return cls.__cache[key]
        else:
            obj = super(Cached, cls).__call__(*args, **kwargs)
            cls.__cache[key] = obj
            return obj
