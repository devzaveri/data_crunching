import pandas as pd

FL = ['user_email_hash.1m.tsv',  'plain_32m.tsv' , 'ip_1m.tsv']

readD = [pd.read_csv(f, sep='\t', header=None) for f in FL]
df = pd.concat(readD, axis=1, ignore_index=True)

col_names = ['Id', 'username', 'email', 'hashed_password', 'plaintext_password', 'ip']

df.to_csv("merged_file.tsv", sep='\t', index=False, header=True)

