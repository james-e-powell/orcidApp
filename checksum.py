import csv
import sys

arglist = sys.argv
orcidListCsv = arglist[1]

def generateCheckDigit(baseDigits):
  total = 0
  for i  in range(0, len(baseDigits)-1):
    try:
      digit = int(baseDigits[i])
      total = (total + digit) * 2
    except:
      pass
  remainder = total % 11
  result = (12 - remainder) % 11
  if result==10:
    return 'X'
  else:
    return str(result)
  
input_file = csv.DictReader(open(orcidListCsv))
for row in input_file:
  orcid = row['orcid']
  if not 'undefined' in orcid: 
    checksum = generateCheckDigit(orcid)
    if str(orcid[-1])==checksum:
      # print 'match ' + orcid[-1] + ',' + checksum
      pass
    else:
      print 'mismatch ' + orcid + ' checksums: '  + orcid[-1] + ',' + checksum
  else:
    print orcid
