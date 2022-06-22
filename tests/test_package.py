from why_this import check_val
from .config import SIMPLE_CONFIG
import pytest


def test_check_val():
	assert check_val(SIMPLE_CONFIG)
