class Caesar:
    """Caesar cipher class.

    Contains methods for encrypting or decrypting strings using Caesar encryption method.
    """
    ALPHABET = {
        'rus': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
        'eng': 'abcdefghijklmnopqrstuvwxyz'
    }

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


if __name__ == '__main__':
    c = Caesar()
    print("Example:")
    print(c.encrypt.__name__, c.encrypt('Съешь же ещё этих мягких французских булок, да выпей чаю.', 3, language='RUS'))
    print(c.encrypt_modular.__name__, c.encrypt_modular('Чу, я слышу пушек гром!', 3, language='RUS'))
    print(c.decrypt_modular.__name__, c.decrypt_modular('Ъц, в фоюыц тцызн ёусп!', 3, language='RUS'))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert c.encrypt("Чу, я слышу пушек гром!", 3) == "Ъц, в фоюыц тцызн ёусп!", "Check russian"
    assert c.encrypt(text="Hello world!", shift=15, language='eng') == "Wtaad ldgas!", "Check english"
    assert c.encrypt("Hello world!", 15, 'rus') == "Hello world!", "Check wrong language (english)"
    assert c.encrypt("Чу, я слышу пушек гром!", 15, 'eng') == "Чу, я слышу пушек гром!", \
        "Check wrong language (russian)"
    assert c.encrypt("Ви говорите англійською?", 1, 'ukr') == "Selected language is not supported!", "Check ukrainian"
    assert c.encrypt("Oops!", 0) == "Oops!", "English without changes"
    assert c.encrypt("Упс!", 0) == "Упс!", "Russian without changes."
    assert c.encrypt("", 10, 'rus') == "", "Empty string (russian)"
    assert c.encrypt("", 10, 'eng') == "", "Empty string (english)"
    assert c.encrypt("Hello world!", -3, 'eng') == c.encrypt("Hello world!", 23, 'eng'), "Negative shift"
    assert c.encrypt("Hello world!", 0.15, 'eng') == "Shift is not integer number!", "Shift is not int"
    print("The local tests are done.")
