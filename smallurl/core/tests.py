from django.test import TestCase

from smallurl.core.utils import generate_code


class CodeGeneratorTest(TestCase):
    def test_custom_code_chars(self):
        AVAIABLE_CHARS = ["a"]
        self.assertEqual(10 * "a", generate_code(chars=AVAIABLE_CHARS, length=10))

    def test_zero_code_length(self):
        self.assertEqual(0, len(generate_code(length=0)))
