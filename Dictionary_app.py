import json
from difflib import get_close_matches

data=json.load(open('data.json'))

def translate(word):
	word=word.lower()
	
	if word in data:
		return data[word]
	
	elif len(get_close_matches(word,data.keys())) > 0:
		
		yn=input('Did you mean "%s" instead? Y/N? '%get_close_matches(word,data.keys())[0])
		yn=yn.lower()
		
		if yn =="y":
			return data[get_close_matches(word,data.keys())[0]]
		elif yn == 'n':
			return 'Word does not exist.'
		else:
			return 'We did not understand your input.'
	
	elif w.title() in data:
		return data[w.title()]
	
	elif w.upper() in data:
		return data[w.upper()]
	
	else:
		return "Word doesn't exist.Please check it again." 



word=input('Enter word: ')
output=translate(word)

if type(output)==list:
	for defn in output:
		print("Definition: ",defn)
else:
	print(output)
