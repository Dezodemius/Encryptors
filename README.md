What is this?
-
This is a package for Python3 containing encryption methods. May be used for encryption of your messages just for fun
or for learning encryption method. 

The Latest Version
-
Details of the latest version of package you can find by

Caesar encryption method
-
Each character in the text is replaced by a symbol located on some fixed number of positions to the
left or to the right of it in the alphabet.

Encryption of a letter x by a shift can be described mathematically as
        
    Dn(x) = (x - shift) mod n
        
were n is cardinality of alphabet, means number of letters total.


This module contains two realizations of Caesar encryption method:

* using string transformation: `encrypt(...)` 

* using modular arithmetic: `encrypt_modular(...)` for encrypt message, and `decrypt_modular(...)` for decrypt.

Installation
-
For installation use `setup.py`.

Import example
-
* `import Encryptors`

* `from Encryptors import *`

* `from Encryptors import Caesar`

* `from Encryptors.Caesar import Caesar as cs` - for Caesar encryption import.

Examples
-

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
