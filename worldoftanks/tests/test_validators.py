import unittest

from worldoftanks.helper.validators import Validators


class TestValidators(unittest.TestCase):

    def test_check_parameters(self):
        result = Validators.check_if_param_exists("param1", "param2")
        expected = True
        self.assertEqual(result, expected)

    def test_wrong_parameters(self):
        self.assertRaises(ValueError, Validators.check_if_param_exists, "1", None)

    def test_wrong_parameter_type(self):
        self.assertRaises(ValueError, Validators.check_if_param_exists, None, "1")
