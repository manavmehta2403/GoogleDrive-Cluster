import pandas as pd

corr_mat = {
    "A":[1],
    "B":[0.928307],
    "C":[0.479659],
    "D":[0.096756],
    "E":[0.599806],
    "F":[0.6741],
    "G":[0.925214],
    "H":[0.949403],
    "I":[0.940155]
    }

df = pd.DataFrame.from_dict(corr_mat,orient='columns')
print(df.corr(method='pearson'))
