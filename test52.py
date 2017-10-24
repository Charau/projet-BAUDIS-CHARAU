# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:44:23 2017

@author: lamac
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:58:50 2017

@author: lamac
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:01:59 2017

@author: lamac
"""
from PyQt5 import QtGui
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5 import QtWidgets 
from PyQt5 import QtGui

class window(QtWidgets.QWidget):
 
    def __init__(self):
        super(window, self).__init__()
        self.initUI()
        
    def initUI(self):
        # initialisation fenêtre
        self.setGeometry(600, 300, 1000, 600)
        self.setWindowTitle('GUI graphiques') 
        self.centre
        
        #initialisation grille
        grid=QtWidgets.QGridLayout()
        self.setLayout(grid)
        
        btn1 = QtWidgets.QPushButton('micro1',self)
        btn1.resize(btn1.sizeHint())
        btn1.clicked.connect(self.plot1)
        grid.addWidget(btn1, 2,0)
        
        btn2 = QtWidgets.QPushButton('micro2',self)
        btn2.resize(btn2.sizeHint())
        btn2.clicked.connect(self.plot2)
        grid.addWidget(btn2, 2,1)
        
        btn3 = QtWidgets.QPushButton('micro3',self)
        btn3.resize(btn3.sizeHint())
        btn3.clicked.connect(self.plot3)
        grid.addWidget(btn3, 2,2)
        
        btn4 = QtWidgets.QPushButton('micro4',self)
        btn4.resize(btn4.sizeHint())
        btn4.clicked.connect(self.plot4)
        grid.addWidget(btn4, 2,3)
        
        
        btn5 = QtWidgets.QPushButton('micro5',self)
        btn5.resize(btn5.sizeHint())
        btn5.clicked.connect(self.plot5)
        grid.addWidget(btn5, 3,0)
        
        btn6 = QtWidgets.QPushButton('micro6',self)
        btn6.resize(btn6.sizeHint())
        btn6.clicked.connect(self.plot6)
        grid.addWidget(btn6, 3,1)
        
        btn7 = QtWidgets.QPushButton('micro7',self)
        btn7.resize(btn7.sizeHint())
        btn7.clicked.connect(self.plot7)
        grid.addWidget(btn7, 3,2)
        
        btn8 = QtWidgets.QPushButton('micro8',self)
        btn8.resize(btn8.sizeHint())
        btn8.clicked.connect(self.plot8)
        grid.addWidget(btn8, 3,3)
        
        
        self.figure = plt.figure(figsize=(15,5))
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.canvas, 1,0,1,4)
        grid.addWidget(self.toolbar, 0,0,1,2)
        
        self.show()
     
    def plot1(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x =  np.linspace(0,10,100)#[i for i in range(100)]
        y =  np.sin(x)#[i**2 for i in x]
        ax.plot(x,y, 'b-')
        ax.set_title('micro1')
        self.canvas.draw()
        
    def plot2(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x = np.linspace(0, 10, 10)   #[i for i in range(100)]
        y = x**2 #[i**0.5 for i in x]
        ax.plot(x,y, 'r.-')
        ax.set_title('micro2') 
        self.canvas.draw()
        
    def plot3(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x =  np.linspace(0,10,100)#[i for i in range(100)]
        y =  np.sin(x)#[i**2 for i in x]
        ax.plot(x,y, 'b-')
        ax.set_title('micro3')
        self.canvas.draw()    
    
    def plot4(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x =  np.linspace(0,10,100)#[i for i in range(100)]
        y =  np.sin(x)#[i**2 for i in x]
        ax.plot(x,y, 'b-')
        ax.set_title('micro4')
        self.canvas.draw()   
        
    def plot5(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x =  np.linspace(0,10,100)#[i for i in range(100)]
        y =  np.sin(x)#[i**2 for i in x]
        ax.plot(x,y, 'b-')
        ax.set_title('micro5')
        self.canvas.draw()     
        
    def plot6(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x =  np.linspace(0,10,100)#[i for i in range(100)]
        y =  np.sin(x)#[i**2 for i in x]
        ax.plot(x,y, 'b-')
        ax.set_title('micro6')
        self.canvas.draw()  
        
    def plot7(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x =  np.linspace(0,10,100)#[i for i in range(100)]
        y =  np.sin(x)#[i**2 for i in x]
        ax.plot(x,y, 'b-')
        ax.set_title('micro7')
        self.canvas.draw()   
        
        
    def plot8(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x =  np.linspace(0,10,100)#[i for i in range(100)]
        y =  np.sin(x)#[i**2 for i in x]
        ax.plot(x,y, 'b-')
        ax.set_title('micro8')
        self.canvas.draw()  
    
    def centre(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().centre()
        qr.move(qr.topLeft())
        
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()    
        
        
if __name__ == '__main__':
       
     app =QtWidgets.QApplication(sys.argv)
     w = window()
     app.exec_()

        
         
    #if __name__ == '__main__':
       # main()
