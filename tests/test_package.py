
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


""" Test Simple Package"""


import pytest

from simple_package import say_hello, who_are_you


@pytest.mark.parametrize("test_input, expected_output",
                            [
                                (None, 'I am Python'),
                                ('Asif', 'I am Asif'),
                                ('Iron Man', 'I am Iron Man'),
                            ]
                        )
def test_who_are_you(test_input, expected_output):
    assert who_are_you(test_input) == expected_output


@pytest.mark.parametrize("test_input, expected_output",
                            [
                                (None, 'Hello, World'),
                                ('Asif', 'Hello, Asif'),
                                ('Iron Man', 'Hello, Iron Man'),
                            ]
                        )
def test_say_hello(test_input, expected_output):
    assert say_hello(test_input) == expected_output