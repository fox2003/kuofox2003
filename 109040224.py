import csv

infn = "input.csv"
outfn = "output.csv"


with open(infn) as csvRFile:
    csvReader = csv.reader(csvRFile)
    listReport = list(csvReader)
    
with open(outfn, 'w', newline='', encoding='utf8') as csvOFile:
    csvWriter = csv.writer(csvOFile)
    for row in listReport:
        csvWriter.writerow(row)
    csvWriter.writerow(["---------"])
    for row in listReport:
        csvWriter.writerow(row)
    csvWriter.writerow(["花茶", "15"])
    csvWriter.writerow(["密茶", "10"])
    
with open(outfn, encoding='utf8') as csvFile:
    csvReader = csv.reader(csvFile)
    listReport = list(csvReader)   
    for i in listReport:
        print(i)