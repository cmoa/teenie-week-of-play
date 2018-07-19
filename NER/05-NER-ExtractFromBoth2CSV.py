from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
import nltk
import os
import csv

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

# test online
# http://nlp.stanford.edu:8080/ner/process
# core CLP 
# http://corenlp.run/
tagger = StanfordNERTagger('/Users/recordc/Documents/teenie/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz', '/Users/recordc/Documents/teenie/stanford-ner/stanford-ner.jar', encoding='utf-8')


txt = "Board of Education of Central Baptist Church members, seated, from left: Josephine Moore, Edith Venable, guest of honor; Rev. W. Augustus Jones, Mrs. Isaac Green, and Bell Lunn; standing:  A.D. Taylor, Andrew Brookins, Catherine Graham, Robert Bailey, Evelyn Young, Isaac Willoughby, Christine Jones, Jack Fisher, Oplenell Rockamore, Clarence Payne, and Helen Thompson, gathered in Central Baptist Church for baby shower, another version"


# lil' helper to change from array to csv ready string 
def nametoString(lstName):
   # print lstName
    #print type(lstName)
    allNames = ""
    cnt = 0
    for name in lstName:
        if cnt > 0:
            allNames += ", "
        allNames += name
        cnt += 1
  #  print allNames
    return allNames

def extract_entities_NLTK(text): 
     # names (1), num of Names, organizations(2), locations(3), GPE
     allNER = [[],[],[],[],[]]   

     #Names = []
     for sent in nltk.sent_tokenize(text):
        tokens = nltk.word_tokenize(sent)
        tags = nltk.pos_tag(tokens)
        chunks = nltk.ne_chunk(tags)
        for i in chunks:
            if type(i) == nltk.tree.Tree:
                if i.label() == "PERSON":
                    name = ""
                    count = 0
                    for leaf in i:
                        if count > 0:
                            name += " "
                        name += leaf[0]
                        count += 1
                    allNER[0].extend([name])
                elif i.label() == "ORGANIZATION":
                    name = ""
                    count = 0
                    for leaf in i:
                        if count > 0:
                            name += " "
                        name += leaf[0]
                        count += 1
                    allNER[2].extend([name])
                elif i.label() == "LOCATION":
                    name = ""
                    count = 0
                    for leaf in i:
                        if count > 0:
                            name += " "
                        name += leaf[0]
                        count += 1
                    allNER[3].extend([name])
                elif i.label() == "GPE":
                    name = ""
                    count = 0
                    for leaf in i:
                        if count > 0:
                            name += " "
                        name += leaf[0]
                        count += 1
                    allNER[4].extend([name])
        allNER[1].extend([str(len(allNER[0]))])
        allAsStrings = []
        for lis in allNER:
            asStr = nametoString(lis)
            allAsStrings.extend([asStr])
        return allAsStrings

def extract_entities_Stanford(text):    
     # names (1), number of names , organizations(2), locations(3)
     allNER = [[],[],[],[]]
     tokens = nltk.word_tokenize(text)
     tags = tagger.tag(tokens)
     nerId = 0
     for tag in tags:
         if (tag[1] == "PERSON"):
            if nerId == 1:
                allNER[0][len(allNER[0])-1] += " "
            else:
                nerId = 1
                allNER[0].extend([""])
            allNER[0][len(allNER[0])-1] += tag[0]
         elif (tag[1] == "ORGANIZATION"):
            if nerId == 2:
                allNER[2][len(allNER[2])-1] += " "
            else:
                nerId = 2
                allNER[2].extend([""])
            allNER[2][len(allNER[2])-1] += tag[0]
         elif (tag[1] == "LOCATION"):
            if nerId == 3:
                allNER[3][len(allNER[3])-1] += " "
            else:
                nerId = 3
                allNER[3].extend([""])
            allNER[3][len(allNER[3])-1] += tag[0]
         else:
            nerId =0

         
     allNER[1].extend([str(len(allNER[0]))])
     allAsStrings = []
     for lis in allNER:
        asStr = nametoString(lis)
        allAsStrings.extend([asStr])
     return allAsStrings







csvfile = open('data/ecatalogResave2.csv', 'rb') 

saveWithNewData = open('data/ecatalog-newData-3.csv', 'w')
writeNewCsv = csv.writer(saveWithNewData)

#csvfile = codecs.open('data/ecatalog.csv', 'rU', 'utf-8')

readCSV = csv.reader(csvfile)
#print readCSV
writeNewCsv.writerow(["Main Title" ,"Person-A", "# Person-A",  "Org-A", "Loc-A","Person-N", "# Person-N", "Org-N","Loc-N", "Gpe-N", "Person-S", "# Person-S",  "Org-S", "Loc-S"] )

for row in readCSV:
    newRow = []
    newRow.extend([row[3]," "," "," "," "])
    getN = extract_entities_NLTK(row[3])
    newRow.extend(getN)
    getS = extract_entities_Stanford(row[3])
    newRow.extend(getS)
    #nm = nametoString(listNames)
    #row.extend ([ nm])
    writeNewCsv.writerow(newRow)




saveWithNewData.close()
csvfile.close()

#print extract_entities_Stanford(txt)
#print extract_entities_NLTK(txt)


