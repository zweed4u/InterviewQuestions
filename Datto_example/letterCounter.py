#counts occurences for each character in string
def count(arg):
	dict1={}
	arg=arg.split(' ')
	for i in arg:
		for j in i:
			print j + ' occurs '+str(i.count(j))
		print '...in word "'+str(i)+'"'
		print '\n'
word=raw_input('Word? ')
count(word.lower())
