I used the pandas library to read three files. I used the pd.read_csv function to read each file, concatenated the columns of the resulting dataframes, and stored the result in the df. The column names for the final dataframe were assigned using the col_names list of strings. the final dataframe is saved as a .tsv file named "merged_file3.tsv".


to check the memory install memory_profiler. 
then import "from memory_profiler import profile"
then run the command "python -m memory_profiler your_script.py"