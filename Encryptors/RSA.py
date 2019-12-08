import Encryptors.Caesar as c
import Encryptors.constant as const
import textwrap as tw


def RSA_encrypt(p, q, m):
    alphabet = const.ALPHABET['rus']
    n = p * q
    phi = (p-1)*(q-1)
    e = 3
    #d = c.Caesar.solve_mod(e, 1, phi)['x1']
    d = 6111579
    #d = 33336667
    cipher = ''
    for letter in m:
        if alphabet.index(letter) < 10:
            cipher += '0' + str(alphabet.index(letter))
        else:
            cipher += str(alphabet.index(letter))
    l = len(cipher)
    cipher = int(cipher)
    c_ = (cipher ** e) % n
    print(c_)
    return d, toStr(c_, l)

def RSA_derypt(p, q, d, m):
    alphabet = const.ALPHABET['rus']
    n = p * q
    cipher = ''
    for letter in m:
        if alphabet.index(letter) < 10:
            cipher += '0' + str(alphabet.index(letter))
        else:
            cipher += str(alphabet.index(letter))
    l = len(cipher)
    cipher = int(cipher)
    cipher = 252817
    c_ = cipher % n
    for i in range(1, d, 1):
        c_ *= cipher
        c_ = c_ % n
    return c_
    #return toStr(c_, l)

def toStr(cipher, l):
    alphabet = const.ALPHABET['rus']
    cipher = str(cipher)
    a = len(cipher)
    if a % 2 != 0:
        cipher = '0' + cipher
    cipher = tw.wrap(cipher, 2)
    decryptedText = ''
    for number in cipher:
        decryptedText += alphabet[int(number) % len(alphabet)]
    return decryptedText

p = 3557
q = 2579
m = "ваза"
d, m_ = RSA_encrypt(p, q, m)
print(d, m_)
m1_ = RSA_derypt(p, q, d, m_)
print(m1_)
print(toStr(m1_, len(str(m1_))))
#print(RSA_derypt(1002, 1011, "ацбв", 674007))
#print(toStr(24795086 % (10001*10002), 4))
