import sys
from PyQt5.QtWidgets import (QApplication,QWidget, QLabel, QPushButton,QVBoxLayout,QHBoxLayout)
from PyQt5.QtCore import QTime,QTimer, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00",self)
        self.start_label = QPushButton("Start",self)
        self.stop_label = QPushButton("Stop",self)
        self.reset_label = QPushButton("Reset",self)
        self.timer= QTimer(self)
        self.initUI()
    def initUI(self):
            self.setWindowTitle("Stopwatch")
            
            vbox = QVBoxLayout()
            vbox.addWidget(self.time_label)
            vbox.addWidget(self.start_label)            
            vbox.addWidget(self.stop_label)            
            vbox.addWidget(self.reset_label)        
    def start(self):
        pass
        
    def stop(self):
        pass
    
    def reset(self):
        pass
    
    def format_time(self,time):
        pass
    
    def update_display(self):
        pass      
        
          
if __name__ =="__main__":
    app = QApplication(sys.argv)
    Stopwatch = Stopwatch()
    Stopwatch.show()
    sys.exit(app.exec_())