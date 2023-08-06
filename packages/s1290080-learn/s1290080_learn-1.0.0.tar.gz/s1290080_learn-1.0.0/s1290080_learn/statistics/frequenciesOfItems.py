import pandas as pd
import re

class frequenciesOfItems:
    def __init__(self, inputFile, sep='\t'):
        self.inputFile = inputFile
        self.sep = sep
        
    def getFrequencies(self):
        elm_cnt = {}
        df = pd.read_csv(self.inputFile, sep=self.sep)
        hd = re.findall('Point\(\s*-?\d+\.\d+\s*-?\d+\.\d+\s*\)', str(df.columns))
        for v in range(len(df)):
            lst = re.findall('Point\(\s*-?\d+\.\d+\s*-?\d+\.\d+\s*\)', str(df.iloc[v]))
            for v2 in lst:
                if v2 in elm_cnt:
                    elm_cnt[v2] += 1
                else:
                    elm_cnt[v2] = 1
        return elm_cnt
                    