# Source: https://stackoverflow.com/questions/19697846/python-csv-to-json

import csv
import json

csvfile = open('d3_data.csv', 'r')
jsonfile = open('d3_data.json', 'w')

fieldnames = ('School_ID','Short_Name','Long_Name','School_Type','Primary_Category','Address','Zip','School_Survey_Safety','num_crimes')
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)