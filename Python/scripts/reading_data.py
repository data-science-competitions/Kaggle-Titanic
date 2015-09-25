import pandas as pd

## Relative Path
#train = pd.read_csv('./data/train.csv', index_col='PassengerId')
#test = pd.read_csv('./data/test.csv', index_col='PassengerId')

## Absolute Path
train = pd.read_csv('C:/Repositories/Titanic/data/train.csv', index_col='PassengerId')
test = pd.read_csv('C:/Repositories/Titanic/data/test.csv', index_col='PassengerId')
