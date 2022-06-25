__version__ = '1.0.0.dev1'


def check_val(value):
	if value == 'ThisIsNotRandom':
		return True

	return False


def check_val2(value):
	if value == 'ThisIsNotRandom':
		return False

	return True
