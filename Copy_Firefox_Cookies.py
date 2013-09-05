#-------------------------------------------------------------------------------
# Name:        Internet Cookies Module
# Purpose:     Copies stored login information from firefox for use in python
#-------------------------------------------------------------------------------
"""
This is a custom module I set up for myself using Guy Rutenberg's cookie copying method.
It will return an opener, mechanize_browser, and loaded cookiejar all ready for use.
This way whatever cookies you have saved in firefox (i.e. site logins etc.) will be loaded into
your python script.  Means not having to deal with storing your password in any form encrypted or otherwise with
the scripts you write.

USAGE:

import ##WHATEVERYOUNAMEDTHISFILE## as newbrowser
opener, br, cj=newbrowser.redsbrowser()

you can send any questions to capitanwinkie2013@gmail.com


"""
import mechanize, cookielib, urllib, re, os, urllib2
from BeautifulSoup import BeautifulSoup

def _getFFcookiedir():
    profilesdir=os.getenv('appdata')+'\\Mozilla\\Firefox\\Profiles\\'
    filesinfodict={}
    for file in os.listdir(profilesdir):
        filesinfodict[os.path.getatime(profilesdir+file)]=file
    profile=filesinfodict[max(filesinfodict)]
    return profilesdir+profile+'\\cookies.sqlite'

def _makeCookieJar(): #kudos to Guy Rutenberg for the heart of this function
    from StringIO import StringIO
    from pysqlite2 import dbapi2 as sqlite
    cj=cookielib.LWPCookieJar()
    cookiefile=_getFFcookiedir()
    con = sqlite.connect(cookiefile)
    cur = con.cursor()
    cur.execute("SELECT host, path, isSecure, expiry, name, value FROM moz_cookies")
    for item in cur.fetchall():
        c = cookielib.Cookie(0, item[4], item[5], None, False, item[0], item[0].startswith('.'), item[0].startswith('.'), item[1], False, item[2], item[3], item[3]=="", None, None, {})
        cj.set_cookie(c)
    return cj

def redsbrowser():
    cj=_makeCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders.append(('User-Agent','Mozilla/5.0'))
    br=mechanize.Browser()
    br.set_cookiejar(cj)
    br.set_handle_robots(False)
    return opener, br, cj

