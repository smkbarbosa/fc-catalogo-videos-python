import unittest

from __seedwork.application.use_case import UseCase


class TestUseCasesUnit(unittest.TestCase):
    def test_throw_error_when_execute_method_not_implemented(self):
        with self.assertRaises(TypeError) as assert_error:
            UseCase().execute()
        self.assertEqual(assert_error.exception.args[0], "Can't instantiate abstract class UseCase with abstract" +
                         "method execute")
