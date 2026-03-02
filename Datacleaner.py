from DataLoading import DataLoader
import pandas as pd

dloader = DataLoader('./data/train.csv') 
df = dloader.load()

class Datacleaner:
    def __init__(self, df):
        self.df = df

    # dropping column form the datafram
    def dropping(self, col):
        dropped = self.df.drop(columns = [col])
        # print(f' New frame after dropping column :\n {dropped}')
        return dropped
        
dcleaner = Datacleaner(df)
# print(dcleaner.df)

dataframe = dcleaner.dropping('Cabin')
print(dataframe)

    