import pandas as pd
import numpy as np
import os 

# Small dataset: Student Scores

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Math Score': [85, 78, 92, 88, 76],
    'Science Score': [90, 82, 87, 85, 80],
    'English Score': [88, 79, 85, 90, 83]
}

df=pd.DataFrame(data)

data_dir="data"
os.makedirs(data_dir,exist_ok=True )

file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"csv file save to {file_path}")
