
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


"""Simple Package for Multiple Works and Tests"""


def who_are_you(name=None):
    """ Replies who the person is.

    :type name: str, 
    :param name: (Optional) Name of a person, defaults to :data:`None`.

    :return: Person telling his name.
    :rtype: str
    """

    if name is None:
        name = 'Python'

    return f"I am {name}"


def say_hello(name=None):
    """ Say hello to a person.

    :type name: str, 
    :param name: (Optional) Name of a person, defaults to :data:`None`.

    :return: Greets the person hello.
    :rtype: str
    """

    if name is None:
        name = 'World'

    return f"Hello, {name}"


def say_goodbye(name=None):
    """ Say goodbye to a person.

    :type name: str, 
    :param name: (Optional) Name of a person, defaults to :data:`None`.

    :return: Greets the person goodbye.
    :rtype: str
    """

    if name is None:
        name = 'World'

    return f"Goodbye, {name}"
