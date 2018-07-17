import nltk
import csv


csvfile = open('data/ecatalogResave2.csv', 'rb') 

saveWithNewData = open('data/ecatalog-newData.csv', 'w')
writeNewCsv = csv.writer(saveWithNewData)

#csvfile = codecs.open('data/ecatalog.csv', 'rU', 'utf-8')

readCSV = csv.reader(csvfile)
print readCSV
for row in readCSV:
		row.extend (["bye!!! (: "])
		writeNewCsv.writerow(row)



#writeNewCsv.writerows(readCSV)
saveWithNewData.close()

print "hihihih"


txt = "Ammon Pony League baseball team, first row from left: co-captain Ronald Jackson, Michael Simms, Kenneth Blackwell, Alan Taylor; second row: co-captain Robert Ryan, Ronald Broadway, Ralph Greene, John Jackson, Robert Marshall, George Weston, manager Edward Dean; third row: coach David Boggus and Rennard Braxton posed on field"


def extract_entities(text):
     for sent in nltk.sent_tokenize(text):
     	print "I'm in loop1"
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            print chunk
            if hasattr(chunk, 'JJ'):
                print "inside if"
                print chunk.node, ' '.join(c[0] for c in chunk.leaves())




def extract_entities2(text):          
     Names = []
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
        			Names.extend([name])
        print Names


def nametoString(lstName):
	allNames = ""
	cnt = 0
	for name in lstName:
		if cnt > 0:
			allNames += ", "
		allNames += name
	return allNames


extract_entities2(txt)
csvfile.close()
