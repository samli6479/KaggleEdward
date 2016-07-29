'''
author = Edward, Li
'''
import numpy as np
import pandas as pd
import csv

def filereader(filename,filetype='csv',header=True,sep=",",colindex=None):
    '''
    read the raw data and return numpy array
    data is either csv or txt
    colindex is the index try to find
    '''
    
    opener = open(filename)
    
    if filetype == 'csv':
      reader = csv.reader(opener,delimiter=sep)
      
      if header:
         head = np.array(next(reader))[colindex]
         print(head)
         
      data = [np.array(row) for row in reader]

      if colindex:
         data = [tuple(item for item in row[colindex]) for row in data]
    
      return np.array(data)
    
    if filetype == 'txt':
      data = np.array(line.rstrip('\r\n') for line in opener)
      data = np.array(map(lambda x: x.split(sep), data))
      
      if header:
         head = data[0]
         data = np.array(filter(lambda a: a != head,data))
         print(np.array(head)[colindex])

      if colindex:
         data = [tuple(item for item in row[colindex]) for row in data]
     
      return np.array(data)

def intergized(data):
    '''
    Turn the data into integers for machine learning
    '''
    
    data = data.transpose()
    frame =[]
    for item in data:
        uniqueval = np.unique(item)
        length = len(uniqueval)
        maps = dict(zip(uniqueval,range(length)))
        datas = [maps[key] for key in item]
        frame.append(datas)
    return np.array(frame).transpose()

def normalize(data,method=False):
    '''
    normalize data with (data-mean)/std if method is True, otherwise (data-mean) 
    '''
    
    meanval = data.mean(axis=0)
    stdval = data.std(axis=0)
    
    if method:
       return (data-meanval)/stdval
    
    return data-meanval
    
    
