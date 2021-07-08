import csv
import hashlib

def my_range(path):
    file = open(path)
    text = csv.reader(file)
    for row in text:
         mdpass = hashlib.md5(str( row).encode("utf-8")).hexdigest()
         yield   mdpass