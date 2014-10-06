from sys import argv

script, filename = argv


text = open(filename)
passage = text.read()
passage = passage.lower()
words = passage.split()



word_dict = {}

for word in words:

    word = word.strip("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

for item, count in word_dict.iteritems():
    print item + ": ", count