#!/usr/bin/python

import os.path
import re
import sys

basepath = os.path.dirname(__file__)
regex = re.compile("coords=\"(([0-9]|,)+)\"")
ratio = 0

def main():
	try:
		arg = sys.argv[1]
		oldWidth = sys.argv[2]
		newWidth = sys.argv[3]
		ratio = (100*int(newWidth))/int(oldWidth)

		filename = basepath + "\\" + arg
		if filename:
			f = open(filename, 'r')
			fnew = f.read()
			f.close()
			groups = regex.findall(fnew)
			for group in groups:
				buf = ""
				numbers = group[0].split(",")
				for number in numbers:
					buf = buf + str(resize(int(number), ratio)) + ","
				fnew = fnew.replace(group[0], buf[:-1]) 
			f = file(basepath + "\\" +"output.html", "w+")
			f.write(fnew)
			f.close()
			print fnew
	except:
		print "Usage: ./coords.py file.html oldwidth newwidth"

def resize(value, ratio):
	return (value*ratio)/100

main()
