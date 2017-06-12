__author__ = 'Anouk Lang'

import codecs

stopwords = set(codecs.open('FrenchStopwords.txt', encoding='utf8').readlines())



countedwords = {}
in_file = codecs.open('le-musee.txt', encoding='utf8')
for line in in_file:
    tokenizedwords = tokenize_words(line)
    for word in tokenizedwords:
        countedwords.setdefault(word, 0)
        countedwords[word] += 1

#        if word in countedwords:
#            countedwords[word] += 1
#        else:
#            countedwords[word] = 1

out_file = codecs.open('output.txt', 'w', encoding='utf8')
for key, value in sorted(countedwords.items(), key=lambda x:x[1]):
    out_file.write(key + ': ' + str(value) + '\n')