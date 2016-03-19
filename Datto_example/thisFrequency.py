def freq(string):
	list=[];
	for word in string.split(' '):
		dict={};
		for letter in word:
			dict.update({letter:word.count(letter)})
		list.append(dict)
	for words in list:
		print words
	
word=raw_input('String: ')
freq(word.lower())
