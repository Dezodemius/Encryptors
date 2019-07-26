from unittest import TestCase
from Caesar import encrypt, encrypt_modular, decrypt_modular


class CaesarTestCase(TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt("Чу, я слышу пушек гром!", 3), "Ъц, в фоюыц тцызн ёусп!")
        self.assertEqual(encrypt("Hello world!", 15, 'eng'), "Wtaad ldgas!")
        self.assertEqual(encrypt("Hello world!", 15, 'rus'), "Hello world!")
        self.assertEqual(encrypt("Чу, я слышу пушек гром!", 15, 'eng'), "Чу, я слышу пушек гром!")
        self.assertEqual(encrypt("Ви говорите англійською?", 1, 'ukr'), "Selected language is not supported!")
        self.assertEqual(encrypt("Oops!", 0), "Oops!")
        self.assertEqual(encrypt("Упс!", 0), "Упс!")
        self.assertEqual(encrypt("", 10, 'rus'), "")
        self.assertEqual(encrypt("", 10, 'eng'), "")
        self.assertEqual(
            encrypt("Чу, я слышу пушек гром!", 100, 'rus'),
            "Shift greater than the number of letters of the alphabet!")
        self.assertEqual(encrypt("Hello world!", -3, 'eng'), encrypt("Hello world!", 23, 'eng'))
        self.assertEqual(encrypt("Hello world!", 0.15, 'eng'), "Shift is not integer number!")

    def test_encrypt_modular(self):
        self.assertEqual(encrypt_modular("Чу, я слышу пушек гром!", 3), "Ъц, в фоюыц тцызн ёусп!")
        self.assertEqual(encrypt_modular("Hello world!", 15, 'eng'), "Wtaad ldgas!")
        self.assertEqual(encrypt_modular("Hello world!", 15, 'rus'), "Hello world!")
        self.assertEqual(encrypt_modular("Чу, я слышу пушек гром!", 15, 'eng'), "Чу, я слышу пушек гром!")
        self.assertEqual(encrypt_modular("Ви говорите англійською?", 1, 'ukr'), "Selected language is not supported!")
        self.assertEqual(encrypt_modular("Oops!", 0), "Oops!")
        self.assertEqual(encrypt_modular("Упс!", 0), "Упс!")
        self.assertEqual(encrypt_modular("", 10, 'rus'), "")
        self.assertEqual(encrypt_modular("", 10, 'eng'), "")
        self.assertEqual(encrypt_modular("Чу, я слышу пушек гром!", 100, 'rus'), "Шф, а тмьщф рфщёл дспн!")
        self.assertEqual(encrypt_modular("Hello world!", -3, 'eng'), encrypt_modular("Hello world!", 23, 'eng'))
        self.assertEqual(encrypt_modular("Hello world!", 0.15, 'eng'), "Shift is not integer number!")

    def test_decrypt_modular(self):
        self.assertEqual(decrypt_modular("Ъц, в фоюыц тцызн ёусп!", 3), "Чу, я слышу пушек гром!")
        self.assertEqual(decrypt_modular("Wtaad ldgas!", 15, 'eng'), "Hello world!")
        self.assertEqual(decrypt_modular("Hello world!", 15, 'rus'), "Hello world!")
        self.assertEqual(decrypt_modular("Чу, я слышу пушек гром!", 15, 'eng'), "Чу, я слышу пушек гром!")
        self.assertEqual(decrypt_modular("Ви говорите англійською?", 1, 'ukr'), "Selected language is not supported!")
        self.assertEqual(decrypt_modular("Oops!", 0), "Oops!")
        self.assertEqual(decrypt_modular("Упс!", 0), "Упс!")
        self.assertEqual(decrypt_modular("", 10, 'rus'), "")
        self.assertEqual(decrypt_modular("", 10, 'eng'), "")
        self.assertEqual(decrypt_modular("Чу, я слышу пушек гром!", 100, 'rus'), "Цт, ю ркъчт отчдй впнл!")
        self.assertEqual(decrypt_modular("Hello world!", -3, 'eng'), decrypt_modular("Hello world!", 23, 'eng'))
        self.assertEqual(decrypt_modular("Hello world!", 0.15, 'eng'), "Shift is not integer number!")


