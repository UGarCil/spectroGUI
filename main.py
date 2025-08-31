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


class App(MainWindow):
    def __init__(self, image_files, labels):
        super().__init__()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fg_indexes = [0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]
        self.image_files = image_files
        self.labels = labels
        self.index = 0
        self.update_image()
        # Connect navigation buttons
        self.ui.pushButton_3.clicked.connect(self.next_image)
        self.ui.pushButton_15.clicked.connect(self.prev_image)
        # Connect Go button
        self.ui.pushButton_2.clicked.connect(self.go_to_index)
        # Functional group indexes and button mapping
        

    def update_image(self):
        img_path = os.path.join(DATA_DIR, self.image_files[self.index])
        pixmap = QtGui.QPixmap(img_path)
        # Resize to QLabel size
        label_size = self.ui.label.size()
        pixmap = pixmap.scaled(label_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
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


    def next_image(self):
        if self.index < len(self.image_files) - 1:
            self.index += 1
            self.update_image()

    def prev_image(self):
        if self.index > 0:
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
    app = QtWidgets.QApplication(sys.argv)
    win = App(image_files, labels)
    win.show()
    sys.exit(app.exec_())
