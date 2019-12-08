#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Caesar cipher
import math
import io


class Caesar:
    """Caesar cipher class.

    Contains methods for encrypting or decrypting strings using Caesar encryption method.
    """
    from Encryptors.constant import ALPHABET

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
            alphabet = Caesar.ALPHABET[language.lower()]
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
            alphabet = Caesar.ALPHABET[language.lower()]
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

        :param text: string,
        :param shift: int
        :param language: string (default 'rus')
        :return: decrypted text: string

        Encryption of a letter x by a shift can be described mathematically as
            Dn(x) = (x - shift) mod n,
        were n is cardinality of alphabet, means number of letters total.
        Works for negative shifts correctly.
        """
        decrypted_text = ''

        try:
            alphabet = Caesar.ALPHABET[language.lower()]
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

    @staticmethod
    def encrypt_a_b(text, language='rus', *shift):
        """ Шифр сдвига, вроде бы."""
        encrypted_text = ''

        try:
            alphabet = Caesar.ALPHABET[language.lower()]
        except KeyError:
            return 'Selected language is not supported!'

        for letter in text:
            if letter.lower() in alphabet:
                letter_index = ((alphabet.index(letter.lower())) * shift[0] + shift[1]) % len(alphabet)
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
    def decrypt_a_b(text, language='rus'):
        """ Дешифровка шифра сдвига."""
        decrypted_text = ''

        f = io.open("word_rus.txt", 'rb')

        dictionary = f.read().decode("utf-8")

        dictionary = dictionary.split()

        try:
            alphabet = Caesar.ALPHABET[language.lower()]
        except KeyError:
            return 'Selected language is not supported!'

        for a in range(1, len(alphabet)):
            decrypted_text = ""
            for b in range(1, len(alphabet)):
                decrypted_text = ""
                for letter in text:
                    if letter.lower() in alphabet:
                        letter_index = Caesar.solve_mod(a, alphabet.index(letter.lower()) - b, len(alphabet))['x1']

                        try:
                            if letter.isupper():
                                decrypted_text += alphabet[letter_index].upper()

                            else:
                                decrypted_text += alphabet[letter_index]

                        except IndexError as e:
                            return e
                    else:
                        decrypted_text += letter
                #print(decrypted_text, a, b)
                if decrypted_text.lower() in dictionary:
                    print(decrypted_text, a, b)

    @staticmethod
    def mod(a_, b_):
        """ Деление с остатком."""
        q = int(a_ / b_) if a_ >= 0 else (int(a_ / b_) - 1 if b_ > 0 else int(a_ / b_) + 1)
        r = int(math.fabs(a_ - q * b_))
        return q, r

    @staticmethod
    def gcd(a, b):
        """ Наибольший общий делитель чисел."""
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a

        return a + b

        #if a == 0 and b > 0:

            #return b
        #if b == 0 and a > 0:
        #    return a

        #if b == 0:
         #   return a
        #else:
        #    return Caesar.gcd(b, a % b)

    @staticmethod
    def phi(n):
        """ Функция Эйлера."""
        j = 0
        for i in range(1, n):
            if Caesar.gcd(i, n) == 1:
                j += 1
        return j

    # def mhp(a, n, b):
    #    return mod(a**mod(n, phi(b))[1], b)[1]
    @staticmethod
    def mhp(a, n, b):
        """ Возведение в степень больших чисел."""
        return a ** (n % Caesar.phi(b)) % b

    @staticmethod
    def solve_mod(a, b, m):
        """ Решение систем сравнений."""
        if a % Caesar.gcd(a, m) != 0:
            return "Нет решений"
        a = Caesar.mod(a, m)[1]
        b = Caesar.mod(b, m)[1]
        x0 = b * Caesar.mhp(a, Caesar.phi(m) - 1, m)
        x = dict(("x{0}".format(k + 1), Caesar.mod(x0 + m / Caesar.gcd(a, m) * k, m)[1])
                 for k in range(Caesar.gcd(a, m)))
        return x

    @staticmethod
    def g(m):
        """ Это не нужно."""
        for i in range(2 * m):
            print(i, Caesar.mod(i, m))

    @staticmethod
    def find_equations(x, m):
        """ Найти все уравнения, к которым подходит решение x.X"""
        for i in range(m):
            for j in range(m):
                if Caesar.mod(i * x, m)[1] == Caesar.mod(j, m)[1]:
                    print(i, j)

    @staticmethod
    def bigram_encrypt(line, a, b, language="rus"):
        """ Шифрование с помощью биграм."""
        try:
            alphabet = Caesar.ALPHABET[language.lower()]
        except KeyError:
            return 'Selected language is not supported!'

        pairs = [line[i:i + 2] for i in range(0, len(line), 2)]

        decryptedText = ''

        for pair in pairs:
            t = alphabet.index(pair[0]) * len(alphabet) + alphabet.index(pair[1])
            T = a * t + b
            newA = alphabet[Caesar.mod(T, len(alphabet))[0] % len(alphabet)]
            newB = alphabet[Caesar.mod(T, len(alphabet))[1] % len(alphabet)]
            newPair = newA + newB
            decryptedText += newPair
        return decryptedText

    @staticmethod
    def bigram_decrypt(line, a, b, language="rus"):
        """ Дешифровка биграм."""
        try:
            alphabet = Caesar.ALPHABET[language.lower()]
        except KeyError:
            return 'Selected language is not supported!'

        pairs = [line[i:i + 2] for i in range(0, len(line), 2)]
        decryptedText = ''

        for pair in pairs:
            v = alphabet.index(pair[0]) * len(alphabet) + alphabet.index(pair[1])
            a_ = Caesar.solve_mod(a, 1, len(alphabet)**2)['x1']
            v_ = int((v - b) * a_)
            newA = alphabet[Caesar.mod(v_, len(alphabet))[0] % len(alphabet)]
            newB = alphabet[Caesar.mod(v_, len(alphabet))[1] % len(alphabet)]
            decryptedText += newA + newB
        return decryptedText

if __name__ == '__main__':
    # print("Not executable!")
    # print(Caesar.encrypt_a_b("ваза", "rus", 2, 3))
    # print(Caesar.encrypt_a_b("БАБА", "rus", 23, 6))
    #Caesar.decrypt_a_b("ТГУГВФ")
    print(Caesar.bigram_encrypt("роза", 2, 2))
    print(Caesar.bigram_decrypt("бяпв", 2, 2))
