from DataLoading import DataLoader
import pandas as pd

dloader = DataLoader('./data/train.csv') 
df = dloader.load()

class Datacleaner:
    def __init__(self, df):
        self.df = df

    # dropping column form the datafram
    def dropping(self, col):
        self.df = self.df.drop(columns = [col])
        # print(f' New frame after dropping column :\n {dropped}')
        return self.df
    
    # filling numerical data with average/mean of the entire column if an entry has NaN value
    def mean(self, col):
        mean_value = self.df[col].mean()
        self.df[col] = self.df[col].fillna(mean_value)
        return self.df
    
    # filling embarked column vlaues with most frequent values of the column
    def mode(self, col):
        mode_value = self.df[col].mode()[0]
        self.df[col] = self.df[col].fillna(mode_value)
        return self.df
        


if __name__ == '__main__':

    dcleaner = Datacleaner(df)
    # print(dcleaner.df)

    # dropping the cabin column
    dataframe = dcleaner.dropping('Cabin')
    # print(dataframe)

    # taking meanof age column and filling the null values with mean value of the column
    dataframe = dcleaner.mean('Age')
    # print(dataframe)

    # filling the null values of embarked column with most frequent value of the column
    dataframe = dcleaner.mode('Embarked')

    print(dcleaner.df.isnull().sum())