#ATTN ALL VIEWERS
#Please Be Advised that this code is being used in a training
#exercise and is deliberately NOT SECURE.  Please find another code for
#anyone who is searching for a secure way of encoding messages to prevent
#unauthorized viewing.
# from http://code.activestate.com/recipes/266586-simple-xor-keyword-encryption/

import os

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

def xor_crypt_string(data, key='awesomepassword', encode=False, decode=False):
    from itertools import izip, cycle
    import base64
    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    if encode:
        return base64.encodestring(xored).strip()
    return xored

encryptedfileparser()

##f=open('emailmessage.txt', 'r')
##data=f.read()
##secret_data = data
##print xor_crypt_string(secret_data, encode=True)
##print xor_crypt_string(xor_crypt_string(secret_data, encode=True), decode=True)
