import numpy as np
import pandas as pd
import csv
import copy

def filereader(filename,filetype='csv',header=True,sep=","):
    '''read the raw data and return numpy array'''
    
    opener = open(filename)
    
    if filetype == 'csv':
      reader = csv.read(opener,delimiter=sep)
      
      if header:
         head = next(reader)
         
      data = [tuple(row) for row in reader]
    
    return np.array(data)
    
    if filetype == 'txt':
      data = [line.rstrip('\r\n') for line in opener]
      data = list(map(lambda x: x.split(sep), data))
      
      if header:
         head = data[0]
         
         data = list(filter(lambda a: a != head,data))
      
    return np.array(data)
