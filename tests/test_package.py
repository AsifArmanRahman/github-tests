
#   Copyright (c) 2022 Asif Arman Rahman
#   Licensed under MIT (https://github.com/AsifArmanRahman/firebase/blob/main/LICENSE)

# --------------------------------------------------------------------------------------


""" Test Simple Package"""


import pytest

from simple_package import say_hello


@pytest.mark.parametrize("test_input, expected_output",
                            [
                                (None, 'I am Python'),
                                ('Asif', 'I am Asif'),
                                ('Iron Man', 'I am Iron Man'),
                            ]
                        )
def test_say_hello(test_input, expected_output):
    assert say_hello(test_input) == expected_output