import pandas as pd
import json

## Return the row of the image_id that user inputs
def lookup_image(df):
    while True:
        try:
            user_input = input("Enter an image_id (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting lookup.")
                break
            image_id = int(user_input)
            result = df[df['image_id'] == image_id]
            if result.empty:
                print(f"No entry found for image_id {image_id}.")
            else:
                print(result.to_string(index=False))
                print("-" * 60)  # Line separator
        except ValueError:
            print("Please enter a valid integer image_id or 'exit'.")

## Main Starts Here
# Read the json file
with open('cached_metadata.json', 'r') as f:
    cached_metadata = json.load(f)

# Save the json file as a dataframe
df = pd.DataFrame({'image_path': cached_metadata['image_paths'], 'label': cached_metadata['labels']})

# Perform a dataclean - find digits that appear right before .png at the end of the string (aka the SDBS number)
df['SDBS_no'] = df['image_path'].str.extract(r'(\d+)\.png$')

# Data_id: Starting from 0, all the way to the length of the dataframe
df['image_id'] = list(range(len(df)))

# Drop the "image_path" column
df = df.drop(columns=['image_path'])
df = df[['image_id', 'SDBS_no', 'label']]

# Export the results as a csv
df.to_csv('cached_metadata.csv', index=False)

lookup_image(df)