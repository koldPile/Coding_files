########################################
#ATTENTION THIS INFORMATION HAS BEEN PLACED HERE TO BE USED AS PART OF A TRAINING EXERCISE.  PLEASE DO NOT CONSIDER THIS DATA TO BE FULLY SECURE
# from http://code.activestate.com/recipes/266586-simple-xor-keyword-encryption/
######################################

#MESSAGE FROM 5n0wdr1ft:
#This is pretty much the core part of the code that I use to encrypt my messages that I don't want other people being able to read.  I simply type what I want to say, run it through this code and then it spits out a block of encrypted text at the other side and THAT information is what i send in the message.  Then it is decoded on the other end by the PROPER recipient that I have informed of the decryption key and provided a copy of this code to decypher it.

import os

if os.path.exists('Decoder Dashboard.html')==True:
    os.remove('Decoder Dashboard.html')

def xor_crypt_string(data, key='awesomepassword', encode=False, decode=False):
    from itertools import izip, cycle
    import base64
    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    if encode:
        return base64.encodestring(xored).strip()
    return xored

"""The Unique_User_Modifier is information unique to each user that is used by the program to slightly modifiy the output, making the operation COMPLETELY unique to each user and thus impossible to forceibly decode.  Please remember to keep your Unique_User_Modifier information hidden and apart from the rest of your script!  If an outside party obtains this information they could gain authorization as you!
"""
Unique_User_Modifier=['ZCBzZW5kaW5nIDVuMHdkcmlmdCBhIFBNIGNvbnRhaW5pbmcgdGhlIHdvcmRzICJTT1JSWSIsICJVUlRIRU1BTiIsIGFuZCAiRE9YIiBpbiBhbnkgb3JkZXIgYXMgbG9uZyBhcyB0aGV5IGFyZSBpbiBhbGwgY2Fwcy4gIA0KDQpCZXR0ZXIgbHVjayBuZXh0IHRpbWUuIE1VQUhBSEE=', 'QlVTVEVEISAgWW91IGhhdmUgYmVlbiBkZXRlY3RlZC4gIFRoZSBjb2RlIHlvdSBqdXN0IHJhbiBjb250YWluZWQgYSBoaWRkZW4gcHJvdG9jb2wgdGhhdCBlbWFpbGVkIHlvdXIgT1dOIHBlcnNvbmFsIGluZm9ybWF0aW9uIChTaW11bGF0ZWQgdGhpcyB0aW1lIHNpbmNlIGl0cyBvbmx5IGEgdHJhaW5pbmcgY2hhbGxlbmdlKSB0byA1bjB3ZHIxZnQgSElNU0VMRi4gIFlvdXIgZG94aW', '5nIGNoYWxsZW5nZSBoYXMgYmVlbiBmcm96ZW4gc2luY2UgeW91IGRpZCBub3QgY29tcGxldGUgdGhlIG1pc3Npb24gd2l0aG91dCBiZWluZyBkZXRlY3RlZC4gIFlvdSBjYW4gcmVzdW1lIHRoZSBtaXNzaW9uIGJ5IGxvZ2dpbmcgb250byBIQkgub3JnIGFu']

def encryptedfileparser():
    import webbrowser, base64
    datax=Unique_User_Modifier[1]+Unique_User_Modifier[2]+Unique_User_Modifier[0]
    f=open('Decoder Dashboard.html', 'w+')
    datax2=base64.b64decode(datax)
    f.write(datax2)
    pathex=os.path.abspath('Decoder Dashboard.html')
    f.close()
    bro=webbrowser.open('file:\\'+pathex)

def execute():
    from cStringIO import StringIO
    fileslocation='XXXXXXX' ##Nice Try, not gonna make it that easy for you
    if fileslocation!='XXXXXXX':
        urlpointer="folderview?id=0B2L4m-igEjnnN2ZfOVBacktRbkk&usp=sharing"
        f=StringIO(fileslocation+urlpointer+'\emailmessage.txt')
    if os.path.exists('emailmessage.txt')==True:
        f=open('emailmessage.txt', 'r')
    data=f.read()
    secret_data = data
    print xor_crypt_string(secret_data, encode=True)
    #print xor_crypt_string(xor_crypt_string(secret_data, encode=True), decode=True)
encryptedfileparser()
execute()
