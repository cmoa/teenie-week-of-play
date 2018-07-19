from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
import nltk

import os

from nltk.parse import stanford
# ensure java 1.8 is running. Needs extra work around for new mac OS 
#https://stackoverflow.com/questions/34201990/unsupported-major-minor-version-on-mac-os-x-el-capitan
os.environ["JAVA_HOME"] = "/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home"

# must set environment variables to use standford tagger 
#https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software#stanford-tagger-ner-tokenizer-and-parser
os.environ["CLASSPATH"] = "/Users/recordc/Documents/teenie/stanford-ner"
os.environ["STANFORD_MODELS"] = "/Users/recordc/Documents/teenie/stanfordModelJar"


#print os.environ["JAVA_HOME"]
#print os.environ["CLASSPATH"]
#print os.environ["STANFORD_MODELS"]


def formatted_entities(classified_paragraphs_list):
   # print classified_paragraphs_list
    entities = {'persons': list(), 'organizations': list(), 'locations': list()}

    for classified_paragraph in classified_paragraphs_list:
        for entry in classified_paragraph:
            entry_value = entry[0]
            entry_type = entry[1]

            if entry_type == 'PERSON':
                entities['persons'].append(entry_value)

            elif entry_type == 'ORGANIZATION':
                entities['organizations'].append(entry_value)

            elif entry_type == 'LOCATION':
                entities['locations'].append(entry_value)

    return entities

tagger = StanfordNERTagger('/Users/recordc/Documents/teenie/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz', '/Users/recordc/Documents/teenie/stanford-ner/stanford-ner.jar', encoding='utf-8')
tagged = tagger.tag('Rami Eid is studying at Stony Brook University in NY'.split()) 
#chunks = nltk.ne_chunk(tagged)
print tagged
#chunks = nltk.ne_chunk(tags)
#text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

#tokenized_text = word_tokenize(text)
#classified_text = st.tag(tokenized_text)

#print(classified_text)

paragraphs = [
            'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.',
            "Apple Inc. is an American mul",
            "Samuel Patterson Smyth Sam Pollock, OC",
        ]

tokenized_paragraphs = list()

for text in paragraphs:
    tokenized_paragraphs.append(word_tokenize(text))

#lassified_paragraphs_list = tagger.tag_sents(tokenized_paragraphs)


#formatted_result = formatted_entities(classified_paragraphs_list)
#print(formatted_result)