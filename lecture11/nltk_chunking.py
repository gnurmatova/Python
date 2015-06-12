import nltk
def extract_entities(text):
	for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
		print(chunk)


s="His Name was Charlie Chaplin!"
extract_entities(s)