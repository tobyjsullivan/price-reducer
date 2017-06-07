import sys
import csv
import time
import numpy

with open('coinbaseUSD.csv', 'rb') as csvfile:
  pricereader = csv.reader(csvfile)
  lastdate = ''
  values = []
  for row in pricereader:
    datestamp = time.strftime('%Y-%m-%d', time.gmtime(float(row[0])))
    if lastdate != datestamp:
      if lastdate != '':
        median = numpy.median(values)
        out = [lastdate, str(median)]
        print ','.join(out)
        sys.stdout.flush()
      lastdate = datestamp
      values = []
    values.append(float(row[1]))
