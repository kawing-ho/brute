#!/usr/bin/env python3

# Enumerate and print until told to stop
# wordstr is the list of characters to enumerate
# counters is the initial number to start with ie. a vs aaaa


# Threads:
# 1) threads handle I/O
# 2) master thread handles ranges from threads to print
# 3) master generates and put line into q, workers get and print from q


wordstr = "abcdefghijklmnopqrstuvwxyz0123456789" #/Change as necessary/
l = len(wordstr)
counters = [0]

#recursively check the counter list from back to front
def indexCheck(index):
	
	#base case
	if index == 0:
		if counters[index] == l:
			counters[index] = 0
			#if all counters reach maximum, add new counter
			counters.append(0)
		return 0
	 
	#else recurse down list
	else : 
		if counters[index] == l:
			counters[index] = 0
			counters[index-1] +=1
		indexCheck(index-1)

while True:	#forever and ever and ever and ever ...
	
	indexCheck(len(counters)-1)
	
	#loop through counters and add corresponding char to print string
	p = ""
	for index in counters: 
		p += wordstr[index]
		
	#print the string
	print(p)
	
	#increase the counter  (current will always be counters[-1])
	counters[-1] += 1
	
