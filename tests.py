#!/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import TestCase

from Encryptors import Caesar, testing_decorators


class CaesarTestCase(TestCase):
    @testing_decorators.stopwatch
    def setUp(self):
        self.c = Caesar.Caesar()

    @testing_decorators.stopwatch
    def tearDown(self):
        del self.c

    @testing_decorators.stopwatch
    @testing_decorators.average_runtime(100)
    def test_encrypt(self):
        self.assertEqual(self.c.encrypt("Чу, я слышу пушек гром!", 3), "Ъц, в фоюыц тцызн ёусп!")
        self.assertEqual(self.c.encrypt("Hello world!", 15, 'eng'), "Wtaad ldgas!")
        self.assertEqual(self.c.encrypt("Hello world!", 15, 'rus'), "Hello world!")
        self.assertEqual(self.c.encrypt("Чу, я слышу пушек гром!", 15, 'eng'), "Чу, я слышу пушек гром!")
        self.assertEqual(self.c.encrypt("Ви говорите англійською?", 1, 'ukr'), "Selected language is not supported!")
        self.assertEqual(self.c.encrypt("Oops!", 0), "Oops!")
        self.assertEqual(self.c.encrypt("Упс!", 0), "Упс!")
        self.assertEqual(self.c.encrypt("", 10, 'rus'), "")
        self.assertEqual(self.c.encrypt("", 10, 'eng'), "")
        self.assertEqual(self.c.encrypt("Чу, я слышу пушек гром!", 100, 'rus'),
            "Shift greater than the number of letters of the alphabet!")
        self.assertEqual(self.c.encrypt("Hello world!", -3, 'eng'), self.c.encrypt("Hello world!", 23, 'eng'))
        self.assertEqual(self.c.encrypt("Hello world!", 0.15, 'eng'), "Shift is not integer number!")

    @testing_decorators.stopwatch
    @testing_decorators.average_runtime(100)
    def test_encrypt_modular(self):
        self.assertEqual(self.c.encrypt_modular("Чу, я слышу пушек гром!", 3), "Ъц, в фоюыц тцызн ёусп!")
        self.assertEqual(self.c.encrypt_modular("Hello world!", 15, 'eng'), "Wtaad ldgas!")
        self.assertEqual(self.c.encrypt_modular("Hello world!", 15, 'rus'), "Hello world!")
        self.assertEqual(self.c.encrypt_modular("Чу, я слышу пушек гром!", 15, 'eng'), "Чу, я слышу пушек гром!")
        self.assertEqual(self.c.encrypt_modular("Ви говорите англійською?", 1, 'ukr'),
                         "Selected language is not supported!")
        self.assertEqual(self.c.encrypt_modular("Oops!", 0), "Oops!")
        self.assertEqual(self.c.encrypt_modular("Упс!", 0), "Упс!")
        self.assertEqual(self.c.encrypt_modular("", 10, 'rus'), "")
        self.assertEqual(self.c.encrypt_modular("", 10, 'eng'), "")
        self.assertEqual(self.c.encrypt_modular("Чу, я слышу пушек гром!", 100, 'rus'), "Шф, а тмьщф рфщёл дспн!")
        self.assertEqual(self.c.encrypt_modular("Hello world!", -3, 'eng'), self.c.encrypt_modular("Hello world!", 23, 'eng'))
        self.assertEqual(self.c.encrypt_modular("Hello world!", 0.15, 'eng'), "Shift is not integer number!")

    @testing_decorators.stopwatch
    @testing_decorators.average_runtime(100)
    def test_decrypt_modular(self):
        self.assertEqual(self.c.decrypt_modular("Ъц, в фоюыц тцызн ёусп!", 3), "Чу, я слышу пушек гром!")
        self.assertEqual(self.c.decrypt_modular("Wtaad ldgas!", 15, 'eng'), "Hello world!")
        self.assertEqual(self.c.decrypt_modular("Hello world!", 15, 'rus'), "Hello world!")
        self.assertEqual(self.c.decrypt_modular("Чу, я слышу пушек гром!", 15, 'eng'), "Чу, я слышу пушек гром!")
        self.assertEqual(self.c.decrypt_modular("Ви говорите англійською?", 1, 'ukr'),
                         "Selected language is not supported!")
        self.assertEqual(self.c.decrypt_modular("Oops!", 0), "Oops!")
        self.assertEqual(self.c.decrypt_modular("Упс!", 0), "Упс!")
        self.assertEqual(self.c.decrypt_modular("", 10, 'rus'), "")
        self.assertEqual(self.c.decrypt_modular("", 10, 'eng'), "")
        self.assertEqual(self.c.decrypt_modular("Чу, я слышу пушек гром!", 100, 'rus'), "Цт, ю ркъчт отчдй впнл!")
        self.assertEqual(self.c.decrypt_modular("Hello world!", -3, 'eng'), self.c.decrypt_modular("Hello world!", 23, 'eng'))
        self.assertEqual(self.c.decrypt_modular("Hello world!", 0.15, 'eng'), "Shift is not integer number!")


