#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Polybius square encryption.
from Encryptors import constant


class Polybius:
    """Polybius square encryption class.

    Contains methods for encrypting and decrypting strings using Polybius square encryption.
    """

    """Encryption method"""
    @staticmethod
    def encrypt(text, square=constant.SQUARE):
        """Encryption message with Polybius square

        :param text: input text
        :param square: used Polybius square (should be a dictionary). Default is built-in from constant.py
        :return: encrypted text
        """
        encrypted_text = ''
        for letter in text:
            if letter.lower() in square:
                if letter.isupper():
                    encrypted_text += constant.SQUARE[letter.lower()].upper() + " "
                else:
                    encrypted_text += constant.SQUARE[letter.lower()] + " "
            else:
                encrypted_text += ""
        return encrypted_text

    """Decryption method"""
    @staticmethod
    def decrypt(text, square=constant.SQUARE):
        """Decryption message with Polybius square.

        :param text: input text
        :param square: used Polybius square (should be a dictionary). Default is built-in from constant.py
        :return: decrypted text
        """
        square = {val: key for key, val in square.items()}
        encrypted_text = ''
        text = text.split()
        for letter in text:
            if letter.lower() in square:
                if letter.isupper():
                    encrypted_text += square[letter.lower()].upper()
                else:
                    encrypted_text += square[letter.lower()]
            else:
                encrypted_text += ""
        return encrypted_text


if __name__ == "__main__":
    s = "завтра будет теплее"
    print(Polybius.encrypt(s))
    print(Polybius.decrypt(Polybius.encrypt(s)))
