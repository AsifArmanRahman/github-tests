
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


"""Simple Package for Multiple Works and Tests"""


__version__ = '2.0.0.dev1'


def say_hello(name=None):
    """ Say hello to a person.

    :type name: str, 
    :param name: (Optional) Name of a person, defaults to :data:`None`.

    :return: Greets the person hello.
    :rtype: str
    """

    if name is None:
        name = 'Python'

    return f"I am {name}"