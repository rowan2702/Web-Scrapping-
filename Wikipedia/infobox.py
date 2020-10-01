import urllib.request, urllib.parse, urllib.error
import re
import ssl
import wptools

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
title = 'Bill Gates'

so = wptools.page(title).get_parse()

infobox = so.data['infobox']

print("\n")

for (key,value) in infobox.items():
    print(key,":",value)

print("\n")
