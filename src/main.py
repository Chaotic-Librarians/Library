import sys

sys.path.insert(0,'src//')
import os
from gui.pageselect import PageSelect
from PyQt6.QtWidgets import QApplication

def myExitHandler():
    path = os.path.abspath('src/assets/covers/')
    for file_name in os.listdir(path):
        # construct full file path
        file = os.path.join(path, file_name)
        if os.path.isfile(file):
            #print('Deleting file:', file)
            os.remove(file)
def main():
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(myExitHandler)
    
    root = os.getcwd()
    stylesheet = os.path.join(root, os.path.abspath("src/GUI/styles.qss"))
    
    with open(stylesheet, "r") as file:
       app.setStyleSheet(file.read())
        
    application = PageSelect()
    app.exec()
        
if __name__ == "__main__":
    main()
    