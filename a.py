import pandas as pd

file_list = ['user_email_hash.1m.tsv',  'plain_32m.tsv' , 'ip_1m.tsv']

df_list = [pd.read_csv(f, sep='\t', header=None) for f in file_list]
df = pd.concat(df_list, axis=1, ignore_index=True)

col_names = ['Id', 'username', 'email', 'hashed_password', 'plaintext_password', 'ip']

df.to_csv("merged_file5.tsv", sep='\t', index=False, header=True)
