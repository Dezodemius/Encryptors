#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Caesar Encryptor.
from Encryptors.constant import ALPHABET


class Caesar:
    """Caesar cipher class.

    Contains methods for encrypting and decrypting strings using Caesar encryption method.
    """

    @staticmethod
    def encrypt(text, shift, language='rus'):
        """Caesar cipher.

        Input:
            text: string,
            shift: int
            language: string (default 'rus')
        Return: Each character in the text is replaced by a symbol located on some fixed number of positions to the
        left or to the right of it in the alphabet.
        """
        encrypted_text = ''

        try:
            alphabet = ALPHABET[language.lower()]
        except KeyError:
            return 'Selected language is not supported!'

        if shift > len(alphabet):
            return 'Shift greater than the number of letters of the alphabet!'

        if type(shift) is not int:
            return 'Shift is not integer number!'

        for letter in text:
            if letter.lower() in alphabet:
                letter_index = alphabet.index(letter.lower())

                if letter.isupper():
                    try:
                        encrypted_text += alphabet[letter_index + shift].upper()
                    except IndexError:
                        encrypted_text += alphabet[shift - (len(alphabet) - letter_index)].upper()
                else:
                    try:
                        encrypted_text += alphabet[letter_index + shift]
                    except IndexError:
                        encrypted_text += alphabet[shift - (len(alphabet) - letter_index)]
            else:
                encrypted_text += letter
        return encrypted_text

    @staticmethod
    def encrypt_modular(text, shift, language='rus'):
        """Encryption message with Caesar cipher based on Modular arithmetic.

        Input:
            text: string,
            shift: int
            language: string (default 'rus')
        Return:
            Encrypted text: string

        Encryption of a letter x by a shift n can be described mathematically as
            En(x) = (x + shift) mod n,
        were n is cardinality of alphabet, means number of letters total.
        Works for negative shifts correctly.
        """
        encrypted_text = ''

        try:
            alphabet = ALPHABET[language.lower()]
        except KeyError:
            return 'Selected language is not supported!'

        if type(shift) is not int:
            return 'Shift is not integer number!'

        for letter in text:
            if letter.lower() in alphabet:
                letter_index = (alphabet.index(letter.lower()) + shift) % len(alphabet)

                try:
                    if letter.isupper():
                        encrypted_text += alphabet[letter_index].upper()

                    else:
                        encrypted_text += alphabet[letter_index]

                except IndexError as e:
                    return e

            else:
                encrypted_text += letter

        return encrypted_text

    @staticmethod
    def decrypt_modular(text, shift, language='rus'):
        """Decryption message with Caesar cipher based on Modular arithmetic.

        Input:
            text: string,
            shift: int
            language: string (default 'rus')
        Return:
            Decrypted text: string

        Encryption of a letter x by a shift can be described mathematically as
            Dn(x) = (x - shift) mod n,
        were n is cardinality of alphabet, means number of letters total.
        Works for negative shifts correctly.
        """
        decrypted_text = ''

        try:
            alphabet = ALPHABET[language.lower()]
        except KeyError:
            return 'Selected language is not supported!'

        if type(shift) is not int:
            return 'Shift is not integer number!'

        for letter in text:
            if letter.lower() in alphabet:
                letter_index = (alphabet.index(letter.lower()) - shift) % len(alphabet)

                try:
                    if letter.isupper():
                        decrypted_text += alphabet[letter_index].upper()

                    else:
                        decrypted_text += alphabet[letter_index]

                except IndexError as e:
                    return e
            else:
                decrypted_text += letter

        return decrypted_text


if __name__ == '__main__':
    print("Not executable!")
