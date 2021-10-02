import pandas as pd
df = pd.read_csv('siracuse.csv',header=None, names=['nb','nb_iter'], delimiter = ';')
print(df.max())
