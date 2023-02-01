import csv

def aggregate_data(input_files, output_file):
   
    aggregated_data = []
    
    
    for input_file in input_files:
        with open(input_file, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
          
            next(reader)
            
            for row in reader:
                aggregated_data.append(row)
    
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
       
        writer.writerow(['Id', 'username', 'email', 'hashed_password', 'plaintext_password', 'ip'])
       
        writer.writerows(aggregated_data)


input_files = ['user_email_hash.1m.tsv', 'ip_1m.tsv', 'plain_32m.tsv']
output_file = 'output_data'
aggregate_data(input_files, output_file)