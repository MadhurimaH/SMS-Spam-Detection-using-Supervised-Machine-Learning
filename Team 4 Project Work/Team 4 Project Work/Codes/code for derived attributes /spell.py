from spellchecker import SpellChecker
spell = SpellChecker() # loads default word frequency list
def get(k):
    misspelled = spell.unknown(k)
    x=len(misspelled)
    return x
import pandas as pd
data=pd.read_csv(r"C:\Users\lenovo pc\Downloads\newspam.csv",encoding="ISO-8859-1")
data.to_csv(r"C:\Users\lenovo pc\Downloads\newspams.csv")
data['mis_spell']= data['Message'].apply(get)
df=data.loc[data['mis_spell'] > 0]
k=[]
k.append(df.loc[df['Category']=="ham"].shape[0])
k.append(df.loc[df['Category']=="spam"].shape[0])
