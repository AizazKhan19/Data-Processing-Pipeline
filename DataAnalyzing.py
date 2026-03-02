# DataAnalyzer class is use to analyze the data which we cleaned using Datacleaner class.

from DataLoading import DataLoader
from Datacleaner import Datacleaner
import pandas as pd

# loading the data using DataLoader class
dloader = DataLoader('./data/train.csv')
df = dloader.load()

# cleaning the data using Datacleaner class
dcleaner = Datacleaner(df)
dataframe = dcleaner.dropping('Cabin')
dataframe = dcleaner.mean('Age')
dataframe = dcleaner.mode('Embarked')

# analyzing the data using DataAnalyzer class
class DataAnalyzer:
    def __init__(self,df):
        self.df = df

    # this function will return the total number of passengers in the dataset
    def Total_passengers(self):
        return len(self.df)
    
    #survial rate of the passengers
    def survival_rate(self):
        survival_percentage = (self.df['Survived'].mean()) * 100
        total_alive = self.df['Survived'].sum()
        total_deaths = len(self.df['Survived']) - total_alive
        return survival_percentage, total_alive, total_deaths
    
    # average age of the passengers
    def average_age(self):
        return self.df['Age'].mean()
    
    # gender distribution of the passengers
    def gender_count(self):
        return self.df['Sex'].value_counts()

    
    



data_analyzer=DataAnalyzer(dataframe)
print(f'Total Passengers : {data_analyzer.Total_passengers()}\n')
print(f'Survival Rate of Passengers : {data_analyzer.survival_rate()}\n')
print(f'Average Age of Passengers : {data_analyzer.average_age()}\n')
print(f'Gender Count of Passengers : {data_analyzer.gender_count()}\n')