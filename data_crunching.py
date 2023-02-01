import pandas as pd

def process_file(filename):
    # read the TSV file into a Pandas dataframe
    df = pd.read_csv(filename, sep='\t')
    
    # process the data as needed
    # ...
    
    return df

def aggregate_data(files):
    # initialize an empty dataframe
    aggregated_df = pd.DataFrame(columns=['Id', 'username', 'email', 'hashed password', 'plain text password', 'ip'])
    
    # process each file and concatenate the result to the aggregated dataframe
    for file in files:
        df = process_file(file)
        aggregated_df = pd.concat([aggregated_df, df], ignore_index=True)
    
    return aggregated_df

def main(files, output_file):
    aggregated_df = aggregate_data(files)
    
    # write the aggregated data to the output file
    aggregated_df.to_csv(output_file, sep='\t', index=False)

if __name__ == '__main__':
    files = ['user_email_hash.1m.tsv', 'ip_1m.tsv', 'plain_32m.tsv']
    output_file = 'output2.tsv'
    main(files, output_file)
