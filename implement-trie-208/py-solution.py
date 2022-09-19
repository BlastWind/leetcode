# { "h": { "val": "e", "match": true, children: { "l": {"val": "e", "match": false, children: {}}}}}
#
#
#
#

from typing import Dict


class Trie:
	def __init__(self):
		self.dict = dict()

	def insert(self, word: str) -> None:
		iterator = self.dict
		for i in range(len(word)-1):
			letter = word[i]
			if letter not in iterator: 
				iterator[letter] = {"match": False, "children": {}}
			iterator = iterator[letter]["children"]
		# at last iter
	
		letter = word[len(word)-1]
		if letter not in iterator: 
			iterator[letter] = {"match": True, "children": {}}
		else: 
			iterator[letter]["match"] = True 

	def search(self, word: str) -> bool: # TODO: MIGHT NEED TO BE RECURSIVE?
		iterator = self.dict
		for i in range (len(word)-1):
			letter = word[i]
			if letter not in iterator:
				return False
			iterator = iterator[letter]["children"]
		# if inserted apple, but searching for app, return false
		letter = word[-1]
		return letter in iterator and letter in iterator and iterator[letter]["match"]

	def startsWith(self, prefix: str) -> bool:
		iterator = self.dict
		for letter in prefix:
			if letter not in iterator:
				return False
			iterator = iterator[letter].children
		return True

trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("appl"))
print(trie.search("apple"))

print(trie.search("app"))

print(trie)
# print(trie.search("app"))