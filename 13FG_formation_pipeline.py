import os
import pandas as pd

## Step 1. Define the directory that stores the annotations.
dir_12FG = r"D:\spectroGUI\annotations"                                     # Directory of the 12FG (input / raw annotations)
dir_13FG = r"D:\spectroGUI\annotations_13FG"                                # Directory of the 13FG (output)
dir_results = r"D:\spectroGUI\FINAL_MODEL_AND_RESULTS\Annotations_Result"   # Directory of where the .csv is saved

## Step 1.1 Define the mapping rules for switching the label names
mapping_12FG = {
    0: "Aromatics",
    1: "Alcohols",
    2: "Amines",
    3: "Esters",
    4: "Alkenes",
    5: "Carb. acids",
    6: "Ketones",
    7: "Phenols",
    8: "Nitriles",
    9: "Amides",
    10: "Aldehydes",
    11: "Alkynes",
}
mapping_10FG = {
    0: "Aromatics",
    1: "Alcohols",
    2: "Amines",
    3: "Carbonyl_subgroups",    # Esters, Ketones, Aldehydes are collapsed
    4: "Alkenes",
    5: "Carb. acids",
    6: "Phenols",
    7: "Nitriles",
    8: "Amides",
    9: "Alkynes",
}
mapping_13FG = {
    0: "Aromatics",
    1: "Alcohols",
    2: "Amines_L",
    3: "Amines_R",
    4: "Carbonyl_subgroups",
    5: "Alkenes_L",
    6: "Alkenes_R",
    7: "Carb. acids",
    8: "Phenols",
    9: "Nitriles",
    10: "Amides_R",
    11: "Alkynes_L",
    12: "Alkynes_R",
}
mapping_13FG_reverse = {v: k for k, v in mapping_13FG.items()}  # Reverse the 13FG mapping in the end

## Step 2. For every .txt file in the annotation folder, extract every row and concatenate them into a dataframe
COCO_rows = []                                                                                  # Construct an empty list that stores the information of COCO formats
for name_txt in os.listdir(dir_12FG):                                                           # For every file inside the annotation folder path
    if name_txt.endswith(".txt"):                                                               # For every file that ends with ".txt", and does not contain "aug"
        path_txt = os.path.join(dir_12FG, name_txt)                                             # Construct the path of the current .txt file,
        with open(path_txt, 'r') as f:                                                          # and open it
            for COCO_lines in f:                                                                # For every line, extract their corresponding information
                COCO_parts = COCO_lines.strip().split()
                COCO_label = int(COCO_parts[0])
                COCO_x = float(COCO_parts[1])
                COCO_y = float(COCO_parts[2])
                COCO_width = float(COCO_parts[3])
                COCO_height = float(COCO_parts[4])
                COCO_rows.append([name_txt, COCO_label, COCO_x, COCO_y, COCO_width, COCO_height])   # Along with the current file name, converts them into a list that will be every row of the dataframe
df_12FG = pd.DataFrame(COCO_rows, columns=['file name', 'label', 'x', 'y', 'width', 'height'])      # Construct the dataframe based on every row
df_12FG['label'] = df_12FG['label'].replace(mapping_12FG)       # Re-name the labels based on 12FG mapping

## Step 3. Formation of the 10FG
df_10FG = df_12FG.copy()
## Refactor "Esters", "Ketones" and "Aldehydes" into "Carbonyl_subgroups"
df_10FG.loc[df_10FG['label'].isin(["Esters", "Ketones", "Aldehydes"]), 'label'] = "Carbonyl_subgroups"

## Step 4. Formation of the 13FG
df_13FG = df_10FG.copy()
## Step 4.1 Threshold point for these functional groups
threshold_Alkenes = float(0.4)
threshold_Alkynes = float(0.3)
threshold_Amines = float(0.4)
threshold_Amides = float(0.4)
## Alkenes
df_13FG.loc[(df_13FG['label'] == "Alkenes") & (df_13FG['x'] < threshold_Alkenes), 'label'] = "Alkenes_L"    ## =C-H
df_13FG.loc[(df_13FG['label'] == "Alkenes") & (df_13FG['x'] > threshold_Alkenes), 'label'] = "Alkenes_R"    ## C=C
## Alkynes
df_13FG.loc[(df_13FG['label'] == "Alkynes") & (df_13FG['x'] < threshold_Alkynes), 'label'] = "Alkynes_L"    ## ≡C-H
df_13FG.loc[(df_13FG['label'] == "Alkynes") & (df_13FG['x'] > threshold_Alkynes), 'label'] = "Alkynes_R"    ## C≡C
## Amines
df_13FG.loc[(df_13FG['label'] == "Amines") & (df_13FG['x'] < threshold_Amines), 'label'] = "Amines_L"       ## N-H stretch
df_13FG.loc[(df_13FG['label'] == "Amines") & (df_13FG['x'] > threshold_Amines), 'label'] = "Amines_R"       ## N-H bend
## Amides
df_13FG.loc[(df_13FG['label'] == "Amides") & (df_13FG['x'] < threshold_Amides), 'label'] = "Amines_L"       ## N-H stretch
df_13FG.loc[(df_13FG['label'] == "Amides") & (df_13FG['x'] > threshold_Amides), 'label'] = "Amides_R"       ## -C=O-N-

## Step 5. Saving the results
df_12FG.to_csv(os.path.join(dir_results, "12FG_annotations.csv"), index=False)
df_10FG.to_csv(os.path.join(dir_results, "10FG_annotations.csv"), index=False)
df_13FG.to_csv(os.path.join(dir_results, "13FG_annotations.csv"), index=False)

## Step 5.1 Rewrite the df_13FG as COCO labels
df_13FG_COCO = df_13FG.copy()
df_13FG_COCO['label'] = df_13FG_COCO['label'].map(mapping_13FG_reverse)     # Replace the alphabetical labels back to integers
df_13FG_COCO['label'] = df_13FG_COCO['label'].astype(int)                   # Explicitly convert the columns back to integers

## Step 5.2 Write every row to the designated .txt file as outputs.
grouped = df_13FG_COCO.groupby("file name")
for name_txt, group in grouped:
    path_txt = os.path.join(dir_13FG, name_txt)
    COCO_lines = group[['label', 'x', 'y', 'width', 'height']]
    COCO_lines.to_csv(path_txt, sep="\t", header=False, index=False)