import requests
import os
import pandas as pd

path_to_save = 'data/'
links_to_extract = {
    "TCABR": "https://portal.if.usp.br/controle/sites/portal.if.usp.br.ifusp/files/TCABR.txt",
    "HELIMAK": "https://portal.if.usp.br/controle/sites/portal.if.usp.br.ifusp/files/Helimak.txt"
}
col_names = ["time", "probe_a", "probe_b"]

if not os.path.exists(path_to_save):
    os.makedirs(path_to_save)


for k in links_to_extract.keys():
    txt = requests.get(links_to_extract[k]).text
    txt = txt.split('\n')

    data = []
    for l in txt:
        data.append(list(filter(None, l.lstrip().split('  '))))
    
    pd.DataFrame(data, columns=col_names).to_csv(path_to_save + k + ".csv", index=False)
