# importar bibliotecas
import os
import pandas as pd
from fpgrowth_py import fpgrowth
import pickle

# ler arquivo
#dataset_path = '2023_spotify_ds1.csv'
dataset_path = os.getenv("DATASET", "app/datasets/2023_spotify_ds1.csv")
dataset = pd.read_csv(dataset_path)

# group by e to list
playlist_list = dataset.groupby('pid')['track_name'].apply(list).tolist()

# gerar regras fpgrowth
freqItemSet, rules = fpgrowth(playlist_list, minSupRatio=0.1, minConf=0.5)

'''
print("Exemplos de Regras:")
for rule in rules[:5]:  # Mostrar as primeiras 5 regras
    antecedent, consequent, confidence = rule
    print(f"Se {antecedent}, então {consequent} (confiança: {confidence:.2f})")
'''
    
# salvar em arquivo pickle
with open("/data/rules.pkl", 'wb') as file:
    pickle.dump(rules, file)