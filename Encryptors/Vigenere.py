#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Vigenere Encryptor.
from Encryptors.constant import ALPHABET
from Encryptors.Caesar import Caesar


class Vigenere:
    """Vigenere cipher class.

    Contains methods for encrypting and decrypting messages using Vigenere encryption method.
    """

    @staticmethod
    def encrypt(text, key, language='rus'):
        """Encryption message with Vigenere cipher.

        :param text: string,
        :param key: string
        :param language: string (default 'rus')
        :return encrypted_text: string
        """
        encrypted_text = ''

        try:
            alphabet = ALPHABET[language.lower()]
        except KeyError:
            return 'Selected language is not supported!'

        for i in range(len(text)):
            if text[i].lower() in alphabet:
                new_key = key[i % len(key)].lower()
                encrypted_text += Caesar.encrypt_modular(text[i], shift=alphabet.index(new_key), language=language)
            else:
                encrypted_text += text[i]
        return encrypted_text

    @staticmethod
    def decrypt(text, key, language='rus'):
        """Decryption message with Vigenere cipher.

        :param text: string,
        :param key: string
        :param language: string (default 'rus')
        :return decrypted_text: string
        """
        encrypted_text = ''

        try:
            alphabet = ALPHABET[language.lower()]
        except KeyError:
            return 'Selected language is not supported!'

        for i in range(len(text)):
            if text[i].lower() in alphabet:
                try:
                    new_key = key[i % len(key)].lower()
                    encrypted_text += Caesar.decrypt_modular(text[i], shift=alphabet.index(new_key), language=language)
                except ValueError as e:
                    print(e, '\nThe key contains numbers! Please select a key with letters only.')
                    return None
            else:
                encrypted_text += text[i]
        return encrypted_text


if __name__ == "__main__":
    v = Vigenere()
    print("Example")
    print("Original text: {0}, key: {1}, encrypted: {2}".format("ATTACKATDAWN", "LEMON", v.encrypt("ATTACKATDAWN", "LEMON", "ENG")))
    print("Original text: {0}, key: {1}, encrypted: {2}".format("завтра пар не будет", "буря",
                                                                v.encrypt("завтра пар не будет", "буря", "RUS")))
    print("Original text: {0}, key: {1}, encrypted: {2}".format("иутссу обд мё стешг", "буря",
                                                                v.decrypt("иутссу обд мё стешг", "буря", "RUS")))
    print("Original text: {0}, key: {1}, encrypted: {2}".format("LXFOPVEFRNHR", "LEMON", v.decrypt("LXFOPVEFRNHR", "LEMON", "ENG")))