import pandas as pd
import time 

start_time = time.time()
# Create an empty DataFrame with a specified number of rows and columns
num_rows = 1000000  # Adjust as needed
list_num_cols = [10, 100, 1000]

for num_columns in list_num_cols:
    df = pd.DataFrame(index=range(num_rows), columns=num_columns)

#print(df)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")