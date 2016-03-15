def anagram(first,second):
	#print first
	#print second
	dict1={}
	dict2={}
	for i in list(first):
		dict1.update({i:first.count(i)})
	for j in list(second):
		dict2.update({j:second.count(j)})
	'''
	print dict1.keys()
	print dict2.keys()

	print dict1.values()
	print dict2.values()
	'''	
	if (set(dict1.keys()) == set(dict2.keys())) and (set(dict1.values()) == set(dict2.values())):
		print 'Anagram'
	else:
		print 'Not Anagram'

word1=raw_input('First word: ')
word2=raw_input('second word: ')

anagram(word1.lower(),word2.lower())
