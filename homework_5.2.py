"""
    homework_5.2.py -- sorting data from csv file by date
    Author: Winston Trinh (nvth@hotmail.com)
    Last Revised: 04/29/2024
"""

from datetime import datetime

source_fname = 'dated_file.csv'                     # str, 'dated_file.csv'
target_fname = 'sorted_file.csv'                    # str, 'sorted_file.csv'

def line_by_date(this_line):                        # str, '10/15/2018,A,B,28.3\n"
    data = this_line.rstrip().split(',')            # list, ['10/15/2018', 'A', 'B', '28.3']
    return datetime.strptime(data[0], '%m/%d/%Y')   # class 'datetime.datetime'>, 10/15/2018

# read the file into a list of lines
fh = open(source_fname)                             # file object
lines = fh.readlines()                              # list, ['10/15/2018,A,B,28.3\n', '09/03/2018,A,C,23.85\n'...]

slines = sorted(lines, key=line_by_date)            # list, ['12/06/2017,B,A,9.9\n', '12/13/2017,A,B,0.3\n'...]

# write the lines to a new file
wfh = open(target_fname, 'w')                       # class, <_io.TextIOWrapper name='sorted_file.csv' mode='w' encoding='cp1252'>

for line in slines:                                 # str, '12/06/2017,B,A,9.9'
    wfh.write(line)
wfh.close()

print(f'wrote to {target_fname}')
