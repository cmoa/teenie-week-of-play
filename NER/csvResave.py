import csv

# Open file of data 
# original file from drive has to be resaved from excel to work
csvfile = open('data/ecatalogResave2.csv', 'rb') 
readCSV = csv.reader(csvfile)
# create / open file to write to 
saveWithNewData = open('data/ecatalog-newData.csv', 'w')
writeNewCsv = csv.writer(saveWithNewData)

for row in readCSV:
        # confirm it is reading data by uncommenting line below
        # print row
        # to add data to a new column
		row.extend (["pretend data"])
		writeNewCsv.writerow(row)


saveWithNewData.close()
csvfile.close()
