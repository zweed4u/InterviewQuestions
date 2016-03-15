def count(arg):
	dict1={}
	for i in word:
		print i + ' occurs '+str(word.count(i))
		dict1.update({i:word.count(i)})
	print '\n'
	mostOccurences=max(dict1.values())
	if dict1.values().count(mostOccurences)>1:
		#tie for most occurences
		indexOfOccurences=[]
		for i in range(len(dict1.values())):
			if dict1.values()[i]==int(mostOccurences):
				indexOfOccurences.append(i)
		
		for i in indexOfOccurences:
			print dict1.keys()[i] +' is the most frequesnt character with '+str(mostOccurences)+' occurrences.'
	else:
		print dict1.keys()[dict1.values().index(mostOccurences)] +' is the most frequesnt character with '+str(mostOccurences)+' occurrences.'

	print '\n\n'+str(dict1)

word=raw_input('Word? ')
count(word)
