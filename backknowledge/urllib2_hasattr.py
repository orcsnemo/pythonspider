from urllib2 import Request,urlopen,HTTPError,URLError
req = Request('http://bbs.csdn.net/callmewhy')

try:
	respone=urlopen(req)

except URLError,e:
	if hasattr(e,'reason'):
		print "Failed to reach server."
		print "Reason:", e.reason
	elif hasattr(e,'code'):
		print 'The server failed to fuifill the request.'
		print 'Error code', e.code
else:
	print "No excetpion was raised."
