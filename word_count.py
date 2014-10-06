from sys import argv
from operator import itemgetter

script, filename = argv


text = open(filename)
passage = text.read()
passage = passage.lower()
words = passage.split()

word_dict = {}

for word in words:

    word = word.strip("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
 
    word_dict[word] = word_dict.get(word, 0) + 1

counts = [(word,count) for word, count in word_dict.items()]
counts.sort()
sorted_word = sorted(counts, key=itemgetter(1), reverse = True)


for w, c in sorted_word:
    print w, ": ", c


