def palindrome(first):
	if (first==first[::-1]):
		print '"'+first + '" is a palindrome'
	else:
		print '"'+first + '" is not a palindrome'
		if (first.lower()==first.lower()[::-1]):
			print '...but "'+ first.lower() + '" is a palindrome. (Case-sensitive!)'
word1=raw_input('Word: ')
palindrome(word1)
