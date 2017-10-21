import unittest
import problems


class ValidPinTest(unittest.TestCase):

    def test_is_valid_pin_4_digits(self):
        self.assertTrue(problems.is_valid_pin("1234"))

    def test_is_valid_pin_5_digits(self):
        self.assertFalse(problems.is_valid_pin("12345"))

    def test_is_valid_pin_alnum(self):
        self.assertFalse(problems.is_valid_pin("a234"))


class PalindromeTest(unittest.TestCase):

    def test_is_palindrome_aabb(self):
        self.assertTrue(problems.is_palindrome("aabb"))

    def test_is_palindrome_aabab(self):
        self.assertTrue(problems.is_palindrome("aabab"))

    def test_is_palindrome_madam3(self):
        self.assertFalse(problems.is_palindrome("madam3"))


class RemoveVowelTest(unittest.TestCase):

    def test_has_no_vowels_shiit(self):
        self.assertEqual(problems.remove_vowels("shiit"), "sht")

    def test_has_no_vowels_with_space(self):
        self.assertEqual(problems.remove_vowels(
            "I am called Rodgers"), " m clld Rdgrs")

if __name__ == '__main__':
    unittest.main()
