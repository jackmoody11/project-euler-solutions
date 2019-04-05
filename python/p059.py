import csv
import os
from itertools import chain

ASCII_LIST = list(range(32, 127))

def is_english_char(a1, a2):
    if a1 ^ a2 in ASCII_LIST:
        return True
    return False

def valid_message(message, key):
    """
    We expect a long message to contain the words 'the' and 'and'. 
    Therefore, we limit the search to deciphered messages that contain 
    these words. If these words are in the message, we will consider the message 
    valid. The message can then be checked further.
    """
    decoded = decode_as_chr(message, key)
    return 'the ' in decoded and 'and ' in decoded

def decode_as_int(cipher, key):
    m = [cipher[i] ^ key[i % len(key)] for i in range(len(cipher))]
    return m

def decode_as_chr(cipher, key):
    m = ''.join([chr(cipher[i] ^ key[i % len(key)]) for i in range(len(cipher))])
    return m

def get_message():
    filename = os.getcwd() + '/p059.txt'
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        nums = list(map(int, list(reader)[0]))
    return nums

def message_search(nums):
    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                if valid_message(nums, [i, j, k]):
                    return(i, j, k)
        
def compute():
    message = get_message()
    key = message_search(message)
    return sum(decode_as_int(message, key))


if __name__ == "__main__":
    # message = get_message()
    # # See the message
    # key = message_search(message)
    # print('MESSAGE: ', decode_as_chr(message, key))

    # # See the key
    # print('KEY: ', ''.join([chr(k) for k in key]))
    print(compute())