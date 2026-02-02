import os
import pandas as pd

# Step 1. For every .txt file in the annotation folder, extract every row and concatenate them into a dataframe
path_annotations = r"D:\spectroGUI\annotations"                 # The folder path that includes all annotations
COCO_rows = []                                                  # Construct an empty list that stores the information of COCO formats
for name_txt in os.listdir(path_annotations):                   # For every file inside the annotation folder path
    if name_txt.endswith(".txt"):                               # For every file that ends with ".txt"
        path_txt = os.path.join(path_annotations, name_txt)     # Construct the path of the current .txt file,
        with open(path_txt, 'r') as f:                          # and open it
            for COCO_lines in f:                                # For every line, extract their corresponding information
                COCO_parts = COCO_lines.strip().split()
                COCO_label = int(COCO_parts[0])
                COCO_x = float(COCO_parts[1])
                COCO_y = float(COCO_parts[2])
                COCO_width = float(COCO_parts[3])
                COCO_height = float(COCO_parts[4])
                COCO_rows.append([name_txt, COCO_label, COCO_x, COCO_y, COCO_width, COCO_height])       # Along with the current file name, converts them into a list that will be every row of the dataframe
df_annotations = pd.DataFrame(COCO_rows, columns=['file name', 'label', 'x', 'y', 'width', 'height'])   # Construct the dataframe based on every row

# Step 2. Isolate .txt files that have multiple annotations, save their information as a dataframe
df_annotations_duplicates = df_annotations.groupby("file name").size().reset_index(name="count")        # Calculate how many duplicates of every file name per .txt file
df_annotations_repeated = df_annotations_duplicates[df_annotations_duplicates["count"] > 1]             # Isolate .txt files that have multiple rows

# Step 3. Created a dataframe that calculates the occurrence of the duplicated labels
df_annotations_tracker = pd.DataFrame({"fg_label": list(range(12)), "total_count": [0]*12})
for file_name in df_annotations_repeated["file name"]:                                                  # For every .txt file that has multiple rows
    df_file_name = df_annotations[df_annotations["file name"] == file_name]                             # Extract their rows as a smaller dataframe
    df_fg_duplicates = df_file_name.groupby("label").size().reset_index(name="count")                   # Using the same strategy, calculate how many duplicates of every label per .txt file
    for _, row in df_fg_duplicates.iterrows():
        label = int(row["label"])
        count = int(row["count"])
        if count != 1:
            df_annotations_tracker.loc[label, "total_count"] += 1
print(df_annotations_tracker)
print("/"*30)

# Step 4. Query the users to check
while True:
    label_to_check = input("Please enter the label to check (or q to quit): ")
    if label_to_check == "q": break
    label_to_check = int(label_to_check)
    files_with_dup_label = (df_annotations.groupby(["file name", "label"]).size().reset_index(name="count").query("label == @label_to_check and count > 1")["file name"].tolist())
    print("Label %s has %s for multiple annotations" %(label_to_check, files_with_dup_label))
