#encrypts/decrypts text using a password

from random import randrange

def encrypt_a_message(text, key=''):
    key=(sum([ord(s) for s in key]))/len(key)
    rezult=''
    for i in text:
        curval=ord(i)+key
        num1=curval/3+randrange(-10, 10)
        num2=curval/3+randrange(-10, 10)
        num3=curval-(num1+num2)
        rezult+="%s%s%s" % (chr(num1), chr(num2), chr(num3))
    return rezult

def decrypt_a_message(text, key=''):
    data=[int(ord(i)) for i in text]
    data=[data[value]+data[value+1]+data[value+2] for value in xrange(len(data)) if value%3 ==0]
    key=(sum([ord(s) for s in key]))/len(key)
    dekrypted=''
    for num in data:
        dekrypted+=chr(num-key)
    return dekrypted
