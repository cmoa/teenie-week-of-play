import nltk
import csv


def extract_entities(text):    
     Names = []
     for sent in nltk.sent_tokenize(text):
        tokens = nltk.word_tokenize(sent)
        tags = nltk.pos_tag(tokens)
        chunks = nltk.ne_chunk(tags)
        print chunks
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
        			Names.extend([name])
        return Names


def nametoString(lstName):
   # print lstName
    allNames = ""
    cnt = 0
    for name in lstName:
        if cnt > 0:
			allNames += ", "
        allNames += name
        cnt += 1
  #  print allNames
    return allNames


csvfile = open('data/ecatalogResave2.csv', 'rb') 

saveWithNewData = open('data/ecatalog-newData.csv', 'w')
writeNewCsv = csv.writer(saveWithNewData)

#csvfile = codecs.open('data/ecatalog.csv', 'rU', 'utf-8')

readCSV = csv.reader(csvfile)
#print readCSV
for row in readCSV:
        listNames = extract_entities(row[3])
        nm = nametoString(listNames)
        row.extend ([ nm])
        writeNewCsv.writerow(row)



saveWithNewData.close()
csvfile.close()
