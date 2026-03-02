import pandas as pd
# class for loading data 
class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    # now funciton to read a file

    def load(self):
        df = pd.read_csv(self.file_path)
        return df



if __name__ == '__main__':
    
       dloader = DataLoader('./data/train.csv')
       df=dloader.load()
       print(df.head())
      
