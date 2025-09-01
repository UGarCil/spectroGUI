# SpectroAnnotationTool

A PyQt5-based GUI tool for annotating chemical spectra images with bounding boxes and functional group labels.

## Features
- Display and navigate chemical spectra images
- Annotate images with bounding boxes
- Assign functional group labels to each bounding box via UI buttons
- Save annotations in COCO-like format per image
- Trash button to clear all annotations for the current image
- Responsive UI scaling
- Data and annotation folders tracked in Git (using `.gitkeep`)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/UGarCil/spectroGUI.git
   cd spectroGUI
   ```
2. Install dependencies:
   ```sh
   pip install pyqt5 numpy
   ```

## Usage
1. Place your PNG images in the `data/` folder.
2. Place your label numpy array (e.g., `subsa_labels_10000.npy`) in the `data/` folder.
3. Run the main GUI:
   ```sh
   python main.py
   ```
4. Annotate images by drawing bounding boxes and assigning labels.
5. Use the trash button to clear annotations for the current image.
6. Annotation files are saved in the `annotations/` folder, one `.txt` file per image.

## Annotation Format
Each annotation file is saved in tab-separated format:
```
label_idx    x    y    w    h
```
- `label_idx`: Index of the functional group label
- `x`, `y`, `w`, `h`: Relative coordinates and size of the bounding box

## Folder Tracking
- The `data/` and `annotations/` folders are tracked in Git using `.gitkeep` files, but their contents are ignored (see `.gitignore`).

## Requirements
- Python 3.6+
- PyQt5
- numpy


