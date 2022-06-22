from why_this import *
from .config import SIMPLE_CONFIG1, SIMPLE_CONFIG2
import pytest


def test_check_val1():
	assert check_val(SIMPLE_CONFIG1)


def test_check_val2():
	assert not check_val2(SIMPLE_CONFIG1)


def test_check_val3():
	assert check_val2(SIMPLE_CONFIG2)
