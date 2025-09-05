import sys
import os
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from gui import MainWindow

# Get all PNG images in ./data
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
image_files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith('.png')])

# Load labels (update filename if needed)
LABELS_PATH = os.path.join(DATA_DIR, 'subsa_labels_10000.npy')
labels = np.load(LABELS_PATH)
assert labels.shape[0] == len(image_files), "Labels and images count mismatch!"


class Box:
    def __init__(self, x1, y1, label="", label_idx=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1
        self.y2 = y1
        self.label = label
        self.label_idx = label_idx
    def set_end(self, x2, y2):
        self.x2 = x2
        self.y2 = y2
    def get_rect(self):
        x = min(self.x1, self.x2)
        y = min(self.y1, self.y2)
        w = abs(self.x2 - self.x1)
        h = abs(self.y2 - self.y1)
        return x, y, w, h

class App(MainWindow):
    def save_annotations(self):
        # Save current annotations to a txt file in COCO format
        if not self.annotations:
            return
        # Create annotations folder if not exists
        ann_dir = os.path.join(os.path.dirname(__file__), 'annotations')
        if not os.path.exists(ann_dir):
            os.makedirs(ann_dir)
        # Get image filename and build annotation filename
        img_filename = self.image_files[self.index]
        ann_filename = os.path.splitext(img_filename)[0] + '.txt'
        ann_path = os.path.join(ann_dir, ann_filename)
        # Save each annotation in COCO format: label_idx x y w h
        with open(ann_path, 'w') as f:
            for i, ann in enumerate(self.annotations):
                label_idx = ann.get('label_idx', 0)
                line = f"{label_idx}\t{ann['x']}\t{ann['y']}\t{ann['w']}\t{ann['h']}\n"
                f.write(line)
        print(f"Saved annotations to {ann_path}")
        # Clear boxes and annotations
        self.boxes = []
        self.annotations = []
        
    def enable_edit_mode(self):
        self.cursor_settings["mode"] = "edit"
        
    def fit_pixmap_to_label(self, img_path):
        label_size = self.ui.label.size()
        pixmap = QtGui.QPixmap(img_path)
        # Resize to fit QLabel exactly (ignore aspect ratio)
        pixmap = pixmap.scaled(label_size, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
        return pixmap
    def __init__(self, image_files, labels):
        super().__init__()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fg_indexes = [0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]
        self.image_files = image_files
        self.labels = labels
        self.index = 0
        self.annotations = []  # List of dicts: [{x, y, w, h, label, label_idx}]
        self.boxes = []        # List of Box instances for current image
        self.cursor_settings = {"mode": "", "label": "base", "label_idx": 6}
        self.box = None        # Current box being drawn
        self.box_preview = None
        self.update_image()
        # Connect navigation buttons
        self.ui.pushButton_3.clicked.connect(self.next_image)
        self.ui.pushButton_15.clicked.connect(self.prev_image)
        # Connect Go button
        self.ui.pushButton_2.clicked.connect(self.go_to_index)
        # Connect Edit button
        self.ui.pushButton_28.clicked.connect(self.enable_edit_mode)
        # Connect trash button
        self.ui.pushButton_27.clicked.connect(self.clear_annotations)
        # Connect functional group buttons to label setter
        for idx, btn_name in enumerate(self.button_names):
            btn = getattr(self.ui, btn_name)
            btn.clicked.connect(lambda checked, idx=idx, btn=btn: self.set_box_label(btn.text(), idx))
        # Enable mouse tracking on label
        self.ui.label.setMouseTracking(True)

    def clear_annotations(self):
        # Clear boxes and annotations, redraw image
        self.boxes = []
        self.annotations = []
        self.box = None
        self.box_preview = None
        self.draw_all_boxes()

    def set_box_label(self, label, label_idx):
        self.cursor_settings["label"] = label
        self.cursor_settings["label_idx"] = label_idx


    def update_image(self):
        ## Save annotations before changing image   # Commented by Martin
        # self.save_annotations()                   # Commented by Martin
        img_path = os.path.join(DATA_DIR, self.image_files[self.index])
        pixmap = self.fit_pixmap_to_label(img_path)
        self.ui.label.setPixmap(pixmap)
        # Update index label
        self.ui.label_3.setText(f"index: {self.index}")

        label_row = self.labels[self.index]
        fg_values = [label_row[i] for i in self.fg_indexes]
        for btn_name, value in zip(self.button_names, fg_values):
            btn = getattr(self.ui, btn_name)
            if value == 1:
                btn.setStyleSheet('background-color: green;')
            else:
                btn.setStyleSheet('')

        # Clear box preview for new image
        self.box = None
        self.box_preview = None

    def mousePressEvent(self, event):
        if self.cursor_settings["mode"] == "edit":
            label = self.ui.label
            if event.button() == QtCore.Qt.LeftButton:
                pos = label.mapFromParent(event.pos())
                if label.rect().contains(pos):
                    # Start box on press, use current label and label_idx
                    self.box = Box(pos.x(), pos.y(), label=self.cursor_settings["label"], label_idx=self.cursor_settings["label_idx"])
                    self.box_preview = True
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if self.cursor_settings["mode"] == "edit":
            label = self.ui.label
            if event.button() == QtCore.Qt.LeftButton and self.box is not None and self.box_preview:
                pos = label.mapFromParent(event.pos())
                if label.rect().contains(pos):
                    # Finalize box on release
                    self.box.set_end(pos.x(), pos.y())
                    x, y, w, h = self.box.get_rect()
                    rel_x = x / label.width()
                    rel_y = y / label.height()
                    rel_w = w / label.width()
                    rel_h = h / label.height()
                    annotation = {
                        "x": rel_x,
                        "y": rel_y,
                        "w": rel_w,
                        "h": rel_h,
                        "label": self.box.label,
                        "label_idx": self.box.label_idx
                    }
                    self.annotations.append(annotation)
                    self.boxes.append(self.box)
                    self.box_preview = False
                    self.box = None
                    self.draw_all_boxes()
                    print("Annotations:", self.annotations)
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.cursor_settings["mode"] == "edit" and self.box is not None and self.box_preview:
            label = self.ui.label
            pos = label.mapFromParent(event.pos())
            if label.rect().contains(pos):
                self.box.set_end(pos.x(), pos.y())
                self.draw_all_boxes(preview=True)
        super().mouseMoveEvent(event)

    def draw_all_boxes(self, preview=False):
        # Draw all boxes (static and preview) on the image
        img_path = os.path.join(DATA_DIR, self.image_files[self.index])
        pixmap = self.fit_pixmap_to_label(img_path)
        painter = QtGui.QPainter(pixmap)
        font = QtGui.QFont()
        font.setPointSize(12)
        painter.setFont(font)
        # Draw static boxes
        painter.setPen(QtGui.QPen(QtCore.Qt.green, 3, QtCore.Qt.SolidLine))
        for box in self.boxes:
            x, y, w, h = box.get_rect()
            painter.drawRect(x, y, w, h)
            # Draw label text at top-left of box
            painter.setPen(QtGui.QPen(QtCore.Qt.black))
            painter.drawText(x + 2, y + 16, str(box.label))
            painter.setPen(QtGui.QPen(QtCore.Qt.green, 3, QtCore.Qt.SolidLine))
        # Draw preview box (red)
        if preview and self.box is not None:
            painter.setPen(QtGui.QPen(QtCore.Qt.red, 3, QtCore.Qt.SolidLine))
            x, y, w, h = self.box.get_rect()
            painter.drawRect(x, y, w, h)
            painter.setPen(QtGui.QPen(QtCore.Qt.black))
            painter.drawText(x + 2, y + 16, str(self.box.label))
        painter.end()
        self.ui.label.setPixmap(pixmap)


    def next_image(self):
        if self.index < len(self.image_files) - 1:
            self.save_annotations()                 # Added by Martin
            self.index += 1
            self.update_image()

    def prev_image(self):
        if self.index > 0:
            self.save_annotations()                 # Added by Martin
            self.index -= 1
            self.update_image()

    def go_to_index(self):
        text = self.ui.plainTextEdit.toPlainText().strip()
        try:
            idx = int(text)
        except ValueError:
            idx = 0
        if idx < 0:
            idx = 0
        elif idx >= len(self.image_files):
            idx = len(self.image_files) - 1
        self.index = idx
        self.update_image()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Right:
            self.next_image()
        elif event.key() == QtCore.Qt.Key_Left:
            self.prev_image()
        else:
            super().keyPressEvent(event)

if __name__ == "__main__":
    cursor_settings = {"mode":"", "label":"", "label_idx":None}
    app = QtWidgets.QApplication(sys.argv)
    win = App(image_files, labels)
    win.show()
    sys.exit(app.exec_())

