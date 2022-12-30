import random

KEY_LENGTH = 20


def generateKey():
    hashKey = ""
    for i in range(KEY_LENGTH):
        ch = chr(random.randint(33, 126)) #ASCII value to char conversion
        hashKey = hashKey + ch

    return hashKey

def generateHash(hashKey, ans, BASE, MOD):
    hashValue = 0
    for i in range(KEY_LENGTH):
        ch = hashKey[i]
        if (i % 7 == 0 or i % 11 == 0):
            ch = ans  # char to ASCII value conversion

        hashValue = ((hashValue * BASE) % MOD + ord(ch)) % MOD

    return hashValue
