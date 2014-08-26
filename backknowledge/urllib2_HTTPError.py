from urllib2 import Request,urlopen,URLError,HTTPError
req = Request('http:/bbs.csdn.net/callmewhy')
try:
	response=urlopen(req)
except HTTPError,e:
	print "The server could't fulfill the request."
	print "Error code:",e.code
except URLError,e:
	print "We failed to reach a server."
	print "Reason:",e.reason
else:
	print "No exception was raised."

