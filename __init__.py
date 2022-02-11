from hashlib import sha256 , md5 , sha224 , sha512 , sha1
import binascii
import os

def XorEncode(key,string):   
    keys1 = str(sha256(key.encode ('UTF-8')).hexdigest())
    keys2 = str(md5(key.encode ('UTF-8')).hexdigest())
    keys3 = str(sha224(key.encode ('UTF-8')).hexdigest())
    keys4 = str(sha512(key.encode ('UTF-8')).hexdigest())
    keys5 = str(sha1(key.encode ('UTF-8')).hexdigest())

    keys = keys1 + keys2 + keys3 + keys4 + keys5
    keys = keys + keys4 + keys3 + keys2 +keys1 + keys

    binary_string = '0' + bin(int.from_bytes(string.encode(), 'big'))[2:]
    binary_keys = '0' + bin(int.from_bytes(keys.encode(), 'big'))[2:]

    while len(binary_string) >> len(binary_keys):
         binary_keys += binary_keys
    list_string = list(binary_string)
    list_key = list(binary_keys)

    len_string = len(binary_string)

    a = 0
    result = ""
    for loop in range(len_string):
        if list_key[a] == list_string[a]:
           result = result + "1"
        else:
            result = result + "0"
        a = a + 1

    return(result)

def XorDecode(key,string):
    keys1 = str(sha256(key.encode ('UTF-8')).hexdigest())
    keys2 = str(md5(key.encode ('UTF-8')).hexdigest())
    keys3 = str(sha224(key.encode ('UTF-8')).hexdigest())
    keys4 = str(sha512(key.encode ('UTF-8')).hexdigest())
    keys5 = str(sha1(key.encode ('UTF-8')).hexdigest())

    keys = keys1 + keys2 + keys3 + keys4 + keys5
    keys = keys + keys4 + keys3 + keys2 +keys1 + keys

    binary_string = string
    binary_keys = '0' + bin(int.from_bytes(keys.encode(), 'big'))[2:]

    while len(binary_string) >> len(binary_keys):
        binary_keys += binary_keys

    list_string = list(binary_string)
    list_key = list(binary_keys)


    longueur_string = len(binary_string)


    a = 0
    resultat_binaire = ""
    for loop in range(longueur_string):
        if list_key[a] == list_string[a]:
            resultat_binaire = resultat_binaire + "1"
        else:
            resultat_binaire = resultat_binaire + "0"
        a = a + 1
    binary_int = int(resultat_binaire, 2)
    byte_number = binary_int.bit_length()
    binary_array = binary_int.to_bytes(byte_number, "big")
    result = binary_array.decode()
    result_list = list(result)
    first_char = result_list[1]
    while result.startswith(first_char):
        result = result[1:]
    return(result)