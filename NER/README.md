## Extracting named entities into the correct fields

# NLTK install instructions

If you are on a mac you must make sure you are using java 1.8 and set a class variable following these [instructions](https://stackoverflow.com/questions/34201990/unsupported-major-minor-version-on-mac-os-x-el-capita). 

in the code that uses stanford NER you need to change this filepath to match yours. See link above.
os.environ["JAVA_HOME"] = "/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home"

must download the stanford [NER directory](https://nlp.stanford.edu/software/CRF-NER.shtml) and [model](https://stanfordnlp.github.io/CoreNLP/download.html) set environment variables to use standford tagger.
There are full instructions from NLTK [here](https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software#stanford-tagger-ner-tokenizer-and-parser ) but I only had to download the linked to packages to just use NER.
os.environ["CLASSPATH"] = "/Users/recordc/Documents/teenie/stanford-ner"
os.environ["STANFORD_MODELS"] = "/Users/recordc/Documents/teenie/stanfordModelJar"

pip install nltk should do it

# standford NER install instructions

csvResave.py - Simple code to read csv file and re-write into a new one.  

01-NER.py - Applying the NER built into NLTK and applying it to the sample data and resaving as a new CSV “data/ecatalog-NLTK.csv”

02-NER-stanford-justName.py - applying Stanford’s NER to find just the names 

05-NER-both-2.py - applying both the built in NER in NLTK and Stanford NER to data and saving out in a new spreadsheet “data/”


Stanford 73% accurate out of the box per title
56% of error due to place names being confused with people names, 
19% due to nicknames
11% due to places being named after people
11% trivial spacing problems, 
15% for truly miscellaneous reasons

If we could eliminate the rest of the error while still having the misc we would be up to 90-96% accurate
