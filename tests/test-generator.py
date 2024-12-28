import unittest
from unique_code_generator.generator import generate_password

class TestGenerator(unittest.TestCase):
    def test_default_length(self):
        """Test pentru lungimea implicita (30 de caractere)"""
        password = generate_password()
        self.assertEqual(len(password), 30)
        
    def test_custom_length(self):
        """Test pentru lungimea personalizata"""
        password = generate_password(34)
        self.assertEqual(len(password), 34)
        
        
    def test_special_characters_excluded(self):
        """Test pentru caracterele speciale excluse"""
        password = generate_password(include_special_chars=False)
        special_chars = "!@#$%^&*()-_+=[]{}|;:,.<>?/"
        self.assertFalse(any(char in special_chars for char in password))
        
    def test_randomness(self):
        """Test pentru a verifica ca parolele sunt unice."""
        passwords = {generate_password() for _ in range(100)}
        self.assertEqual(len(passwords), 100)  # Toate parolele ar trebui sa fie unice.

if __name__ == "__main__":
    unittest.main()