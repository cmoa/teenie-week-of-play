import csv, re, spacy, textacy
from spacy.symbols import *

nlp = spacy.load('en_core_web_sm')

# TOOLS:
#   - python
#   - regex
#   - spacy
#   - textacy

# 1. trim descriptions
#   - trailing ", another version" or ", another pose"
#   - remove blocks of named individuals: including, clockwise, from left, to right, standing, seated, kneeling, front row, first row, back row, last row, second row, middle row

# 2. handle common variants:
#   - "Portrait of X"
#   - "Group Portrait of X"
#   - "Members of X"

# 3. handle other variants:
#   - subject, verb, object?
#   - trailing prepositional phrases? ("at X")

# trim unneccessary trailing phrases
def trim_trailing(text):
    return re.sub(', another (version|pose)\s*$', '', text)

# remove blocks of named individuals marked by e.g. "from left:"
def remove_individuals(text):
    return re.sub('', '', text)

# generator function to yield noun part subtrees
# from: https://stackoverflow.com/a/33512175
np_labels = set([nsubj, nsubjpass, dobj, iobj]) # Probably others too
def iter_nps(doc):
    for word in doc:
        if word.dep in np_labels:
            yield word.subtree

with open('ecatalog.csv', 'rb') as csvfile:
    rows = csv.reader(csvfile)
    for index, row in enumerate(rows):
        if index == 0: continue
        title = trim_trailing(unicode(row[3]))
        title = remove_individuals(title)
        if title != unicode(row[3]): print(title)

        doc = nlp(title)

        # for t in textacy.extract.subject_verb_object_triples(doc):
        #     for word in t:
        #         print word.text
        
        # for np in iter_nps(doc):
        #     for word in np:
        #         print(word, word.dep_)