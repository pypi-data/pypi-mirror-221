import unittest
from generate_password import generate_password, names

class TestGeneratePassword(unittest.TestCase):

    def test_password_length(self):
        # Test the length of the generated password
        password = generate_password()
        self.assertGreaterEqual(len(password), 6)
        self.assertLessEqual(len(password), 12)

    def test_password_requirements(self):
        # Test if the generated password meets the specified requirements
        password = generate_password()
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertNotIn(password.lower(), names)

if __name__ == '__main__':
    unittest.main()
    
    
#python -m unittest test_generate_password.py

