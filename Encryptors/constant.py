#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Dictionary of alphabets. Using in Caesar and Vigenere ciphers
ALPHABET = {
        'rus': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
        'eng': 'abcdefghijklmnopqrstuvwxyz'
    }
# Square
SQUARE = {'а': 'a1', 'б': 'b1', 'в': 'c1', 'г': 'd1', 'д': 'e1', 'е': 'f1',
          'ё': 'f2', 'ж': 'e2', 'з': 'd2', 'и': 'c2', 'й': 'b2', 'к': 'a2',
          'л': 'a3', 'м': 'b3', 'н': 'c3', 'о': 'd3', 'п': 'e3', 'р': 'f3',
          'с': 'f4', 'т': 'e4', 'у': 'd4', 'ф': 'c4', 'х': 'b4', 'ц': 'a4',
          'ч': 'a5', 'ш': 'b5', 'щ': 'c5', 'ъ': 'd5', 'ы': 'e5', 'ь': 'f5',
          'э': 'f6', 'ю': 'e6', 'я': 'd6', ' ': 'c6', '.': 'b6', ',': 'a6'}

DE_SQUARE = {val: key for key, val in SQUARE.items()}
if __name__ == "__main__":
    print("Not executable!")
