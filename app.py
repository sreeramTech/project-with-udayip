import os
import random
import search
import jsonParser
from time import sleep 
items = {}
user_agent = ['Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36','Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1']
'''fatt = os.system('python3 fatt/fatt.py -r fatt/testbed.pcap -j')
if fatt == 1:
	exit(1)
sleep(4)'''
s = 0
hashes = jsonParser.jsonParser('fatt/fatt.log')
fp = open("trainingDataset.text","r")
lines = fp.readlines()
lines.pop(-1)
for line in lines:
	if line == '\n':
		continue
	word = line.rstrip('\n').split()
	items[word[0]] = word[1]
for hash in hashes:
	r = random.randint(0,2)
	if hash in items:
		print("%s:%s:%s"%(hashes[hash],user_agent[r],items[hash]))
	else:
		s = search.find(hash)
		if s == 1:
			print("%s:%s:DOS"%(user_agent[r],hashes[hash]))
		else:
			print("%s:%s:Not a threat"%(user_agent[r],hashes[hash]))


		



	

