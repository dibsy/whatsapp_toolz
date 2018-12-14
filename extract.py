import sys
def extract():
	if len(sys.argv) != 2:
		print "Usage: python exract.py whataspp_chat.txt"
		return -1
	w = open(sys.argv[1],'r')
	data = w.readlines()
	for info in data:
		words = info.split(' ')
		for j in words:
			if j.find('http') > -1:
				print j
	w.close()
extract()
