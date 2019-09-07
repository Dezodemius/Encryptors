# <p align="center">Encryptors
* [Getting started.](#getting-started)
* [Caesar cipher.](#caesar-cipher)
* [Vigenere cipher.](#vigenere-cipher)
* [Polybius square cipher.](#polybius-square-cipher)
* [Cardan grille.](#cardan-grille)

## Getting started.

This API is not tested with Python 2.6, Python 2.7, Python 3.4, Pypy and Pypy 3, but don't worry.
There are two ways to install the library:

* Installation using pip (a Python package manager)*:

```
$ pip install -i https://test.pypi.org/simple/ Encryptors
```
* Installation from source (requires git):

```
$ git clone https://github.com/Dezodemius/Encryptors
$ cd Encryptors
$ python setup.py install
```

It is generally recommended to use the first option.

**While the API is production-ready, it is still under development and it has regular updates, do not forget to update it regularly by calling `pip install Encryptors --upgrade`*

What is this?
-
This is a package for Python3 containing encryption methods. May be used for encryption of your messages just for fun
or for learning encryption method.

The Latest Version
-
Details of the latest version of package you can find by

## Caesar cipher.

Each character in the text is replaced by a symbol located on some fixed number of positions to the
left or to the right of it in the alphabet.

Encryption of a letter x by a shift can be described mathematically as

    Dn(x) = (x - shift) mod n

were n is cardinality of alphabet, means number of letters total.


This module contains two realizations of Caesar encryption method:

* using string transformation: `encrypt(...)`

* using modular arithmetic: `encrypt_modular(...)` for encrypt message, and `decrypt_modular(...)` for decrypt.

Import example
-
* `import Encryptors`

* `from Encryptors import *`

* `from Encryptors import Caesar`

* `from Encryptors.Caesar import Caesar as cs` - for Caesar encryption import.

Examples:

```buildoutcfg
>>> cs.encrypt('Съешь же ещё этих мягких французских булок, да выпей чаю.', 3, language='RUS')

'Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн, жг еютзм ъгб.'
```

```buildoutcfg
>>> cs.encrypt_modular("Чу, я слышу пушек гром!", 3)
'Ъц, в фоюыц тцызн ёусп!'
```

```buildoutcfg
>>> cs.decrypt_modular("Ъц, в фоюыц тцызн ёусп!", 3)
'Чу, я слышу пушек гром!'
```

##Vigenere cipher.
In the Vigenere cipher, each character of the phrase that needs to be encrypted, as in Caesar's cipher, is shifted by a certain number of characters in the alphabet with the only difference that this number is inconsistent and depends on the key phrase

This module is based on Caesar's encryptor.

Import example
-
* `import Encryptors`

* `from Encryptors import *`

* `from Encryptors import Vigenere`

* `from Encryptors.Vigenere import Vigenere as vgn` - for Vigenere encryption import.

Examples:

```buildoutcfg
>>> vgn.encrypt("ATTACKATDAWN", "LEMON", "ENG")

'LXFOPVEFRNHR'
```
```buildoutcfg
>>> vgn.decrypt("LXFOPVEFRNHR", "LEMON", "ENG")

'ATTACKATDAWN'
```

```buildoutcfg
>>> vgn.encrypt("завтра пар не будет", "буря", "RUS")
'иутссу обд мё стешг'
```

```buildoutcfg
>>> vgn.encrypt("иутссу обд мё стешг", "буря", "RUS")
'завтра пар не будет'
```

## Polybius square cipher.

## Cardan grille.
