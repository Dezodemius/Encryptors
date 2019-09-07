#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Cardan grille.
import numpy as np
import math as m


class Cardan:
    """Cardan grille class

    Contains methods for encrypting and decrypting strings using Cardan grille encryption.
    """
    @staticmethod
    def encrypt16(text):
        """Encryption message with Cardan grille
        Use next mask for encryption:
        |_|1|_|2|
        |_|_|_|_|
        |_|_|4|3|
        |_|_|_|_|

        :param text: input text (must contain 16 letters)
        :return: encrypted grille
        """
        grille = np.zeros((4, 4))

        text = [letter for letter in text if letter.isalpha()]

        if m.sqrt((len(text))) % 1 != 0:
            return "Please choose different phrase!"

        for i in range(0, len(text)-3, 4):
            grille[0][1] = i
            grille[0][3] = i + 1
            grille[2][3] = i + 2
            grille[2][2] = i + 3

            grille = np.rot90(grille, 1)

        return Cardan.explain(text, grille)

    @staticmethod
    def decrypt16(grille):
        """Decryption message with Cardan grille
        Use next mask for decryption:
        |_|1|_|2|
        |_|_|_|_|
        |_|_|4|3|
        |_|_|_|_|

        :param grille: array containing encrypted string indices
        :return: decrypted string
        """
        decrypted_text = ''

        for i in range(4):
            decrypted_text += grille[0][1] + grille[0][3] + grille[2][3] + grille[2][2]
            grille = np.rot90(grille)

        return decrypted_text

    @staticmethod
    def explain(text, grille):
        """Method is used to fill the list with letters

        :param text: used string
        :param grille: used grille for explaining
        :return: list with letters
        """
        explained_grille = []
        for i in range(grille.shape[0]):
            temp = []
            for j in range(grille.shape[1]):
                temp.append(text[int(grille[i][j])])
            explained_grille.append(temp)
        return explained_grille


if __name__ == "__main__":
    print(Cardan.encrypt16("Где мне взять фразу"))
    print(Cardan.decrypt16(Cardan.encrypt16("Где мне взять фразу")))