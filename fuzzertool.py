#!/usr/bin/python

import httplib
import sys

d1=open(sys.argv[2],"r")
dlist=d1.read().split('\n')

outfile=open("results.txt", "a")
print("\n\n***********************************************\n\n")
print ("Domain adresiniz:    {}".format(sys.argv[1]))
print ("Wordlistiniz:        {}".format(sys.argv[2]))
print("\n\n***********************************************\n\n\n")
for i in dlist:
	conn = httplib.HTTPConnection(sys.argv[1]," 80")
	url = "/"+str(i)
        print url
	conn.request('GET', url)
	resp = conn.getresponse()
	print resp.getheader("Server")
	print resp.getheader("Date")
	print resp.getheader("Cookie")
	respcode=resp.status
        respcoders=resp.reason
        print resp.status, resp.reason
        print("------------------------------------------\n")
	result="http://"+sys.argv[1]+url+" "+str(respcode)+" "+str(respcoders)+"\n"
	outfile.write(result)

d1.close()	
