
# 'ROTOR'
# 'MOTOR'

def is_palindrome(word):
	flipped_word = ''
	# Clean Reverse Syntax
	for i in reversed(xrange(len(word))):
		flipped_word += word[i]
	return flipped_word == word

def is_palindrome_recursive(word):
	def flip(index):
		if index == 0:
			return word[0]
		return word[index] + flip(index - 1)
	return word == flip(len(word) - 1)
