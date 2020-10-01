import urllib.request, urllib.parse, urllib.error
import re
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'https://www.geeksforgeeks.org'

html = urllib.request.urlopen(url, context=ctx).read()

links = re.findall(r'href="(.*?)"', str(html))

for link in links:
	print(link)



# 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999
# 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 
# 2010 2011 2012 2013 2014 		2016 2017 	   2019 2020
