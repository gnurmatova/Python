import nltk
def extract_entities(text):
	for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
		if(isinstance(chunk, nltk.tree.Tree)):
			for subtree in chunk.subtrees(filter=lambda t: t.label() == 'PERSON'):
				for leave in subtree.leaves():
					print(leave[0])


s="Who is Gula Nurmatova?"
extract_entities(s)