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




tagger = StanfordNERTagger('/Users/recordc/Documents/teenie/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz', '/Users/recordc/Documents/teenie/stanford-ner/stanford-ner.jar', encoding='utf-8')


txt = "Children, some in bathing suits, possibly including Rebecca Tab in center, Vernon Vaughn in light colored top, and Sara Mae Allen in back, standing on Webster Avenue under spray from fire hose, near Webster Avenue firehouse at Wandless Street, Hill District"

def extract_entities(text):    
     #for sent in nltk.sent_tokenize(text):
     names = []
     tokens = nltk.word_tokenize(text)
     tags = tagger.tag(tokens)
     #chunks = nltk.ne_chunk(tags)
     print tags
     name = ""
     cnt = 0
     for tag in tags:
         if (tag[1] == "PERSON"):
            if cnt > 0:
                name += " "
            name += tag[0]
            cnt += 1
         else:
            if cnt > 0:
                names.extend([name])
                cnt = 0
                name = ""
     return names




print extract_entities(txt)


