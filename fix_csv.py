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
parser.add_argument('--in-delimiter', dest='delimiter')
parser.add_argument('--in-quote', dest='quote')
parser.add_argument('infile', nargs='?')
parser.add_argument('outfile', nargs='?')
args = parser.parse_args()

with open(args.infile, 'rt') as file:
    arguments = {}
    if args.delimiter:
        arguments['delimiter'] = args.delimiter
    if args.quote:
        arguments['quotechar'] = args.quote
    if not args.delimiter and not args.quote:
        arguments['dialect'] = csv.Sniffer().sniff(file.read())
        file.seek(0)
    reader = csv.reader(file, **arguments)
    with open(args.outfile, 'wt') as outfile:
        writer = csv.writer(outfile)
        for row in reader:
            writer.writerow(row)
