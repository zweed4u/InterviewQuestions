#finds the most occuring character in a string
def count(arg):
	dict1={}
	for i in arg:
		print i + ' occurs '+str(arg.count(i))
		dict1.update({i:arg.count(i)})
	print '...in string "'+str(arg)+'"'
	print '\n'
	mostOccurences=max(dict1.values())
	if dict1.values().count(mostOccurences)>1:
		#tie for most occurences
		indexOfOccurences=[]
		for i in range(len(dict1.values())):
			if dict1.values()[i]==int(mostOccurences):
				indexOfOccurences.append(i)
		for i in indexOfOccurences:
			print dict1.keys()[i] +' is the most frequent character in complete string with '+str(mostOccurences)+' occurrences.'
	else:
		print dict1.keys()[dict1.values().index(mostOccurences)] +' is the most frequent character in complete string with '+str(mostOccurences)+' occurrences.'
	
	print '\n\n'+str(dict1)+'\n'

word=raw_input('Word? ')
count(word.lower())
