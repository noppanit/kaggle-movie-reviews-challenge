import csv
class TrainDataGatherer:

    def get():
        with open('data/train.tsv') as infile:
            for line in csv.reader(infile, delimiter='\t'):
                print line
