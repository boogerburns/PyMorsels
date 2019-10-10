"""Hello!


This week we're going to normalize CSV files by writing a program, fix_csv.py, that turns a pipe-delimited file into a comma-delimited file. I'll explain how it should work by example.

Your original file will look like this:

Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257
You'll then run your script by typing this at the command line:

$ python fix_csv.py cars-original.csv cars.csv
Note : "$" is not typed; that is simply the beginning of the prompt.

Your fixed file should then look like this:

Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257
"""

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--in-delimitier', dest='delimiter', default='|')
parser.add_argument('--inputfile')
parser.add_argument('--outputfile')
args = parser.parse_args()

fieldnames = ['Reading', 'Make', 'Model', 'Type', 'Value']

with open(args.inputfile, 'rt') as file:
    reader = csv.reader(file, delimiter=args.delimiter)
    with open(args.outputfile, 'wt') as outfile:
        writer = csv.writer(outfile, 'excel', lineterminator='\n')
        for row in reader:
            writer.writerow(row)
