#prints the word with the most reoccuring instances of a character in a string
def count(arg):
	dict1={}
	for i in arg:
		print i + ' occurs '+str(arg.count(i))
		dict1.update({i:arg.count(i)})
	print '\n'
	mostOccurences=max(dict1.values())
	if dict1.values().count(mostOccurences)>1:
		#tie for most occurences
		indexOfOccurences=[]
		for i in range(len(dict1.values())):
			if dict1.values()[i]==int(mostOccurences):
				indexOfOccurences.append(i)
		
		for i in indexOfOccurences:
			print dict1.keys()[i] +' is the most frequent character with '+str(mostOccurences)+' occurrences.'
		print '======================================================================'
	else:
		print dict1.keys()[dict1.values().index(mostOccurences)] +' is the most frequent character with '+str(mostOccurences)+' occurrences.'
		print '======================================================================'
		maxCount.append(arg)#word
		maxCount.append(dict1.keys()[dict1.values().index(mostOccurences)] )#letter
		maxCount.append(mostOccurences)#number of occurences

	print '\n\n'+str(dict1)

word=raw_input('Word? ')
word=word.split(' ')
maxCount=[]
for i in word:
	count(i.lower())
	print '\n'

count=0
indexOfMultipleMax=[]
numOccurrences = maxCount[2::3]
if numOccurrences.count(max(numOccurrences))>1:
	for i in numOccurrences:
		if i==max(numOccurrences):
			 indexOfMultipleMax.append(count)
		count+=1
	for i in indexOfMultipleMax:
		print "'"+maxCount[i*3]+"'" +' has the most reoccurring characters: '
		print 'letter: '+str(maxCount[(i*3)+1])
		print 'with '+str(maxCount[(i*3)+2])+' occurrences.'
		print '\n'
else:
	print "'"+maxCount[numOccurrences.index(max(numOccurrences))*3]+"'" +' has the most reoccurring characters: '
	print 'letter: '+str(maxCount[(numOccurrences.index(max(numOccurrences))*3)+1])
	print 'with '+str(maxCount[(numOccurrences.index(max(numOccurrences))*3)+2])+' occurrences.'
