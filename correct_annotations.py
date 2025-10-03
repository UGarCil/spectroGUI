#!/usr/bin/env python3
"""
Script to correct annotation files from top-left corner format to center format (proper YOLO format).

Original format: [class_id, top_left_x, top_left_y, width, height]
Target format:   [class_id, center_x, center_y, width, height]

The conversion is:
- center_x = top_left_x + (width / 2)
- center_y = top_left_y + (height / 2)
"""

import os
import glob

def correct_annotation_line(line):
    """
    Convert a single annotation line from top-left to center format.
    
    Args:
        line (str): A line containing annotation data
        
    Returns:
        str: The corrected line in center format
    """
    parts = line.strip().split('\t')
    
    if len(parts) != 5:
        print(f"Warning: Line has {len(parts)} parts instead of 5: {line.strip()}")
        return line
    
    try:
        class_id = int(parts[0])
        top_left_x = float(parts[1])
        top_left_y = float(parts[2])
        width = float(parts[3])
        height = float(parts[4])
        
        # Convert from top-left corner to center
        center_x = top_left_x + (width / 2)
        center_y = top_left_y + (height / 2)
        
        # Format the corrected line
        corrected_line = f"{class_id}\t{center_x}\t{center_y}\t{width}\t{height}\n"
        return corrected_line
        
    except ValueError as e:
        print(f"Error parsing line: {line.strip()}")
        print(f"Error: {e}")
        return line

def correct_annotation_file(file_path):
    """
    Correct all annotations in a single file.
    
    Args:
        file_path (str): Path to the annotation file
    """
    print(f"Processing: {file_path}")
    
    try:
        # Read all lines from the file
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Process each line
        corrected_lines = []
        for line_num, line in enumerate(lines, 1):
            if line.strip():  # Skip empty lines
                corrected_line = correct_annotation_line(line)
                corrected_lines.append(corrected_line)
            else:
                corrected_lines.append(line)  # Keep empty lines as-is
        
        # Write the corrected lines back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(corrected_lines)
        
        print(f"Successfully corrected {len([l for l in corrected_lines if l.strip()])} annotations in {os.path.basename(file_path)}")
        
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def main():
    """
    Main function to process all annotation files in the annotations directory.
    """
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    annotations_dir = os.path.join(script_dir, 'annotations')
    
    if not os.path.exists(annotations_dir):
        print(f"Annotations directory not found: {annotations_dir}")
        return
    
    # Find all .txt files in the annotations directory
    annotation_files = glob.glob(os.path.join(annotations_dir, '*.txt'))
    
    if not annotation_files:
        print("No annotation files (.txt) found in the annotations directory.")
        return
    
    print(f"Found {len(annotation_files)} annotation files to process.")
    print("Converting from top-left corner format to center format (proper YOLO format)...")
    print("-" * 70)
    
    # Process each file
    for file_path in sorted(annotation_files):
        correct_annotation_file(file_path)
    
    print("-" * 70)
    print(f"Processing complete! Corrected {len(annotation_files)} files.")
    print("All annotations are now in proper YOLO format (center coordinates).")

if __name__ == "__main__":
    main()
