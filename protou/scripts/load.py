import pandas as pd
from urania.models import Word
data = pd.read_csv('d:/protou/protou/scripts/lkc.csv')

dataframe = pd.DataFrame(data, columns=['Palabra', 'Emocion'])

for row in dataframe.itertuples():
    c = Word(word = row.Palabra,emocion=row.Emocion)
    c.save()

    
    


