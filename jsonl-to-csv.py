@author: Yasir hussain
"""


import glob
import json
import csv

import time


start = time.time()
#import pandas as pd
from flatten_json import flatten

#Path of jsonl file
    File_path = 'path-to-folder-that-contains-jsonl-files'
#reading all jsonl files
    files = [f for f in glob.glob( File_path + "**/*.jsonl", recursive=True)]
i=0
for f in files:
    with open(f, 'r') as F:
        for line in F:
#flatten json files 
            data = json.loads(line)
            data_1=flatten(data)
#creating csv files  
            with open('path-to-csv-file.csv', 'a' , newline='') as f:
                thewriter = csv.writer(f)
#headers should be the Key values from json files that make Coulmn header
                thewriter.writerow([data_1['header1'],data_1['header2']])
